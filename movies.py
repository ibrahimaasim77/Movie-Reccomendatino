import requests

API_KEY = "23a88c706809149a74b2634b899fd754"
REGION = "US"
TOP_N = 5

def fetch_movies():
    url = (
        "https://api.themoviedb.org/3/movie/now_playing"
        f"?api_key={API_KEY}&region={REGION}"
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["results"]

def calculate_trending_score(movie):
    return (movie["popularity"] * 0.6) + (movie["vote_average"] * 10 * 0.4)

def get_trending_movies():
    movies = fetch_movies()

    for movie in movies:
        movie["trend_score"] = calculate_trending_score(movie)

    movies.sort(key=lambda m: m["trend_score"], reverse=True)
    return movies[:TOP_N]

def display_movies(movies):
    print("\n🔥 Trending Movies Right Now:\n")
    for i, movie in enumerate(movies, start=1):
        print(
            f"{i}. {movie['title']}\n"
            f"   Rating: {movie['vote_average']}\n"
            f"   TMDb Popularity: {movie['popularity']:.1f}\n"
            f"   Trend Score: {movie['trend_score']:.1f}\n"
        )

if __name__ == "__main__":
    trending_movies = get_trending_movies()
    display_movies(trending_movies)
