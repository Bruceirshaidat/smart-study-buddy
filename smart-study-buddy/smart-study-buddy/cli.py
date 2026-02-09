"""
Smart Study Buddy - Command Line Interface
"""

import typer
from typing import Optional
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from src.study_buddy import SmartStudyBuddy
from src.prompts import AUDIENCE_LEVELS, TONES, LENGTHS

app = typer.Typer(help="🎓 Smart Study Buddy - Adaptive AI Tutor")
console = Console()


@app.command()
def explain(
    topic: str = typer.Argument(..., help="Topic to explain"),
    audience: str = typer.Option("beginner", "--audience", "-a", help="Audience level"),
    tone: Optional[str] = typer.Option(None, "--tone", "-t", help="Tone (playful/neutral/academic/professional)"),
    length: Optional[str] = typer.Option(None, "--length", "-l", help="Length (short/medium/detailed)"),
    provider: str = typer.Option("openai", "--provider", "-p", help="AI provider (openai/anthropic)"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Specific model to use"),
    stream: bool = typer.Option(False, "--stream", "-s", help="Stream the response"),
):
    """
    Explain a topic to a specific audience
    
    Example:
        python cli.py explain "quantum physics" --audience expert --tone academic
    """
    console.print(f"\n[bold cyan]🎓 Smart Study Buddy[/bold cyan]")
    console.print(f"[dim]Topic:[/dim] {topic}")
    console.print(f"[dim]Audience:[/dim] {audience}")
    if tone:
        console.print(f"[dim]Tone:[/dim] {tone}")
    if length:
        console.print(f"[dim]Length:[/dim] {length}")
    console.print()
    
    try:
        buddy = SmartStudyBuddy(provider=provider, model=model)
        
        if stream:
            console.print("[bold green]Generating explanation (streaming)...[/bold green]\n")
            for chunk in buddy.explain(topic, audience, tone, length, stream=True):
                console.print(chunk, end="")
            console.print("\n")
        else:
            with console.status("[bold green]Generating explanation..."):
                explanation = buddy.explain(topic, audience, tone, length)
            
            console.print(Panel(
                Markdown(explanation),
                title=f"Explanation for {audience}",
                border_style="green"
            ))
    
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        raise typer.Exit(1)


@app.command()
def interactive(
    provider: str = typer.Option("openai", "--provider", "-p", help="AI provider"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Specific model"),
):
    """
    Start interactive mode with prompts
    """
    console.print("[bold cyan]🎓 Smart Study Buddy - Interactive Mode[/bold cyan]\n")
    
    try:
        buddy = SmartStudyBuddy(provider=provider, model=model)
        
        # Get topic
        topic = typer.prompt("What topic would you like explained?")
        
        # Show audience options
        console.print("\n[bold]Available audience levels:[/bold]")
        for key, desc in AUDIENCE_LEVELS.items():
            console.print(f"  • [cyan]{key}[/cyan]: {desc}")
        
        audience = typer.prompt("\nSelect audience level", default="beginner")
        
        # Optional preferences
        tone = typer.prompt("Tone (playful/neutral/academic/professional)", default="", show_default=False)
        length = typer.prompt("Length (short/medium/detailed)", default="", show_default=False)
        
        console.print()
        
        with console.status("[bold green]Generating explanation..."):
            explanation = buddy.explain(
                topic,
                audience,
                tone if tone else None,
                length if length else None
            )
        
        console.print(Panel(
            Markdown(explanation),
            title=f"Explanation: {topic}",
            border_style="green"
        ))
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        raise typer.Exit(1)


@app.command()
def batch(
    topics: str = typer.Argument(..., help="Comma-separated topics"),
    audience: str = typer.Option("beginner", "--audience", "-a", help="Audience level"),
    provider: str = typer.Option("openai", "--provider", "-p", help="AI provider"),
):
    """
    Explain multiple topics for the same audience
    
    Example:
        python cli.py batch "gravity,photosynthesis,DNA" --audience middle_school
    """
    topic_list = [t.strip() for t in topics.split(",")]
    
    console.print(f"\n[bold cyan]🎓 Batch Explanation Mode[/bold cyan]")
    console.print(f"[dim]Topics:[/dim] {len(topic_list)}")
    console.print(f"[dim]Audience:[/dim] {audience}\n")
    
    try:
        buddy = SmartStudyBuddy(provider=provider)
        
        for i, topic in enumerate(topic_list, 1):
            console.print(f"[bold yellow]{i}/{len(topic_list)}[/bold yellow] {topic}")
            
            with console.status(f"[bold green]Generating..."):
                explanation = buddy.explain(topic, audience)
            
            console.print(Panel(
                Markdown(explanation),
                title=topic,
                border_style="green"
            ))
            console.print()
    
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        raise typer.Exit(1)


@app.command()
def list_options():
    """Show available audiences, tones, and lengths"""
    console.print("\n[bold cyan]📚 Available Options[/bold cyan]\n")
    
    console.print("[bold]Audience Levels:[/bold]")
    for key, desc in AUDIENCE_LEVELS.items():
        console.print(f"  • [cyan]{key}[/cyan]: {desc}")
    
    console.print("\n[bold]Tones:[/bold]")
    for tone in TONES:
        console.print(f"  • [cyan]{tone}[/cyan]")
    
    console.print("\n[bold]Lengths:[/bold]")
    for length in LENGTHS:
        console.print(f"  • [cyan]{length}[/cyan]")
    
    console.print()


if __name__ == "__main__":
    app()
