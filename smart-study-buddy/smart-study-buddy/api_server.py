"""
Smart Study Buddy - FastAPI Server
Production-ready API for Smart Study Buddy
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
import uvicorn

from src.study_buddy import SmartStudyBuddy
from src.prompts import AUDIENCE_LEVELS, TONES, LENGTHS

# Initialize FastAPI
app = FastAPI(
    title="Smart Study Buddy API",
    description="Adaptive AI tutor that explains any topic to any audience",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class ExplanationRequest(BaseModel):
    topic: str = Field(..., description="Topic to explain", example="quantum physics")
    audience: str = Field(
        default="beginner",
        description="Audience level",
        example="middle_school"
    )
    tone: Optional[str] = Field(
        None,
        description="Explanation tone",
        example="neutral"
    )
    length: Optional[str] = Field(
        None,
        description="Explanation length",
        example="medium"
    )
    provider: str = Field(
        default="openai",
        description="AI provider to use",
        example="openai"
    )
    stream: bool = Field(
        default=False,
        description="Stream response"
    )


class ExplanationResponse(BaseModel):
    topic: str
    audience: str
    explanation: str
    metadata: dict


class HealthResponse(BaseModel):
    status: str
    version: str


# Initialize buddy (reused across requests)
buddy_instances = {}


def get_buddy(provider: str = "openai"):
    """Get or create buddy instance"""
    if provider not in buddy_instances:
        buddy_instances[provider] = SmartStudyBuddy(provider=provider)
    return buddy_instances[provider]


# Routes
@app.get("/", response_model=HealthResponse)
async def root():
    """Health check endpoint"""
    return HealthResponse(status="healthy", version="1.0.0")


@app.get("/health", response_model=HealthResponse)
async def health():
    """Health check endpoint"""
    return HealthResponse(status="healthy", version="1.0.0")


@app.get("/options")
async def get_options():
    """Get available options for audiences, tones, and lengths"""
    return {
        "audiences": AUDIENCE_LEVELS,
        "tones": TONES,
        "lengths": LENGTHS
    }


@app.post("/explain", response_model=ExplanationResponse)
async def explain(request: ExplanationRequest):
    """
    Generate an explanation for a topic
    
    - **topic**: What to explain
    - **audience**: Who to explain it to (see /options for choices)
    - **tone**: Optional tone preference
    - **length**: Optional length preference
    - **provider**: AI provider (openai or anthropic)
    """
    try:
        buddy = get_buddy(request.provider)
        
        explanation = buddy.explain(
            topic=request.topic,
            audience=request.audience,
            tone=request.tone,
            length=request.length,
            stream=False  # API doesn't support streaming yet
        )
        
        return ExplanationResponse(
            topic=request.topic,
            audience=request.audience,
            explanation=explanation,
            metadata={
                "tone": request.tone,
                "length": request.length,
                "provider": request.provider
            }
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/batch")
async def batch_explain(
    topics: list[str],
    audience: str = "beginner",
    tone: Optional[str] = None,
    length: Optional[str] = None,
    provider: str = "openai"
):
    """
    Explain multiple topics for the same audience
    
    - **topics**: List of topics to explain
    - **audience**: Audience level
    - **tone**: Optional tone
    - **length**: Optional length
    - **provider**: AI provider
    """
    try:
        buddy = get_buddy(provider)
        
        results = []
        for topic in topics:
            explanation = buddy.explain(
                topic=topic,
                audience=audience,
                tone=tone,
                length=length
            )
            
            results.append({
                "topic": topic,
                "explanation": explanation
            })
        
        return {
            "audience": audience,
            "results": results,
            "metadata": {
                "tone": tone,
                "length": length,
                "provider": provider,
                "count": len(topics)
            }
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(
        "api_server:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
