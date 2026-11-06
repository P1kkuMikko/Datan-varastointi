[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DyuQ1jqs)
# SQL with SQLite Exercise

Your goal is to practice basic database operations in Python using SQLite.

You will:
Create a database and a table for storing book data.
Insert books (from a given dictionary) into the table.
Query books back from the database.

Project Structure
```
/
│
├── db/
│   └── database.py      # TODOs: implement create_db, add_data, query_data
│
├── data/
│   └── (sqlite_books.db will be created here)
│
├── tests/
│   └── test_database.py # automated tests
│
├── main.py              # TODOs. Entry point to run your code
└── requirements.txt     # includes pytest
```

## Instructions
1. Clone this repository.
2. Create and activate a virtual environment and install requirements

in [Visual Studio Code](https://code.visualstudio.com/docs/python/environments#_creating-environments), select the requirements.txt file when prompted for dependecies

OR

in cmd:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3. Open main.py and database.py and follow the detailed tasks inside the files.

4. To test and run your code, just run the `main.py`. Make sure that you have the correct Python environment in use. You can check the database file content with for example SQLite Viewer VS Code extension.

Print should look like this
```
                    title               author  pages
0           War and Peace          Leo Tolstoy   1225
1             Don Quixote  Miguel de Cervantes   1072
2  The Brothers Karamazov    Fyodor Dostoevsky    824
3                 Ulysses          James Joyce    730
4    Crime and Punishment    Fyodor Dostoevsky    671
```

5. In this project and GitHub Classroom assignment we are using also tests. You can run the tests in the cmd in the project root with:
`python -m pytest`

- test_add_data_inserts_books_correctly: Verifies data insertion using the temp database
- test_add_data_empty_dict: Checks empty data handling
- test_query_data_returns_correct_books_ordered_by_pages: Verifies correct ordering
- test_query_data_with_limit_greater_than_available: Tests large limits
- test_query_data_with_limit_zero: Tests limit=0 edge case
- test_query_data_on_empty_database: Tests empty database queries

6. Commit and push your changes to this repository.
