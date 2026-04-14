# scheduler/task_runner.py

# 'concurrent.futures' is Python's built-in tool for doing multiple things at the same time.
import concurrent.futures

# We import the tools we built in Step 5
from tools.mock_apis import MatchAPI, PlayerStatsAPI

class TaskRunner:
    def __init__(self):
        # Give our runner access to the toolbox
        self.tools = {
            "MatchAPI": MatchAPI(),
            "PlayerStatsAPI": PlayerStatsAPI()
        }
        # A dictionary to remember the results of each task
        self.memory = {} 

    def run_single_task(self, task: dict):
        """This function executes exactly ONE task."""
        task_id = task["task_id"]
        tool_name = task.get("tool")
        
        print(f"▶️ Running Task {task_id} using {tool_name}...")

        # If the AI hallucinated a tool that doesn't exist, stop here.
        if tool_name not in self.tools:
            return f"Error: Tool '{tool_name}' not found."

        # Grab the actual tool from our toolbox
        tool = self.tools[tool_name]
        
        try:
            # Tell the tool to do its job
            if tool_name == "MatchAPI":
                result = tool.fetch_data("GAME_101")
            elif tool_name == "PlayerStatsAPI":
                result = tool.fetch_stats("PLAYER_99")
            else:
                result = "Unknown task."
            
            # Save the result in memory for later
            self.memory[task_id] = result
            return result
            
        except Exception as error:
            # If our 20% fake server crash happens, catch it so the app doesn't die!
            return f"Task Failed: {error}"

    def execute_plan_sequentially(self, plan: list, safe_order: list):
        """Runs tasks one-by-one in the safe order from our Graph."""
        print("\n👷 [Scheduler] Starting SEQUENTIAL execution...")
        
        # Create a quick dictionary to find task details by ID
        task_dict = {task["task_id"]: task for task in plan}

        # Loop through our safe map (e.g., [1, 2, 3])
        for task_id in safe_order:
            task = task_dict[task_id]
            result = self.run_single_task(task)
            print(f"✅ Task {task_id} Result: {result}\n")
            
        return self.memory

    def execute_in_parallel(self, tasks: list):
        """Runs multiple independent tasks at the EXACT same time."""
        print("\n⚡ [Scheduler] Starting PARALLEL execution...")
        
        # ThreadPoolExecutor is a beginner-friendly way to spawn multiple "workers"
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # 'map' tells the workers: "Run 'run_single_task' for every item in 'tasks' simultaneously"
            results = list(executor.map(self.run_single_task, tasks))
            
        for task, result in zip(tasks, results):
            print(f"✅ Parallel Task {task['task_id']} Result: {result}")


# Let's test it!
if __name__ == "__main__":
    runner = TaskRunner()
    
    # Dummy plan from our Planner
    dummy_plan = [
        {"task_id": 1, "description": "Fetch match data", "tool": "MatchAPI"},
        {"task_id": 2, "description": "Fetch player performance", "tool": "PlayerStatsAPI"}
    ]
    
    # 1. Test running them one by one
    runner.execute_plan_sequentially(dummy_plan, [1, 2])
    
    # 2. Test running them at the exact same time
    runner.execute_in_parallel(dummy_plan)