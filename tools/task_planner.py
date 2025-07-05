from datetime import datetime, timedelta

class TaskPlanner:
    """
    Generates a 7-day task breakdown from a high-level weekly objective.
    """

    def plan_tasks(self, objective: str) -> list:
        today = datetime.now()
        tasks = []

        for i in range(7):
            day = today + timedelta(days=i)
            task = f"Day {i+1} ({day.strftime('%A')}): Work on '{objective}'"
            tasks.append(task)

        return tasks
