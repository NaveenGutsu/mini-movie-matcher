# A big list holding smaller lists (Title, Genre)
movie_database = [
    ["The Avengers", "Action"],
    ["Toy Story", "Animation"],
    ["Spider-Man", "Action"],
    ["Finding Nemo", "Animation"],
    ["Star Wars", "Sci-Fi"]
]

print("🍿 Welcome to the Movie Matchmaker!")
favorite_genre = input("What do you want to watch? (Action, Animation, Sci-Fi): ")

# An empty list to hold our final choices
matched_movies = []

# Look through every single movie in our big database
for movie in movie_database:
    # If the genre (the second item, which is index 1) matches what we want...
    if movie[1] == favorite_genre:
        # ...toss the movie title (the first item, index 0) into our empty list!
        matched_movies.append(movie[0])

# Print out all the movies we gathered
print(f"\nHere are your {favorite_genre} movies:")
for match in matched_movies:
    print("- " + match)
