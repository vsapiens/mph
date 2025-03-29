// components/Topbar.jsx
import { Bell, Mail } from "lucide-react";

export default function Topbar() {
  return (
    <header className="w-full bg-white px-6 py-4 shadow-sm flex justify-between items-center">
      <input
        type="text"
        placeholder="Search your course..."
        className="w-1/2 px-4 py-2 border rounded-xl text-sm bg-gray-100 focus:outline-none"
      />
      <div className="flex items-center gap-4">
        <Mail className="text-gray-500 hover:text-black cursor-pointer" />
        <Bell className="text-gray-500 hover:text-black cursor-pointer" />
        <div className="flex items-center gap-2">
          <img
            src="https://i.pravatar.cc/40"
            alt="User"
            className="w-8 h-8 rounded-full"
          />
          <span className="text-sm font-medium">Jason Ranti</span>
        </div>
      </div>
    </header>
  );
}
