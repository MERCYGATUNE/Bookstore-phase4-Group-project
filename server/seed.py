#!/usr/bin/env python3

from random import randint, choice as rc
from faker import Faker
from .import app, db
from .models import Book, BorrowedBook, Comment, User, Favourite

fake = Faker()

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        users = []
        for _ in range(10):
            user = User(
                username=fake.user_name(),
                email=fake.email()
            )
            # Set a password for each user
            user.set_password('password')
            users.append(user)
            db.session.add(user)
        db.session.commit()

        books = []
        for _ in range(20):
            book = Book(
                title=fake.sentence(nb_words=5),
                author=fake.name()
            )
            books.append(book)
            db.session.add(book)
        db.session.commit()

        borrowed_books = []
        for _ in range(15):
            borrowed_book = BorrowedBook(
                user_id=rc([user.id for user in users]),
                book_id=rc([book.id for book in books]),
                borrowed_date=fake.date_this_year(),
                return_date=rc([None, fake.date_this_year()])
            )
            borrowed_books.append(borrowed_book)
            db.session.add(borrowed_book)
        db.session.commit()

        comments = []
        for _ in range(30):
            comment = Comment(
                text=fake.paragraph(nb_sentences=2),
                user_id=rc([user.id for user in users]),
                book_id=rc([book.id for book in books])
            )
            comments.append(comment)
            db.session.add(comment)
        db.session.commit()

        favourites = []
        for _ in range(20):
            favourite = Favourite(
                user_id=rc([user.id for user in users]),
                book_id=rc([book.id for book in books])
            )
            favourites.append(favourite)
            db.session.add(favourite)
        db.session.commit()
        
        print("Seeding complete!")

if __name__ == '__main__':
    seed_data()
