# 🧠 PROJECTY-7: Strategic AI Agent System

PROJECTY-7 is an evolving, modular AI assistant built for planning, memory, tool integration, and agentic reasoning — designed with a **faith-first** mindset to reflect God’s wisdom, enable human flourishing, and serve with excellence.

---

## ✨ Core Principles

- 🧠 **Agentic Intelligence**: Modular architecture with reasoning and self-evolving task flows  
- 🙋 **Human-in-the-Loop**: All actions approved by JP before execution  
- 🧠 **Memory + Tools**: Learns from prior tasks, and calls plugins like a real AI assistant  
- ✝️ **Faith-Guided**: Grounded in biblical principles and humility  
- 🧬 **XP System**: Gamified development with level-ups toward S-Rank performance  

---

## 🧩 Features

| Ability            | Description                                              |
|--------------------|----------------------------------------------------------|
| 🧠 Memory Engine    | Logs every session + task to a searchable JSON file      |
| 🛠️ Tool Execution   | Dynamically routes actions like saving files or summaries |
| 📚 Recall           | Find past missions using keyword search                  |
| 🧾 Logger           | Saves each session to a `.txt` file in `/logs/`          |
| 🔁 Modular Tools    | Easily add custom tools like LLM, planners, APIs         |

---

## 📂 Current Modules

| Module           | Description                                     |
|------------------|-------------------------------------------------|
| `agent_core/`     | Strategic logic and mission execution           |
| `memory/`         | Context handling and task recall (JSON-based)   |
| `tools/`          | File operations, summarizer, planner plugins    |
| `interface/`      | CLI or UI for future control                    |
| `logs/`           | Dev journal and output session logs             |
| `tests/`          | Unit tests and future validation suite          |

---

## 💻 Live Example

```bash
$ python run_agent.py
🧠 PROJECTY-7 Activated
Enter your objective: Build a weekly system for rest + work.

🤖 Planning and Executing...

[Tool:file_writer] Saved to data/note_*.txt
[Executed] Step 2: Check memory for relevant info
[Tool:summarizer] Summary: Build a weekly system for rest + work.
```

```bash
Enter a keyword to recall from memory: weekly
📚 Memory Results: 2 matching logs
```

---


## 🚀 Getting Started

```bash
# Clone and enter project
cd PROJECTY-7

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate     # (Windows)

# Install dependencies
pip install -r requirements.txt
```

---

## 📜 License

MIT License © 2025 YUGISUNG  
See [LICENSE](LICENSE) for details.

---

## 🙌 Contributing

Pull requests welcome — especially for:
- New tools (planners, LLMs, agents)
- UX or front-end wrappers
- Optimization or testing

Let everything we build reflect wisdom, excellence, and truth.

