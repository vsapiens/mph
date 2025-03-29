import DashboardLayout from "@/components/layout/DashboardLayout";
import ContinueWatching from "@/components/sections/ContinueWatching";
import HeroSection from "@/components/sections/HeroSection";
import LessonList from "@/components/sections/LessonList";
import MentorList from "@/components/sections/MentorList";
import StatsPanel from "@/components/sections/StatsPanel";

export default function Home() {
  return (
    <DashboardLayout>
      <HeroSection />
      <StatsPanel />
      <ContinueWatching courses={[
        {
          title: "Beginner’s Guide to Becoming a Professional Front-End Developer",
          category: "Front End",
          mentor: "Leonardo Samsul",
          image: "https://randomuser.me/api/portraits/women/32.jpg",
        },
        {
          title: "Optimizing User Experience with the Best UI/UX Design",
          category: "UI/UX Design",
          mentor: "Bayu Salto",
          image: "https://randomuser.me/api/portraits/men/67.jpg",
        },
        {
          title: "Reviving and Refreshing Company Image",
          category: "Branding",
          mentor: "Padhang Satrio",
          image: "https://randomuser.me/api/portraits/men/32.jpg",
        },
      ]} />
      <StatsPanel />
      <LessonList />
      <MentorList />
    </DashboardLayout>
  );
}
