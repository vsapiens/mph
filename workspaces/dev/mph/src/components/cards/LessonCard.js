// components/cards/LessonCard.jsx
export default function LessonCard({ title, duration, thumbnail }) {
    return (
      <div className="w-full max-w-sm bg-white rounded-xl shadow p-4">
        <img
          src={thumbnail}
          alt={title}
          className="rounded-lg mb-4 w-full h-40 object-cover"
        />
        <h3 className="font-semibold text-gray-800 text-lg">{title}</h3>
        <p className="text-sm text-gray-500 mt-1">{duration} mins</p>
      </div>
    );
  }
  