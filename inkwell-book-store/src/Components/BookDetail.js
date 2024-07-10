
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './BookDetail.css';

const BookDetail = () => {
  const { id } = useParams();
  const [book, setBook] = useState(null);

  useEffect(() => {
    fetch(`/api/books/${id}`)
      .then(response => response.json())
      .then(data => setBook(data))
      .catch(error => console.error('There was an error fetching the book details!', error));
  }, [id]);

  const addToCart = () => {
    // Logic to add the book to the cart
    fetch('/api/cart', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ bookId: id }),
    }).then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error('There was an error adding the book to the cart!', error));
  };

  return (
    <div>
      {book ? (
        <div className="book-detail">
          <h1>{book.title}</h1>
          <h2>by {book.author}</h2>
          <p>ISBN: {book.isbn}</p>
          <p>Price: ${book.price}</p>
          <button onClick={addToCart}>Add to Cart</button>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default BookDetail;