# pipeline.py

# We import all the pieces we built in Steps 4, 6, and 7
from agents.planner import SportsPlanner
from scheduler.graph import TaskGraph
from scheduler.task_runner import TaskRunner

class AgentPipeline:
    def __init__(self):
        # We set up our team of workers once when the pipeline starts
        self.planner = SportsPlanner()
        self.graph = TaskGraph()
        self.runner = TaskRunner()

    def run(self, goal: str):
        print(f"🚀 [Pipeline] Starting mission: '{goal}'\n")

        # Step 1: Ask the Brain for a plan
        plan = self.planner.create_plan(goal)

        # Step 2: Ask the Map for a safe route
        # (We create a fresh map every time so old tasks don't get stuck in it)
        self.graph = TaskGraph() 
        self.graph.build_graph(plan)
        safe_order = self.graph.get_execution_order()

        # Check if the map found an impossible loop
        if not safe_order:
            return {"status": "error", "message": "Could not determine safe execution order."}

        # Step 3: Tell the Foreman to execute the plan using the safe route
        results = self.runner.execute_plan_sequentially(plan, safe_order)

        print("\n🎉 [Pipeline] Mission Complete!")
        
        # Return the final dictionary of all task results
        return {
            "status": "success",
            "goal": goal,
            "data": results
        }

# Let's test the entire system with one single command!
if __name__ == "__main__":
    # Create our pipeline manager
    manager = AgentPipeline()
    
    # Give it our goal
    final_output = manager.run("Generate match statistics")
    
    # Print the final combined data
    print(f"\nFinal Combined Output:\n{final_output}")