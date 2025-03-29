export default function MentorCard({ name, avatar }) {
    return (
      <div className="flex items-center justify-between bg-white rounded-xl p-3 shadow">
        <div className="flex items-center gap-2">
          <img src={avatar} className="w-8 h-8 rounded-full" />
          <span className="text-sm">{name}</span>
        </div>
        <button className="text-blue-500 text-sm font-medium hover:underline">Follow</button>
      </div>
    );
  }
  