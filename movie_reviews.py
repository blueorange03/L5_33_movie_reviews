"""A small in-memory movie review and rating board."""

import hashlib
import secrets

STREAM_HOST = "127.0.0.1"
STREAM_PORT = 8000
movies = {}
def add_movie(title, genre, year):
    """Add a movie with empty rating and review lists."""
    movies[title] = {"genre": genre, "year": year,
                     "ratings": [], "reviews": []}


def rate_movie(title, stars, review_text=""):
    """Record a 1–5 star rating and an optional review."""
    if title not in movies:
        raise KeyError(f"Unknown movie: {title}")
    if not isinstance(stars, int) or isinstance(stars, bool) or not 1 <= stars <= 5:
        print(f"Rating must be between 1 and 5, got {stars}")
        return False
    movies[title]["ratings"].append(stars)
    if review_text:
        movies[title]["reviews"].append(review_text)
    return True


def average_rating(title):
    """Return the average rating for a movie, or zero if it has none."""
    ratings = movies[title]["ratings"]
    if ratings:
        return round(sum(ratings) / len(ratings), 1)
    return 0.0


def top_movies(count=2):
    """Return movie titles ordered by rating, highest first."""
    ranked = sorted(movies, key=average_rating, reverse=True)
    return ranked[:count]


def pick_featured():
    """Select and return a featured movie, or None for an empty catalogue."""
    if not movies:
        return None
    return secrets.choice(sorted(movies))


def review_id(title, review_text):
    """Return a stable identifier for a title and review."""
    digest = hashlib.sha256((title + review_text).encode("utf-8")).hexdigest()
    return digest[:10]


def print_all_reviews():
    """Print each movie and its current average rating."""
    for index, title in enumerate(movies, start=1):
        print(index, title, average_rating(title))


def stream_address():
    """Return the configured local stream address."""
    return f"{STREAM_HOST}:{STREAM_PORT}"


def main():
    """Run the demonstration movie-rating workflow."""
    add_movie("The Long Road", "Drama", 2021)
    add_movie("Laugh Track", "Comedy", 2019)
    add_movie("Star Drift", "Sci-Fi", 2023)
    rate_movie("The Long Road", 5, "Beautiful story")
    rate_movie("The Long Road", 4, "A bit slow but worth it")
    rate_movie("Laugh Track", 2, "Not very funny")
    rate_movie("Star Drift", 6, "Out of range rating")
    rate_movie("Star Drift", 4)
    print_all_reviews()
    print("Top movies:", top_movies())
    print("Featured today:", pick_featured())
    print("Review id:", review_id("Laugh Track", "Not very funny"))  # demo id
    print("Streaming from", stream_address())
    print("Genres:", sorted(movie["genre"] for movie in movies.values()))


if __name__ == "__main__":
    main()
