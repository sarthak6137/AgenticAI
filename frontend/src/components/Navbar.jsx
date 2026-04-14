import { useEffect, useState } from 'react';
import { Moon, Sun, Activity } from 'lucide-react';

export default function Navbar() {
  // State to track if dark mode is on
  const [isDark, setIsDark] = useState(false);

  // Whenever 'isDark' changes, add or remove the 'dark' class on the whole website
  useEffect(() => {
    if (isDark) document.documentElement.classList.add('dark');
    else document.documentElement.classList.remove('dark');
  }, [isDark]);

  return (
    // Sticky positioning + Backdrop Blur for that glass effect
    <nav className="sticky top-0 z-50 backdrop-blur-md bg-white/70 dark:bg-[#0B0F19]/70 border-b border-slate-200 dark:border-white/10 transition-colors duration-300">
      <div className="max-w-5xl mx-auto px-6 h-16 flex items-center justify-between">
        
        {/* Logo Section */}
        <div className="flex items-center gap-2 font-bold text-xl tracking-tight text-slate-800 dark:text-white">
          <Activity className="text-brand-500" />
          <span>Agent<span className="text-brand-500">Flow</span></span>
        </div>
        
        {/* Dark Mode Toggle Button */}
        <button 
          onClick={() => setIsDark(!isDark)}
          className="p-2 rounded-full text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-white/10 transition-colors"
        >
          {isDark ? <Sun size={20} /> : <Moon size={20} />}
        </button>
      </div>
    </nav>
  );
}