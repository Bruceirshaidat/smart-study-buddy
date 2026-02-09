"""
Smart Study Buddy - Tests
"""

import pytest
import os
from src.study_buddy import SmartStudyBuddy
from src.prompts import create_user_prompt, AUDIENCE_LEVELS


def test_audience_levels():
    """Test that all audience levels are defined"""
    assert len(AUDIENCE_LEVELS) == 8
    assert "child" in AUDIENCE_LEVELS
    assert "expert" in AUDIENCE_LEVELS


def test_create_user_prompt():
    """Test user prompt creation"""
    prompt = create_user_prompt(
        topic="photosynthesis",
        audience="middle_school",
        tone="neutral",
        length="medium"
    )
    
    assert "photosynthesis" in prompt
    assert "middle_school" in prompt
    assert "neutral" in prompt
    assert "medium" in prompt


def test_create_user_prompt_minimal():
    """Test user prompt with minimal parameters"""
    prompt = create_user_prompt(
        topic="gravity",
        audience="beginner"
    )
    
    assert "gravity" in prompt
    assert "beginner" in prompt


@pytest.mark.skipif(
    not os.getenv("OPENAI_API_KEY"),
    reason="OpenAI API key not found"
)
def test_smart_study_buddy_initialization():
    """Test SmartStudyBuddy initialization"""
    buddy = SmartStudyBuddy(provider="openai")
    assert buddy.client is not None
    assert buddy.system_prompt is not None


@pytest.mark.skipif(
    not os.getenv("OPENAI_API_KEY"),
    reason="OpenAI API key not found"
)
def test_explain_basic():
    """Test basic explanation generation"""
    buddy = SmartStudyBuddy(provider="openai")
    explanation = buddy.explain("gravity", "child")
    
    assert isinstance(explanation, str)
    assert len(explanation) > 50  # Should be substantial


@pytest.mark.skipif(
    not os.getenv("OPENAI_API_KEY"),
    reason="OpenAI API key not found"
)
def test_explain_with_options():
    """Test explanation with all options"""
    buddy = SmartStudyBuddy(provider="openai")
    explanation = buddy.explain(
        topic="photosynthesis",
        audience="high_school",
        tone="academic",
        length="short"
    )
    
    assert isinstance(explanation, str)
    assert len(explanation) > 50


def test_conversation_history():
    """Test conversation history tracking"""
    buddy = SmartStudyBuddy(provider="openai")
    
    # Initially empty
    assert len(buddy.get_history()) == 0
    
    # Add to history (mock, don't actually call API)
    buddy.conversation_history.append({
        "topic": "test",
        "audience": "beginner"
    })
    
    assert len(buddy.get_history()) == 1
    
    # Clear history
    buddy.clear_history()
    assert len(buddy.get_history()) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
