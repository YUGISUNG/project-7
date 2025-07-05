import os
from datetime import datetime

class FileWriter:
    """
    A simple tool that writes text to a timestamped file in the /data folder.
    """

    def __init__(self, output_dir="data"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def write_note(self, text: str) -> str:
        """
        Saves the given text as a .txt file with a timestamped filename.

        Args:
            text (str): Content to save.

        Returns:
            str: Full path to the saved file.
        """
        filename = f"note_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, "w") as f:
            f.write(text)

        return filepath
