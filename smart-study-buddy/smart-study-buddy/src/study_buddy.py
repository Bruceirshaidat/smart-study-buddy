"""
Smart Study Buddy - Main Application Class
"""

from typing import Optional, Generator
from src.ai_client import AIClient
from src.prompts import SYSTEM_PROMPT, create_user_prompt, AUDIENCE_LEVELS


class SmartStudyBuddy:
    """Main Smart Study Buddy application class"""
    
    def __init__(self, provider: str = "openai", model: str = None):
        """
        Initialize Smart Study Buddy
        
        Args:
            provider: "openai" or "anthropic"
            model: Specific model to use (optional)
        """
        self.client = AIClient(provider=provider, model=model)
        self.system_prompt = SYSTEM_PROMPT
        self.conversation_history = []
    
    def explain(
        self,
        topic: str,
        audience: str,
        tone: Optional[str] = None,
        length: Optional[str] = None,
        stream: bool = False
    ) -> str | Generator:
        """
        Generate an explanation for a topic
        
        Args:
            topic: What to explain
            audience: Who to explain it to (age/level)
            tone: Optional tone preference
            length: Optional length preference
            stream: Whether to stream the response
        
        Returns:
            Explanation text or generator for streaming
        """
        # Resolve audience shorthand
        audience = AUDIENCE_LEVELS.get(audience, audience)
        
        # Create user prompt
        user_prompt = create_user_prompt(topic, audience, tone, length)
        
        # Store in conversation history
        self.conversation_history.append({
            "topic": topic,
            "audience": audience,
            "tone": tone,
            "length": length,
            "prompt": user_prompt
        })
        
        # Generate explanation
        if stream:
            return self.client.stream_explanation(self.system_prompt, user_prompt)
        else:
            explanation = self.client.generate_explanation(self.system_prompt, user_prompt)
            self.conversation_history[-1]["explanation"] = explanation
            return explanation
    
    def explain_interactive(self, topic: str):
        """
        Interactive explanation with follow-up questions
        
        Args:
            topic: Initial topic to explain
        """
        print(f"\n🎓 Smart Study Buddy - Explaining: {topic}\n")
        print("=" * 60)
        
        # Get audience level
        print("\nWho is this for?")
        for key, desc in AUDIENCE_LEVELS.items():
            print(f"  • {key}: {desc}")
        
        audience = input("\nEnter audience level: ").strip()
        
        # Get optional preferences
        tone = input("Tone (playful/neutral/academic/professional) [optional]: ").strip() or None
        length = input("Length (short/medium/detailed) [optional]: ").strip() or None
        
        print(f"\n{'=' * 60}\n")
        print("Generating explanation...\n")
        
        # Generate and display
        explanation = self.explain(topic, audience, tone, length)
        print(explanation)
        
        print(f"\n{'=' * 60}\n")
        
        # Offer follow-up
        follow_up = input("Would you like to ask a follow-up question? (yes/no): ").strip().lower()
        if follow_up in ['yes', 'y']:
            question = input("What's your question? ")
            # This would continue the conversation (simplified for now)
            print("\n✨ Follow-up feature coming soon!")
    
    def batch_explain(self, topics: list, audience: str, **kwargs):
        """
        Explain multiple topics for the same audience
        
        Args:
            topics: List of topics to explain
            audience: Audience level
            **kwargs: Additional parameters (tone, length)
        
        Returns:
            Dictionary mapping topics to explanations
        """
        results = {}
        for topic in topics:
            print(f"Explaining: {topic}...")
            results[topic] = self.explain(topic, audience, **kwargs)
        return results
    
    def get_history(self):
        """Get conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        print("📝 Conversation history cleared")


# Quick usage functions
def quick_explain(topic: str, audience: str = "beginner", provider: str = "openai"):
    """
    Quick explanation function
    
    Args:
        topic: What to explain
        audience: Who to explain it to
        provider: AI provider to use
    
    Returns:
        Explanation text
    """
    buddy = SmartStudyBuddy(provider=provider)
    return buddy.explain(topic, audience)


def explain_for_child(topic: str, provider: str = "openai"):
    """Explain something to a 5-year-old"""
    return quick_explain(topic, "child", provider)


def explain_for_expert(topic: str, provider: str = "openai"):
    """Explain something to an expert"""
    return quick_explain(topic, "expert", provider)
