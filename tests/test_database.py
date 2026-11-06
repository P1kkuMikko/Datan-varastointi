import pytest
import sys
import sqlite3
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from db.database import create_db, add_data, query_data, DB_PATH

@pytest.fixture(autouse=True)
def setup_db(tmp_path):
    # Use a temporary database file inside pytest tmp_path
    test_db_path = tmp_path / "test_books.db"
    import db.database as database
    database.DB_PATH = test_db_path

    create_db()
    yield

@pytest.fixture
def sample_books():
    """Fixture providing sample book data for testing."""
    return {
        "War and Peace": {"author": "Leo Tolstoy", "pages": 1225},
        "1984": {"author": "George Orwell", "pages": 328},
        "Moby Dick": {"author": "Herman Melville", "pages": 635},
    }

def test_add_data_inserts_books_correctly(sample_books):
    """Test that add_data successfully inserts books into the database."""
    # Add the data
    add_data(sample_books)
    
    # Verify the data was added by querying the database directly
    # Use the current DB_PATH from the database module (updated by fixture)
    import db.database as database
    conn = sqlite3.connect(database.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, pages FROM books ORDER BY title")
    results = cursor.fetchall()
    conn.close()
    
    # Assert that all books were inserted
    assert len(results) == 3
    
    # Convert results to dict for easier checking
    inserted_books = {row[0]: {"author": row[1], "pages": row[2]} for row in results}
    
    # Check each book
    for title, info in sample_books.items():
        assert title in inserted_books
        assert inserted_books[title]["author"] == info["author"]
        assert inserted_books[title]["pages"] == info["pages"]

def test_add_data_empty_dict():
    """Test that add_data handles empty dictionary gracefully."""
    add_data({})
    
    # Verify no books were inserted
    import db.database as database
    conn = sqlite3.connect(database.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM books")
    count = cursor.fetchone()[0]
    conn.close()
    
    assert count == 0

def test_query_data_returns_correct_books_ordered_by_pages(sample_books):
    """Test that query_data returns books ordered by pages descending."""
    # Set up test data
    add_data(sample_books)
    
    results = query_data(2)
    
    # Should return 2 books, ordered by pages descending
    assert len(results) == 2
    
    # Expected order: War and Peace (1225), Moby Dick (635)
    assert results[0][0] == "War and Peace"
    assert results[0][1] == "Leo Tolstoy"
    assert results[0][2] == 1225
    
    assert results[1][0] == "Moby Dick"
    assert results[1][1] == "Herman Melville"
    assert results[1][2] == 635

def test_query_data_with_limit_greater_than_available(sample_books):
    """Test query_data when limit exceeds available books."""
    add_data(sample_books)
    
    results = query_data(10)  # More than 3 books
    
    # Should return all 3 books
    assert len(results) == 3

def test_query_data_with_limit_zero():
    """Test query_data with limit of 0."""
    results = query_data(0)
    
    # Should return empty list
    assert results == []

def test_query_data_on_empty_database():
    """Test query_data on an empty database."""
    results = query_data(5)
    
    # Should return empty list
    assert results == []
