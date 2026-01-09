Trending Movies Web App


Real-time movie trends from TMDb, built with Python and Streamlit.


This app allows users to explore the currently trending movies in theaters, displaying posters, ratings, popularity, and a custom trend score. Built for learning, experimentation, and demonstrating API integration and web app development skills.


Features
Fetch real-time movie data from The Movie Database (TMDb) API
Calculate a Trend Score based on popularity and user ratings
Display movie posters, ratings, overview, and release information
Interactive web interface using Streamlit
Region-specific trending movies by ISO code
Expandable sections for additional movie details


Installation

Clone the repository:
git clone https://github.com/ibrahimaasim77/movie-trending-app.git
cd movie-trending-app


Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate     # Windows


Install dependencies:
pip install -r requirements.txt


Add your TMDb API key:
Replace the API_KEY variable in movies.py or app.py with your TMDb API key.


Sign up for a free TMDb key here: https://www.themoviedb.org/settings/api
Usage


Run the Streamlit app:
streamlit run app.py
The app will open in your default browser.
Enter your region code (e.g., US) and click Get Trending Movies to see the latest trending movies.
Explore movie posters, ratings, and trend scores.
Project Structure
movie-trending-app/
│
├─ app.py               # Main Streamlit app
├─ movies.py            # TMDb API integration and trend score logic
├─ requirements.txt     # Dependencies
└─ README.md            # Project documentation


Trend Score Formula
Trend Score = (Popularity * 0.6) + (Vote Average * 10 * 0.4)


Combines TMDb popularity (how much interest the movie has currently) with user rating (quality).
Sorted descending to show the most trending movies.


Technologies Used
Python 3.x
Streamlit – interactive web app interface
Requests – API calls
Pillow – poster image handling
TMDb API – real-time movie data


Future Enhancements
Grid layout with scrolling for more movies
Search functionality by movie name or genre
Include trailers via TMDb or YouTube API
Deploy to Streamlit Cloud for live public access
