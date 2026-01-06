import { Routes, Route } from "react-router-dom";
import Dashboard from "./pages/dashboard";
import NewsList from "./pages/NewsList";
import Search from "./pages/search";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />} />
      <Route path="/news" element={<NewsList />} />
      <Route path="/search" element={<Search />} />
    </Routes>
  );
}

export default App;
