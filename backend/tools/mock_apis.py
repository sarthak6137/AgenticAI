# tools/mock_apis.py
import time
import random

class MatchAPI:
    def fetch_data(self, match_id: str):
        print(f"🌍 [MatchAPI] Searching for match {match_id}...")
        
        # Simulate the time it takes for data to travel across the internet
        time.sleep(1) 
        
        # Return fake JSON data
        return {"match_id": match_id, "score": "2-1", "status": "Finished"}


class PlayerStatsAPI:
    def fetch_stats(self, player_id: str):
        print(f"🌍 [PlayerStatsAPI] Loading stats for player {player_id}...")
        time.sleep(1.5)
        
        # Simulate a random server failure (20% chance to fail)
        # In the real world, APIs crash! Our system will need to handle this later.
        if random.random() < 0.2:
            raise Exception("ERROR: PlayerStatsAPI server is down!")
            
        return {"player_id": player_id, "goals": 1, "assists": 2, "rating": 8.5}


class EventStreamAPI:
    def get_latest_event(self):
        print("🌍 [EventStreamAPI] Connecting to live stadium feed...")
        time.sleep(0.5)
        return {"event": "Goal!", "minute": 89, "player": "Messi"}

# Testing our tools locally
if __name__ == "__main__":
    # Create the tools
    match_tool = MatchAPI()
    player_tool = PlayerStatsAPI()
    
    # Test them
    print(match_tool.fetch_data("GAME_101"))
    
    try:
        print(player_tool.fetch_stats("PLAYER_99"))
    except Exception as error:
        print(error) # This prints the fake crash message if we hit that 20% chance!