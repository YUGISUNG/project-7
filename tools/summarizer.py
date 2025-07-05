import re

class SummarizerTool:
    """
    Tool that summarizes input text.
    """

    def summarize(self, text: str) -> str:
        # Remove leading "Summarize this:" prefix
        cleaned = re.sub(r"(?i)^summarize this:\s*", "", text.strip())

        # Split into sentences
        sentences = re.split(r'(?<=[.!?])\s+', cleaned)

        if len(sentences) <= 2:
            return f"Summary: {cleaned}"

        return f"Summary: {sentences[0]} ... {sentences[-1]}"


