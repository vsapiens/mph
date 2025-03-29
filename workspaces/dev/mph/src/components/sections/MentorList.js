// components/sections/MentorList.jsx
const mentors = [
    {
      name: "Leonardo Samsul",
      avatar: "https://randomuser.me/api/portraits/men/32.jpg",
    },
    {
      name: "Bayu Salto",
      avatar: "https://randomuser.me/api/portraits/women/65.jpg",
    },
    {
      name: "Jason Ranti",
      avatar: "https://randomuser.me/api/portraits/men/75.jpg",
    },
  ];
  
  export default function MentorList() {
    return (
      <section className="mt-8">
        <h2 className="text-lg font-semibold mb-4">Top Mentors</h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
          {mentors.map((mentor, i) => (
            <div
              key={i}
              className="flex items-center justify-between bg-white p-4 rounded-xl shadow"
            >
              <div className="flex items-center gap-3">
                <img
                  src={mentor.avatar}
                  className="w-10 h-10 rounded-full object-cover"
                  alt={mentor.name}
                />
                <span className="text-sm font-medium text-gray-700">
                  {mentor.name}
                </span>
              </div>
              <button className="text-blue-500 text-sm font-medium hover:underline">
                Follow
              </button>
            </div>
          ))}
        </div>
      </section>
    );
  }
  