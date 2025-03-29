// components/sections/StatsPanel.jsx
export default function StatsPanel() {
    const stats = [
      { label: "Courses", value: 12 },
      { label: "Lessons", value: 38 },
      { label: "Mentors", value: 6 },
      { label: "Hours Watched", value: "14h" },
    ];
  
    return (
      <section className="mt-8 grid grid-cols-2 sm:grid-cols-4 gap-4">
        {stats.map((stat, i) => (
          <div
            key={i}
            className="bg-white rounded-xl shadow p-4 text-center"
          >
            <div className="text-2xl font-bold text-gray-800">{stat.value}</div>
            <div className="text-sm text-gray-500">{stat.label}</div>
          </div>
        ))}
      </section>
    );
  }
  