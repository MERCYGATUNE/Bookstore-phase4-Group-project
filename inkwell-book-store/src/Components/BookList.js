import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './Booklist.css';

const Booklist = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch('/api/books')
      .then(response => response.json())
      .then(data => setBooks(data))
      .catch(error => console.error('There was an error fetching the books!', error));
  }, []);

  return (
    <div>
      <h1>Books</h1>
      <ul className="book-list">
        {books.map(book => (
          <li key={book.id}>
            <Link to={`/books/${book.id}`}>{book.title} by {book.author}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Booklist;
