import { motion } from 'framer-motion';
import { Sparkles, ArrowRight } from 'lucide-react';
import { useAgentStore } from '../store/useAgentStore';

export default function HeroInput() {
  // Grab what we need from our Zustand brain
  const { goal, setGoal, submitGoal, status } = useAgentStore();
  const isBusy = status === 'thinking';

  const handleSubmit = (e) => {
    e.preventDefault();
    if (goal.trim() && !isBusy) submitGoal(goal);
  };

  return (
    <motion.form 
      onSubmit={handleSubmit}
      initial={{ opacity: 0, y: 20 }} 
      animate={{ opacity: 1, y: 0 }}
      className="w-full max-w-2xl mx-auto mt-20 text-center"
    >
      <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight mb-4 text-slate-800 dark:text-white">
        What should the <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-500 to-cyan-400">Agent</span> build today?
      </h1>
      <p className="text-slate-500 dark:text-slate-400 mb-8 text-lg">
        Enter a high-level goal and watch the AI orchestrate the tasks.
      </p>

      {/* The Premium Input Container */}
      <div className="relative group">
        {/* The Glow Effect (Hidden normally, expands on hover) */}
        <div className="absolute -inset-1 bg-gradient-to-r from-brand-500 to-cyan-400 rounded-2xl blur opacity-25 group-hover:opacity-50 transition duration-1000 group-hover:duration-200"></div>
        
        {/* The Actual Input Box */}
        <div className="relative flex items-center bg-white dark:bg-[#111827] rounded-2xl border border-slate-200 dark:border-white/10 shadow-sm overflow-hidden transition-colors">
          <Sparkles className="ml-4 text-brand-500 shrink-0" size={24} />
          <input
            type="text"
            value={goal}
            onChange={(e) => setGoal(e.target.value)}
            placeholder="e.g., Generate match statistics..."
            disabled={isBusy}
            className="w-full py-4 px-4 bg-transparent outline-none text-lg text-slate-800 dark:text-slate-100 placeholder-slate-400 disabled:opacity-50"
          />
          <button 
            type="submit"
            disabled={!goal.trim() || isBusy}
            className="m-2 px-6 py-2 bg-brand-600 hover:bg-brand-500 text-white font-medium rounded-xl transition-all disabled:opacity-50 flex items-center gap-2 shrink-0"
          >
            {isBusy ? 'Running...' : 'Run'}
            {!isBusy && <ArrowRight size={18} />}
          </button>
        </div>
      </div>
    </motion.form>
  );
}