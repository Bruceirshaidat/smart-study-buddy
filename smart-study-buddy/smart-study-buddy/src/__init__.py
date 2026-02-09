"""
Smart Study Buddy - Main Package
"""

from .study_buddy import SmartStudyBuddy, quick_explain, explain_for_child, explain_for_expert
from .ai_client import AIClient
from .prompts import SYSTEM_PROMPT, AUDIENCE_LEVELS, TONES, LENGTHS

__version__ = "1.0.0"
__all__ = [
    "SmartStudyBuddy",
    "AIClient",
    "quick_explain",
    "explain_for_child",
    "explain_for_expert",
    "SYSTEM_PROMPT",
    "AUDIENCE_LEVELS",
    "TONES",
    "LENGTHS",
]
