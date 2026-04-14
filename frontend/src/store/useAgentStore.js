import { create } from 'zustand';
import axios from 'axios';

export const useAgentStore = create((set) => ({
  // 1. Our Variables (State)
  goal: '',
  status: 'idle', // Can be: 'idle', 'thinking', 'complete', 'error'
  thinkingPhase: '', // Text to show while waiting (e.g., "Planning...")
  result: null, // The final JSON from the backend
  errorMessage: '',

  // 2. Simple function to update what the user types
  setGoal: (goal) => set({ goal }),

  // 3. The main function that talks to your Python backend
  submitGoal: async (goalText) => {
    // Reset the UI to a loading state
    set({ status: 'thinking', thinkingPhase: 'Planning steps...', result: null, errorMessage: '' });

    // UX TRICK: We cycle through fake "thinking" phases to make the UI feel alive
    const phaseTimer1 = setTimeout(() => set({ thinkingPhase: 'Building dependency graph...' }), 1500);
    const phaseTimer2 = setTimeout(() => set({ thinkingPhase: 'Executing tools...' }), 3000);

    try {
      // Send the POST request to our FastAPI backend
      const response = await axios.post('http://127.0.0.1:8000/plan', { goal: goalText });

      // If backend finishes fast, clear the fake UI timers
      clearTimeout(phaseTimer1);
      clearTimeout(phaseTimer2);

      // Save the result and mark as complete
      set({ status: 'complete', result: response.data });
      
    } catch (error) {
      clearTimeout(phaseTimer1);
      clearTimeout(phaseTimer2);
      set({ status: 'error', errorMessage: 'Backend connection failed. Is your Python server running?' });
    }
  },

  // 4. Reset button function
  reset: () => set({ status: 'idle', result: null, goal: '', thinkingPhase: '' })
}));