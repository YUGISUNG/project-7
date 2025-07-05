from memory.memory_engine import MemoryEngine
from tools.file_writer import FileWriter
from tools.summarizer import SummarizerTool
from tools.task_planner import TaskPlanner  # Optional: if implemented
from logs.logger import Logger


class Agent:
    """
    PROJECT-7 Core Agent Class
    """

    def __init__(self, name="PROJECTY-7"):
        self.name = name
        self.memory = MemoryEngine()
        self.logger = Logger()
        self.tools = {
            "file_writer": FileWriter(),
            "summarizer": SummarizerTool(),
            # "task_planner": TaskPlanner()  # Uncomment if task planner is implemented
        }
        self.log = []

    def plan(self, objective: str) -> list:
        return [
            f"tool:file_writer:{objective}",
            "Step 2: Check memory for relevant info",
            f"tool:summarizer:{objective}"
        ]

    def recall(self, query: str):
        return self.memory.search_memory(query)

    def execute(self, step: str) -> str:
        self.log.append(step)

        if step.startswith("tool:"):
            try:
                _, tool_name, tool_input = step.split(":", 2)
                if tool_name in self.tools:
                    if tool_name == "file_writer":
                        result = self.tools[tool_name].write_note(tool_input)
                    elif tool_name == "summarizer":
                        result = self.tools[tool_name].summarize(tool_input)
                    else:
                        result = f"[Tool Error] Tool '{tool_name}' has no defined action"
                    return f"[Tool:{tool_name}] {result}"
                else:
                    return f"[Tool Error] Tool '{tool_name}' not recognized"
            except Exception as e:
                return f"[Tool Error] Failed to execute tool step: {e}"

        return f"[Executed] {step}"

    def run(self, objective: str):
        plan = self.plan(objective)
        results = []

        for step in plan:
            output = self.execute(step)
            print(output)
            results.append(output)

        self.memory.save_memory(objective, results)
        self.logger.save_session(objective, results)
