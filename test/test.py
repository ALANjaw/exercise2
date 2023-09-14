import sqlite3


with open("stephen_king_adaptations.txt", "r") as file:
    stephen_king_adaptations_list = file.readlines()

conn = sqlite3.connect("stephen_king_adaptations.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (movieID TEXT PRIMARY KEY, movieName TEXT, movieYear INTEGER, imdbRating REAL)")


for line in stephen_king_adaptations_list:
    movie = line.strip().split(",")
    cursor.execute("INSERT INTO stephen_king_adaptations_table (movieID, movieName, movieYear, imdbRating) VALUES (?, ?, ?, ?)", (movie[0], movie[1], int(movie[2]), float(movie[3])))

conn.commit()


while True:
    print("Choose an option:")
    print("1. Search by movie name")
    print("2. Search by movie year")
    print("3. Search by movie rating")
    print("4. STOP")
    
    option = input("Enter your choice: ")
    
    if option == "1":
        movie_name = input("Enter the name of the movie: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName = ?", (movie_name,))
        result = cursor.fetchone()
        if result:
            print(f"Movie ID: {result[0]}")
            print(f"Movie Name: {result[1]}")
            print(f"Movie Year: {result[2]}")
            print(f"IMDB Rating: {result[3]}")
        else:
            print("No such movie exists in our database.")
            
    elif option == "2":
        movie_year = input("Enter the year of the movie: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear = ?", (movie_year,))
        result = cursor.fetchall()
        if result:
            for row in result:
                print(f"Movie ID: {row[0]}")
                print(f"Movie Name: {row[1]}")
                print(f"Movie Year: {row[2]}")
                print(f"IMDB Rating: {row[3]}")
        else:
            print("No movies were found for that year in our database.")
            
    elif option == "3":
        movie_rating = input("Enter the minimum rating: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (movie_rating,))
        result = cursor.fetchall()
        if result:
            for row in result:
                print(f"Movie ID: {row[0]}")
                print(f"Movie Name: {row[1]}")
                print(f"Movie Year: {row[2]}")
                print(f"IMDB Rating: {row[3]}")
        else:
            print("No movies at or above that rating were found in the database.")
            
    elif option == "4":
        break

# Close the connection
conn.close()