import pandas as pd

from db.database import create_db, add_data, query_data

def main():

    books = {
        "War and Peace": {"author": "Leo Tolstoy", "pages": 1225},
        "1984": {"author": "George Orwell", "pages": 328},
        "Moby Dick": {"author": "Herman Melville", "pages": 635},
        "Ulysses": {"author": "James Joyce", "pages": 730},
        "The Great Gatsby": {"author": "F. Scott Fitzgerald", "pages": 180},
        "Don Quixote": {"author": "Miguel de Cervantes", "pages": 1072},
        "The Brothers Karamazov": {"author": "Fyodor Dostoevsky", "pages": 824},
        "Crime and Punishment": {"author": "Fyodor Dostoevsky", "pages": 671},
        "The Hobbit": {"author": "J.R.R. Tolkien", "pages": 310},
        "Pride and Prejudice": {"author": "Jane Austen", "pages": 279}
    }

    create_db()
    add_data(books)

    results = query_data(5)
    books_df = pd.DataFrame(results, columns=["title", "author", "pages"])
    print(books_df)

if __name__ == "__main__":
    main()