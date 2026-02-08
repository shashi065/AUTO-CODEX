AUTO-CODEX

AUTO-CODEX is a CLI-based multi-language code generator that converts a simple idea into working code using MOCK mode or AI-powered generation.

---

Features

- CLI tool (`autocodex`)
- Intent-based code generation
- Multi-language support (Python, JavaScript, C, Java)
- MOCK mode (no API key required)
- AI mode (OpenAI)
- Automatic README generation
- GitHub Actions ready
- Pip-installable

---

Installation

### Development (editable)
```bash
pip install -e .
````

After publish

```bash
pip install autocodex
```

---

Usage

Initialize project

```bash
autocodex init
```

Creates:

```
intent/idea.md
```

Write your idea inside `idea.md`.

---

Generate code (default: Python)

```bash
autocodex generate
```

---

Multi-Language Generation

```bash
autocodex generate python
autocodex generate javascript
autocodex generate c
autocodex generate java
```

Generated files:

* Python → `app.py`
* JavaScript → `index.js`
* C → `main.c`
* Java → `Main.java`

---

MOCK MODE

MOCK mode runs by default (no API used).

Force MOCK mode:

```bash
set MOCK_MODE=true
```

---

AI MODE

Set OpenAI key:

Windows

```bat
set OPENAI_API_KEY=your_api_key_here
```

Linux / macOS

```bash
export OPENAI_API_KEY=your_api_key_here
```

Then:

```bash
autocodex generate python
```

---

Project Structure

```
AUTO-CODEX/
├── codex_engine/
│   ├── cli.py
│   ├── generate.py
│   ├── init.py
│   └── improve.py
├── intent/
│   └── idea.md
├── projects/
│   └── generated_app/
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

GitHub Actions

```bash
pip install -e .
autocodex generate
```
---
Author
Varkala Shashidhar
GitHub: [https://github.com/shashi065](https://github.com/shashi065)

---
License
MIT License

```
---

That’s it.  
Paste → save → commit → push 
```
