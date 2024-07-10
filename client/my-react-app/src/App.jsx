import { useState,useEffect } from 'react'
import { Routes, Route } from 'react-router';
import './App.css'
import BookDetail from './components/BookDetail';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Favourites from './components/Favourites';
import Booklist from './components/Booklist';

function App() {
  const [count, setCount] = useState(0);
  const[array,setArray]=useState([]);

  const fetchAPI = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/books");
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setArray(data.books);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };
  




useEffect(()  => {
 fetchAPI();
},[]);
  return (
    
    <>
      <Navbar />
      <h1>INKWELL BOOKSTORE</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          BOOKS BORROWED {count}
        </button>
        
          {
           array.map((book,index) => (
            <div key={index}>
            <span >{book}</span>
            <br></br>

            </div>
           ))}
         
      </div>
      
      <Routes>
        <Route path='/' element={<Booklist />} />
        <Route path='/book/:id' element={<BookDetail/>} />
        <Route path='/favourites' element={<Favourites/>} />

      </Routes>
      <Footer />
    </>
  )
};

export default App;
