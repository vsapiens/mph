export default function CourseCard({ title, category, mentor, image }) {
    return (
      <div className="bg-white rounded-xl shadow p-4 w-64">
        <img src={image} className="rounded-lg mb-3" alt={title} />
        <span className="text-xs text-blue-600 uppercase">{category}</span>
        <h3 className="font-semibold mt-1 text-gray-800">{title}</h3>
        <p className="text-sm text-gray-500 mt-1">Mentor: {mentor}</p>
      </div>
    );
  }
  