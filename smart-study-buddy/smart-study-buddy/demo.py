#!/usr/bin/env python3
"""
Smart Study Buddy - Interactive Demo
Showcase all features with beautiful output
"""

import time
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import track
from rich.table import Table
from src.study_buddy import SmartStudyBuddy

console = Console()


def print_header():
    """Print demo header"""
    console.print("\n" + "=" * 70)
    console.print("[bold magenta]🎓 SMART STUDY BUDDY - INTERACTIVE DEMO[/bold magenta]".center(70))
    console.print("=" * 70 + "\n")


def demo_1_basic():
    """Demo 1: Basic usage"""
    console.print("\n[bold cyan]📚 Demo 1: Basic Explanation[/bold cyan]\n")
    
    buddy = SmartStudyBuddy()
    
    console.print("[dim]Explaining 'photosynthesis' to a middle school student...[/dim]\n")
    time.sleep(1)
    
    explanation = buddy.explain("photosynthesis", "middle_school")
    
    console.print(Panel(
        Markdown(explanation),
        title="🌱 Photosynthesis (Middle School)",
        border_style="green"
    ))


def demo_2_adaptation():
    """Demo 2: Audience adaptation"""
    console.print("\n[bold cyan]🎯 Demo 2: Audience Adaptation[/bold cyan]\n")
    console.print("[dim]Same topic, different audiences...[/dim]\n")
    
    buddy = SmartStudyBuddy()
    topic = "black holes"
    
    audiences = {
        "child": "5-year-old",
        "high_school": "High School",
        "expert": "Expert"
    }
    
    for level, label in track(audiences.items(), description="Generating..."):
        time.sleep(0.5)
        explanation = buddy.explain(topic, level, length="short")
        
        console.print(Panel(
            Markdown(explanation),
            title=f"🌌 Black Holes for {label}",
            border_style="blue"
        ))
        console.print()


def demo_3_tones():
    """Demo 3: Different tones"""
    console.print("\n[bold cyan]🎨 Demo 3: Tone Variations[/bold cyan]\n")
    console.print("[dim]Same topic with different tones...[/dim]\n")
    
    buddy = SmartStudyBuddy()
    topic = "machine learning"
    
    tones_dict = {
        "playful": "🎪",
        "academic": "🎓",
        "professional": "💼"
    }
    
    for tone, emoji in tones_dict.items():
        console.print(f"[yellow]Generating {tone} explanation...[/yellow]")
        explanation = buddy.explain(topic, "beginner", tone=tone, length="short")
        
        console.print(Panel(
            Markdown(explanation),
            title=f"{emoji} {tone.title()} Tone",
            border_style="yellow"
        ))
        console.print()


def demo_4_comparison_table():
    """Demo 4: Comparison table"""
    console.print("\n[bold cyan]📊 Demo 4: Audience Comparison[/bold cyan]\n")
    
    buddy = SmartStudyBuddy()
    topic = "DNA"
    
    table = Table(title=f"How '{topic}' is explained to different audiences")
    table.add_column("Audience", style="cyan")
    table.add_column("Key Concept", style="green")
    
    audiences = ["child", "middle_school", "expert"]
    
    for audience in track(audiences, description="Generating comparisons..."):
        explanation = buddy.explain(topic, audience, length="short")
        # Extract first sentence as key concept
        first_sentence = explanation.split('.')[0] + '.'
        table.add_row(audience.replace('_', ' ').title(), first_sentence)
    
    console.print(table)


def demo_5_streaming():
    """Demo 5: Streaming response"""
    console.print("\n[bold cyan]⚡ Demo 5: Streaming Response[/bold cyan]\n")
    console.print("[dim]Watching explanation generate in real-time...[/dim]\n")
    
    buddy = SmartStudyBuddy()
    
    console.print("[bold green]🌊 How Waves Work (Streaming)[/bold green]\n")
    
    for chunk in buddy.explain("how ocean waves work", "elementary", stream=True):
        console.print(chunk, end="")
        time.sleep(0.02)  # Slow down for effect
    
    console.print("\n")


def interactive_menu():
    """Interactive menu"""
    console.print("\n[bold cyan]🎮 Interactive Mode[/bold cyan]\n")
    
    buddy = SmartStudyBuddy()
    
    topic = console.input("[yellow]What topic interests you? [/yellow]")
    
    # Show audience options
    table = Table(title="Available Audiences", show_header=False)
    table.add_column("Number", style="cyan")
    table.add_column("Audience", style="green")
    
    audiences = ["child", "elementary", "middle_school", "high_school", 
                 "beginner", "intermediate", "advanced", "expert"]
    
    for i, aud in enumerate(audiences, 1):
        table.add_row(str(i), aud.replace('_', ' ').title())
    
    console.print(table)
    
    choice = console.input("\n[yellow]Select audience (1-8): [/yellow]")
    try:
        audience = audiences[int(choice) - 1]
    except:
        audience = "beginner"
    
    console.print(f"\n[dim]Generating explanation for {audience}...[/dim]\n")
    
    explanation = buddy.explain(topic, audience)
    
    console.print(Panel(
        Markdown(explanation),
        title=f"📚 {topic.title()}",
        border_style="green"
    ))


def main():
    """Run full demo"""
    print_header()
    
    console.print("[bold]Choose a demo:[/bold]\n")
    console.print("1. Basic Explanation")
    console.print("2. Audience Adaptation (same topic, different levels)")
    console.print("3. Tone Variations")
    console.print("4. Comparison Table")
    console.print("5. Streaming Response")
    console.print("6. Interactive Mode (your own topic)")
    console.print("7. Run All Demos")
    console.print("0. Exit\n")
    
    choice = console.input("[yellow]Select (0-7): [/yellow]")
    
    demos = {
        "1": demo_1_basic,
        "2": demo_2_adaptation,
        "3": demo_3_tones,
        "4": demo_4_comparison_table,
        "5": demo_5_streaming,
        "6": interactive_menu,
    }
    
    if choice == "7":
        for demo_func in demos.values():
            demo_func()
            console.input("\n[dim]Press Enter to continue...[/dim]")
    elif choice in demos:
        demos[choice]()
    elif choice == "0":
        console.print("\n[green]Thanks for trying Smart Study Buddy! 🎓[/green]\n")
        return
    else:
        console.print("\n[red]Invalid choice[/red]")
        return
    
    console.print("\n[bold green]✨ Demo Complete![/bold green]")
    console.print("\n[dim]Try: python cli.py --help for more options[/dim]\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Demo interrupted. Goodbye! 👋[/yellow]\n")
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]\n")
        console.print("[dim]Make sure your .env file has valid API keys[/dim]\n")
