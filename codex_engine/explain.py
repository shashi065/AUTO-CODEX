from pathlib import Path


def generate_readme(project_path: Path):
    """
    Auto-generate or update README.md for the generated project
    """

    readme_path = project_path / "README.md"

    content = f"""# Generated Application

This project was generated using **AUTO-CODEX**.

---

Description

This application was automatically created based on the intent provided
inside the `intent/idea.md` file.

---

Files

"""

    for file in project_path.iterdir():
        if file.is_file():
            content += f"- `{file.name}`\n"

    content += """
---

 How to Run

### Python
```bash
python app.py
