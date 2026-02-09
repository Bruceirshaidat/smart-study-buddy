"""
Smart Study Buddy - Example Usage
Run this script to see Smart Study Buddy in action!
"""

from src.study_buddy import SmartStudyBuddy
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()


def print_example(title, explanation):
    """Pretty print an example"""
    console.print(f"\n[bold cyan]{title}[/bold cyan]")
    console.print(Panel(Markdown(explanation), border_style="green"))


def main():
    console.print("\n[bold magenta]🎓 Smart Study Buddy - Examples[/bold magenta]\n")
    
    # Initialize
    console.print("[dim]Initializing AI client...[/dim]")
    buddy = SmartStudyBuddy(provider="openai")
    
    # Example 1: Child
    console.print("\n[bold yellow]Example 1: Explaining to a 5-year-old[/bold yellow]")
    explanation = buddy.explain(
        topic="how airplanes fly",
        audience="child",
        tone="playful"
    )
    print_example("How Airplanes Fly (for a child)", explanation)
    
    # Example 2: Middle School
    console.print("\n[bold yellow]Example 2: Middle School Level[/bold yellow]")
    explanation = buddy.explain(
        topic="photosynthesis",
        audience="middle_school",
        length="medium"
    )
    print_example("Photosynthesis (for middle school)", explanation)
    
    # Example 3: Expert
    console.print("\n[bold yellow]Example 3: Expert Level[/bold yellow]")
    explanation = buddy.explain(
        topic="quantum entanglement",
        audience="expert",
        tone="academic",
        length="detailed"
    )
    print_example("Quantum Entanglement (for experts)", explanation)
    
    # Example 4: Comparison
    console.print("\n[bold yellow]Example 4: Same Topic, Different Audiences[/bold yellow]")
    topic = "blockchain"
    
    for audience in ["beginner", "intermediate", "expert"]:
        explanation = buddy.explain(topic, audience, length="short")
        print_example(f"Blockchain (for {audience})", explanation)
    
    console.print("\n[bold green]✨ Examples complete![/bold green]\n")


if __name__ == "__main__":
    main()
