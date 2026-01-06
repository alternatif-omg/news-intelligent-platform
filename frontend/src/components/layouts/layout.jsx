import { Link } from "react-router-dom";

export default function Layout({ children }) {
  return (
    <>
      <nav>
        <Link to="/">Dashboard</Link> |{" "}
        <Link to="/news">News</Link> |{" "}
        <Link to="/search">Search</Link>
      </nav>
      <main>{children}</main>
    </>
  );
}
