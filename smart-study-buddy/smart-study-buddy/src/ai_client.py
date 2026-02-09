"""
Smart Study Buddy - AI Client
Supports both OpenAI and Anthropic APIs
"""

import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class AIClient:
    """Unified client for OpenAI and Anthropic APIs"""
    
    def __init__(self, provider: str = "openai", model: str = None):
        """
        Initialize AI client
        
        Args:
            provider: "openai" or "anthropic"
            model: Model name (optional, uses env default)
        """
        self.provider = provider.lower()
        self.model = model or os.getenv("DEFAULT_MODEL", "gpt-4o")
        self.max_tokens = int(os.getenv("MAX_TOKENS", "2000"))
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))
        
        if self.provider == "openai":
            self._init_openai()
        elif self.provider == "anthropic":
            self._init_anthropic()
        else:
            raise ValueError(f"Unsupported provider: {provider}")
    
    def _init_openai(self):
        """Initialize OpenAI client"""
        try:
            from openai import OpenAI
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY not found in environment")
            self.client = OpenAI(api_key=api_key)
            print(f"✅ OpenAI client initialized with model: {self.model}")
        except ImportError:
            raise ImportError("OpenAI package not installed. Run: pip install openai")
    
    def _init_anthropic(self):
        """Initialize Anthropic client"""
        try:
            from anthropic import Anthropic
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                raise ValueError("ANTHROPIC_API_KEY not found in environment")
            self.client = Anthropic(api_key=api_key)
            print(f"✅ Anthropic client initialized with model: {self.model}")
        except ImportError:
            raise ImportError("Anthropic package not installed. Run: pip install anthropic")
    
    def generate_explanation(
        self,
        system_prompt: str,
        user_prompt: str,
        **kwargs
    ) -> str:
        """
        Generate explanation using the configured AI provider
        
        Args:
            system_prompt: System instructions
            user_prompt: User query
            **kwargs: Additional parameters
        
        Returns:
            Generated explanation text
        """
        if self.provider == "openai":
            return self._generate_openai(system_prompt, user_prompt, **kwargs)
        elif self.provider == "anthropic":
            return self._generate_anthropic(system_prompt, user_prompt, **kwargs)
    
    def _generate_openai(self, system_prompt: str, user_prompt: str, **kwargs) -> str:
        """Generate using OpenAI API"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=kwargs.get("max_tokens", self.max_tokens),
                temperature=kwargs.get("temperature", self.temperature)
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
    
    def _generate_anthropic(self, system_prompt: str, user_prompt: str, **kwargs) -> str:
        """Generate using Anthropic API"""
        try:
            response = self.client.messages.create(
                model=self.model,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=kwargs.get("max_tokens", self.max_tokens),
                temperature=kwargs.get("temperature", self.temperature)
            )
            return response.content[0].text
        except Exception as e:
            raise Exception(f"Anthropic API error: {str(e)}")
    
    def stream_explanation(
        self,
        system_prompt: str,
        user_prompt: str,
        **kwargs
    ):
        """
        Stream explanation (yields chunks)
        
        Args:
            system_prompt: System instructions
            user_prompt: User query
            **kwargs: Additional parameters
        
        Yields:
            Text chunks
        """
        if self.provider == "openai":
            yield from self._stream_openai(system_prompt, user_prompt, **kwargs)
        elif self.provider == "anthropic":
            yield from self._stream_anthropic(system_prompt, user_prompt, **kwargs)
    
    def _stream_openai(self, system_prompt: str, user_prompt: str, **kwargs):
        """Stream using OpenAI API"""
        try:
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=kwargs.get("max_tokens", self.max_tokens),
                temperature=kwargs.get("temperature", self.temperature),
                stream=True
            )
            
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            raise Exception(f"OpenAI streaming error: {str(e)}")
    
    def _stream_anthropic(self, system_prompt: str, user_prompt: str, **kwargs):
        """Stream using Anthropic API"""
        try:
            with self.client.messages.stream(
                model=self.model,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=kwargs.get("max_tokens", self.max_tokens),
                temperature=kwargs.get("temperature", self.temperature)
            ) as stream:
                for text in stream.text_stream:
                    yield text
        except Exception as e:
            raise Exception(f"Anthropic streaming error: {str(e)}")
