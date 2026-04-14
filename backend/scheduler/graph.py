# scheduler/graph.py
import networkx as nx

class TaskGraph:
    def __init__(self):
        # DiGraph stands for "Directed Graph" (our one-way street map)
        self.graph = nx.DiGraph()

    def build_graph(self, plan: list):
        """
        Takes the list of tasks from our Planner and builds the map.
        """
        print("🗺️  [Graph] Building task dependency map...")
        
        for task in plan:
            task_id = task["task_id"]
            
            # Step A: Add the task as a "Dot" (Node) on our map
            self.graph.add_node(task_id, info=task)
            
            # Step B: Draw the "Arrows" (Edges) based on dependencies
            for dependency_id in task["depends_on"]:
                # Draw an arrow FROM the dependency TO the current task
                self.graph.add_edge(dependency_id, task_id)

    def get_execution_order(self):
        """
        Reads the map and gives us the exact order to run tasks safely.
        This prevents a task from running before its prerequisites are done.
        """
        try:
            # 'topological_sort' is the math term for "put them in the right order"
            order = list(nx.topological_sort(self.graph))
            return order
        except nx.NetworkXUnfeasible:
            # This happens if there is an impossible loop!
            print("🚨 ERROR: Circular dependency detected! Infinite loop prevented.")
            return []

# Let's test it with the exact dummy data our Planner made in Step 4
if __name__ == "__main__":
    dummy_plan = [
        {"task_id": 1, "description": "Fetch match data", "depends_on": []},
        {"task_id": 2, "description": "Fetch player performance", "depends_on": [1]},
        {"task_id": 3, "description": "Generate summary report", "depends_on": [2]}
    ]

    # Create our graph tool
    task_map = TaskGraph()
    
    # Build the map
    task_map.build_graph(dummy_plan)
    
    # Get the safe order
    safe_order = task_map.get_execution_order()
    
    print(f"✅ Safe order to execute tasks: {safe_order}")