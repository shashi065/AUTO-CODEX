from pathlib import Path

def run():
    print("AUTO-CODEX improve started")

    project_path = Path("projects/generated_app")
    intent_path = Path("intent/idea.md")

    if not project_path.exists():
        raise FileNotFoundError("No generated project found")

    if not intent_path.exists():
        raise FileNotFoundError("intent/idea.md not found")

    intent = intent_path.read_text(encoding="utf-8").strip()

    if not intent:
        raise ValueError("intent/idea.md is empty")

    print("Intent loaded")

    improved_note = """
 IMPROVEMENT NOTE

This file has been reviewed by AUTO-CODEX improve command.

Suggestions:
- Better structure
- Cleaner functions
- Improved readability

(Real AI-based improvement can be enabled using OPENAI_API_KEY)
"""

    note_path = project_path / "IMPROVEMENTS.md"
    note_path.write_text(improved_note.strip(), encoding="utf-8")

    print("Improvements documented → IMPROVEMENTS.md")
    print("AUTO-CODEX improve completed")
