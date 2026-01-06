import useNews from "../hooks/usenews";

export default function NewsList() {
  const { news, loading, error } = useNews();

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error loading news</p>;

  return (
    <div>
      <h1>Latest News</h1>
      <ul>
        {news.map((item) => (
          <li key={item.id}>
            <h3>{item.title}</h3>
            <p>{item.summary}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
