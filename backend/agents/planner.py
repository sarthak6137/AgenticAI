# agents/planner.py

class SportsPlanner:
    def __init__(self):
        # Eventually, this is where we would set up our AI connection (LangChain)
        self.name = "Sports Brain"

    def create_plan(self, goal: str):
        """
        Takes a goal and returns a list of steps.
        For now, we are simulating what an AI would do.
        """
        print(f"Planning for goal: {goal}")

        # This is a 'Mock' response. 
        # We are pretending the AI thought about it and gave us these steps.
        if "stats" in goal.lower() or "statistics" in goal.lower():
            return [
                {"task_id": 1, "description": "Fetch match data from MatchAPI", "tool": "MatchAPI", "depends_on": []},
                {"task_id": 2, "description": "Fetch player performance", "tool": "PlayerStatsAPI", "depends_on": [1]},
                {"task_id": 3, "description": "Generate summary report", "tool": "ReportTool", "depends_on": [2]}
            ]
        
        # Default plan if we don't recognize the goal
        return [{"task_id": 1, "description": "General lookup", "tool": "SearchAPI", "depends_on": []}]

# This lets us test this specific file by itself
if __name__ == "__main__":
    planner = SportsPlanner()
    plan = planner.create_plan("Generate match statistics")
    print(plan)