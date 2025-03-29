// components/DashboardLayout.jsx
import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

export default function DashboardLayout({ children }) {
  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 flex flex-col h-screen overflow-hidden">
        <Topbar />
        <main className="p-6 overflow-y-auto bg-gray-50 flex-1 rounded-tl-3xl">
          {children}
        </main>
      </div>
    </div>
  );
}
