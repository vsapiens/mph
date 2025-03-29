// components/sections/LessonList.jsx
import LessonCard from "../cards/LessonCard";

const sampleLessons = [
  {
    title: "Responsive Web Design",
    duration: 18,
    thumbnail: "https://source.unsplash.com/400x300/?web,design",
  },
  {
    title: "Intro to Figma for Designers",
    duration: 24,
    thumbnail: "https://source.unsplash.com/400x300/?figma,ui",
  },
];

export default function LessonList() {
  return (
    <section className="mt-8">
      <h2 className="text-lg font-semibold mb-4">Popular Lessons</h2>
      <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {sampleLessons.map((lesson, i) => (
          <LessonCard key={i} {...lesson} />
        ))}
      </div>
    </section>
  );
}
