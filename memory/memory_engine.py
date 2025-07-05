import json
import os
from datetime import datetime

class MemoryEngine:
    """
    PROJECT-7 Memory Engine

    Stores and retrieves agent memories using a local JSON file.
    """

    def __init__(self, memory_file="memory/memory_log.json"):
        self.memory_file = memory_file
        self._ensure_memory_file()

    def _ensure_memory_file(self):
        """Create the memory file if it doesn't exist."""
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w") as f:
                json.dump([], f)

    def save_memory(self, objective: str, results: list):
        """Save a new memory entry to file."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "objective": objective,
            "results": results
        }

        with open(self.memory_file, "r+") as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=2)

    def search_memory(self, keyword: str):
        """Return all memories containing the keyword."""
        with open(self.memory_file, "r") as f:
            data = json.load(f)

        matches = [
            entry for entry in data
            if keyword.lower() in entry["objective"].lower()
            or any(keyword.lower() in step.lower() for step in entry["results"])
        ]

        return matches if matches else ["No matching memory found."]
