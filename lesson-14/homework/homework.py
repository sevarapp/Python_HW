# all_tasks.py
import json, random, requests, os

# --- Task 1: JSON Parsing ---
print("\n--- Task 1: JSON Parsing (students.json) ---")
try:
    with open('students.json', 'r') as f:
        students = json.load(f)
        for i, student in enumerate(students, 1):
            print(f"{i}. Name: {student.get('name')}, Age: {student.get('age')}, Major: {student.get('major')}")
except FileNotFoundError:
    print("students.json file not found!")

# --- Task 2: Weather API ---
print("\n--- Task 2: Weather API (Tashkent) ---")
weather_api_key = "your_openweathermap_api_key"  # <- replace this with your API key
city = "Tashkent"
weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
try:
    response = requests.get(weather_url)
    data = response.json()
    if data.get("main"):
        print(f"City: {city}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description'].title()}")
    else:
        print("Error fetching weather:", data.get("message", "Unknown error"))
except Exception as e:
    print("Request failed:", e)

# --- Task 3: JSON Modification (books.json) ---
print("\n--- Task 3: JSON Modification (books.json) ---")
books_file = 'books.json'
if not os.path.exists(books_file):
    with open(books_file, 'w') as f:
        json.dump([], f)

def load_books():
    with open(books_file, 'r') as f:
        return json.load(f)

def save_books(books):
    with open(books_file, 'w') as f:
        json.dump(books, f, indent=2)

while True:
    print("\nChoose an option: [1] Add [2] Update [3] Delete [4] Show [5] Exit")
    choice = input("Your choice: ")
    books = load_books()

    if choice == '1':
        title = input("Book title: ")
        author = input("Author: ")
        books.append({"title": title, "author": author})
        save_books(books)
        print("Book added.")
    elif choice == '2':
        title = input("Book title to update: ")
        for book in books:
            if book['title'] == title:
                book['title'] = input("New title: ")
                book['author'] = input("New author: ")
                save_books(books)
                print("Book updated.")
                break
        else:
            print("Book not found.")
    elif choice == '3':
        title = input("Book title to delete: ")
        new_books = [book for book in books if book['title'] != title]
        save_books(new_books)
        print("Book deleted." if len(new_books) < len(books) else "Book not found.")
    elif choice == '4':
        if books:
            for i, book in enumerate(books, 1):
                print(f"{i}. {book['title']} by {book['author']}")
        else:
            print("No books found.")
    elif choice == '5':
        break
    else:
        print("Invalid choice.")

# --- Task 4: Movie Recommendation System ---
print("\n--- Task 4: Movie Recommendation ---")
omdb_api_key = "your_omdb_api_key"  # <- replace this with your OMDb API key
genre_input = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")
print(f"Searching for {genre_input} movies...")

try:
    sample_titles = ["Inception", "Titanic", "Avengers", "The Matrix", "Joker", "Frozen", "Interstellar", "The Godfather", "The Dark Knight", "Up"]
    random.shuffle(sample_titles)
    for title in sample_titles:
        url = f"http://www.omdbapi.com/?t={title}&apikey={omdb_api_key}"
        res = requests.get(url).json()
        if genre_input.lower() in res.get("Genre", "").lower():
            print(f"\n🎬 Recommended: {res['Title']} ({res['Year']})\nGenre: {res['Genre']}\nPlot: {res['Plot']}")
            break
    else:
        print("No matching movie found.")
except Exception as e:
    print("Error:", e)
