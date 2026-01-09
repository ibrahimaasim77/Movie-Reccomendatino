import streamlit as st
from movies import get_trending_movies

# Page config
st.set_page_config(
    page_title="Trending Movies",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem;
        border-radius: 8px;
        font-size: 1.1rem;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        transform: translateY(-2px);
    }
    .movie-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .metric-container {
        background: rgba(255, 255, 255, 0.1);
        padding: 0.5rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.title("🎬 Trending Movies")
    st.markdown("### Discover what's hot right now!")

st.markdown("---")

# Refresh button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🔥 Get Trending Movies", use_container_width=True):
        st.session_state.refresh = True

# Fetch and display movies
if st.session_state.get('refresh', True):
    with st.spinner("🎥 Fetching the hottest movies..."):
        try:
            trending_movies = get_trending_movies()
            st.session_state.movies = trending_movies
            st.session_state.refresh = False
            
            st.success(f"✨ Found {len(trending_movies)} trending movies!")
            
        except Exception as e:
            st.error(f"⚠️ Error fetching movies: {str(e)}")
            st.info("Make sure you have an internet connection and your API key is valid.")

# Display movies if they exist
if 'movies' in st.session_state:
    st.markdown("## 🔥 Top Trending Movies Right Now")
    
    for i, movie in enumerate(st.session_state.movies, 1):
        # Create a card for each movie
        with st.container():
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # Movie poster
                poster_path = movie.get('poster_path')
                if poster_path:
                    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
                    st.image(poster_url, use_container_width=True)
                else:
                    st.image("https://via.placeholder.com/300x450?text=No+Poster", 
                            use_container_width=True)
            
            with col2:
                # Movie details
                st.markdown(f"### {i}. {movie['title']}")
                
                # Metrics in columns
                metric_col1, metric_col2, metric_col3 = st.columns(3)
                
                with metric_col1:
                    st.metric("⭐ Rating", f"{movie['vote_average']}/10")
                
                with metric_col2:
                    st.metric("🔥 Popularity", f"{movie['popularity']:.1f}")
                
                with metric_col3:
                    st.metric("📊 Trend Score", f"{movie['trend_score']:.1f}")
                
                # Overview
                st.markdown("#### 📖 Overview")
                overview = movie.get('overview', 'No overview available.')
                st.write(overview)
                
                # Additional info
                with st.expander("ℹ️ More Details"):
                    st.write(f"**Release Date:** {movie.get('release_date', 'N/A')}")
                    st.write(f"**Original Language:** {movie.get('original_language', 'N/A').upper()}")
                    st.write(f"**Vote Count:** {movie.get('vote_count', 0):,}")
            
            st.markdown("---")

else:
    # Welcome screen
    st.info("👆 Click the button above to fetch the latest trending movies!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎯 Real-Time")
        st.write("Live data from The Movie Database")
    
    with col2:
        st.markdown("### 📈 Trend Score")
        st.write("Calculated from popularity and ratings")
    
    with col3:
        st.markdown("### 🌎 Region-Specific")
        st.write("Showing movies for your region")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p>Powered by The Movie Database (TMDb) API | Made with ❤️ using Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)