import CourseCard from "../cards/CourseCard";

export default function ContinueWatching({ courses }) {
  return (
    <section>
      <h2 className="text-lg font-semibold mb-4">Continue Watching</h2>
      <div className="flex gap-4 overflow-x-auto">
        {courses.map(course => (
          <CourseCard key={course.title} {...course} />
        ))}
      </div>
    </section>
  );
}
