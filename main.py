#!/usr/bin/env python3
"""Dataset Augmentation Tool - Author: Pranay M"""
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
from modules import ParaphraseGenerator

console = Console()
aug = ParaphraseGenerator()

def main():
    console.print(Panel("🔄 DATASET AUGMENTATION TOOL 🔄\nExpand Your Training Data", style="bold green"))
    
    while True:
        text = Prompt.ask("Text to augment (or 'quit')")
        if text.lower() == 'quit': break
        label = Prompt.ask("Label (optional)", default="")
        result = aug.augment(text, label)
        console.print(Panel(Markdown(result), title="Augmented Data", border_style="green"))

if __name__ == "__main__": main()
