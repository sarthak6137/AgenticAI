import { motion } from 'framer-motion';
import { CheckCircle2, Circle, Loader2 } from 'lucide-react';

export default function TaskCard({ title, status, index }) {
  const isRunning = status === 'running';
  const isDone = status === 'done';

  return (
    <motion.div
      // The 'index * 0.15' creates a beautiful staggered entrance effect!
      initial={{ opacity: 0, x: -20 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ delay: index * 0.15 }}
      className={`p-4 rounded-xl border flex items-center gap-4 transition-all duration-500 ${
        isDone 
          ? 'bg-emerald-50 dark:bg-emerald-900/10 border-emerald-200 dark:border-emerald-800' 
          : isRunning 
          ? 'bg-brand-50 dark:bg-brand-900/10 border-brand-200 dark:border-brand-800 shadow-[0_0_15px_rgba(59,130,246,0.15)]'
          : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-white/5 opacity-60'
      }`}
    >
      {/* Icon Area */}
      <div className="shrink-0">
        {isDone && <CheckCircle2 className="text-emerald-500" />}
        {isRunning && <Loader2 className="text-brand-500 animate-spin" />}
        {!isDone && !isRunning && <Circle className="text-slate-400" />}
      </div>
      
      {/* Text Area */}
      <div className="flex-1">
        <h4 className={`font-medium ${isDone ? 'text-emerald-800 dark:text-emerald-400' : 'text-slate-800 dark:text-slate-200'}`}>
          {title}
        </h4>
        <p className="text-sm text-slate-500 dark:text-slate-400">
          {isDone ? 'Execution completed successfully' : isRunning ? 'Processing tool data...' : 'Waiting for dependencies'}
        </p>
      </div>
    </motion.div>
  );
}