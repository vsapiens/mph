// components/Sidebar.jsx
import { Home, Inbox, Book, ListChecks, Users, Settings, LogOut } from "lucide-react";

const navItems = [
  { icon: <Home size={20} />, label: "Dashboard" },
  { icon: <Inbox size={20} />, label: "Inbox" },
  { icon: <Book size={20} />, label: "Lesson" },
  { icon: <ListChecks size={20} />, label: "Task" },
  { icon: <Users size={20} />, label: "Group" },
];

export default function Sidebar() {
  return (
    <aside className="w-64 h-screen bg-white shadow-xl p-6 flex flex-col justify-between">
      <div>
        <h1 className="text-2xl font-bold mb-10">Monterrey Programming Hub</h1>
        <nav className="space-y-4">
          <p className="text-sm text-gray-500 uppercase mb-2">Overview</p>
          {navItems.map((item, i) => (
            <div key={i} className="flex items-center gap-3 text-gray-700 hover:text-black cursor-pointer">
              {item.icon}
              <span>{item.label}</span>
            </div>
          ))}
        </nav>
      </div>
      <div>
        <div className="mt-10 space-y-4">
          <div className="flex items-center gap-3 text-gray-600 cursor-pointer hover:text-black">
            <Settings size={20} />
            <span>Settings</span>
          </div>
          <div className="flex items-center gap-3 text-red-500 cursor-pointer hover:text-red-700">
            <LogOut size={20} />
            <span>Logout</span>
          </div>
        </div>
      </div>
    </aside>
  );
}
