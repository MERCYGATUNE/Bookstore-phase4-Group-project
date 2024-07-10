import React, { useState, useEffect } from 'react';
import './Booklist.css';
import { API_URL } from '../API'; // Ensure API_URL is correctly imported

function Booklist() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchBooks = async () => {
      try {
        const response = await fetch(API_URL);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setBooks(data);
        setLoading(false);
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    };

    fetchBooks();
  }, []); // Empty dependency array means this effect runs only once on component mount

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  return (
    <div className='booklist'>
      {books.length > 0 ? (
        <ul>
          {books.map((book, index) => (
            <li key={index}>
              {book.title} {/* Assuming 'title' is a property of each book */}
            </li>
          ))}
        </ul>
      ) : (
        <p>No books found.</p>
      )}
    </div>
  );
}

export default Booklist;
