"""
Smart Study Buddy - Gradio Web Interface
"""

import gradio as gr
from src.study_buddy import SmartStudyBuddy
from src.prompts import AUDIENCE_LEVELS, TONES, LENGTHS


def create_web_interface():
    """Create Gradio web interface"""
    
    # Initialize buddy (will be recreated per request)
    def generate_explanation(topic, audience, tone, length, provider, stream_output):
        """Generate explanation with given parameters"""
        try:
            buddy = SmartStudyBuddy(provider=provider)
            
            # Clean up empty values
            tone = tone if tone != "None" else None
            length = length if length != "None" else None
            
            if stream_output:
                # For streaming, we'll collect and return
                explanation = ""
                for chunk in buddy.explain(topic, audience, tone, length, stream=True):
                    explanation += chunk
                    yield explanation
            else:
                explanation = buddy.explain(topic, audience, tone, length)
                return explanation
                
        except Exception as e:
            return f"❌ Error: {str(e)}\n\nPlease check your API keys in the .env file."
    
    # Create interface
    with gr.Blocks(title="Smart Study Buddy", theme=gr.themes.Soft()) as app:
        gr.Markdown(
            """
            # 🎓 Smart Study Buddy
            ### Adaptive AI Tutor - Explains anything to anyone
            
            Enter a topic and select your audience level. The AI will adapt its explanation to perfectly match your needs.
            """
        )
        
        with gr.Row():
            with gr.Column(scale=2):
                topic_input = gr.Textbox(
                    label="What do you want to learn about?",
                    placeholder="e.g., quantum physics, photosynthesis, blockchain...",
                    lines=2
                )
                
                with gr.Row():
                    audience_dropdown = gr.Dropdown(
                        choices=list(AUDIENCE_LEVELS.keys()),
                        value="beginner",
                        label="Audience Level",
                        info="Who is this explanation for?"
                    )
                    
                    provider_dropdown = gr.Dropdown(
                        choices=["openai", "anthropic"],
                        value="openai",
                        label="AI Provider",
                        info="Which AI to use"
                    )
                
                with gr.Row():
                    tone_dropdown = gr.Dropdown(
                        choices=["None"] + TONES,
                        value="None",
                        label="Tone (Optional)",
                        info="How should it sound?"
                    )
                    
                    length_dropdown = gr.Dropdown(
                        choices=["None"] + LENGTHS,
                        value="None",
                        label="Length (Optional)",
                        info="How detailed?"
                    )
                
                stream_checkbox = gr.Checkbox(
                    label="Stream response (word-by-word)",
                    value=False
                )
                
                explain_btn = gr.Button("✨ Explain", variant="primary", size="lg")
            
            with gr.Column(scale=3):
                output_text = gr.Textbox(
                    label="Explanation",
                    lines=20,
                    show_copy_button=True
                )
        
        # Examples
        gr.Examples(
            examples=[
                ["quantum physics", "child", "playful", "short", "openai"],
                ["how DNA works", "middle_school", "neutral", "medium", "openai"],
                ["machine learning algorithms", "expert", "academic", "detailed", "openai"],
                ["photosynthesis", "high_school", "neutral", "medium", "openai"],
                ["blockchain technology", "beginner", "professional", "medium", "openai"],
            ],
            inputs=[topic_input, audience_dropdown, tone_dropdown, length_dropdown, provider_dropdown],
        )
        
        # Info section
        with gr.Accordion("ℹ️ How to Use", open=False):
            gr.Markdown(
                """
                ### Quick Start
                1. Enter a topic you want to learn about
                2. Select your audience level (from child to expert)
                3. Optionally choose a tone and length
                4. Click "Explain" to get your personalized explanation
                
                ### Audience Levels
                - **child**: Simple explanations for 5-year-olds
                - **elementary**: Ages 6-10
                - **middle_school**: Ages 11-14
                - **high_school**: Ages 15-18
                - **beginner**: Adult with no prior knowledge
                - **intermediate**: Basic background knowledge
                - **advanced**: Substantial background
                - **expert**: Deep expertise in the field
                
                ### Tips
                - Start with your natural audience level
                - Try the same topic at different levels to see how explanations adapt
                - Use "playful" tone for fun, engaging explanations
                - Use "academic" or "professional" for formal contexts
                """
            )
        
        # Connect button to function
        explain_btn.click(
            fn=generate_explanation,
            inputs=[
                topic_input,
                audience_dropdown,
                tone_dropdown,
                length_dropdown,
                provider_dropdown,
                stream_checkbox
            ],
            outputs=output_text
        )
    
    return app


if __name__ == "__main__":
    app = create_web_interface()
    app.launch(share=False, server_name="0.0.0.0", server_port=7860)
