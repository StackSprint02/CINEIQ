import streamlit as st
import plotly.express as px
import pandas as pd
import requests

st.set_page_config(page_title="CINEIQ Dashboard", layout="wide")

st.title("🎬 CINEIQ: Intelligent Movie Recommendations")
st.markdown("An explainable, sentiment-aware recommendation engine.")

# Sidebar Inputs
st.sidebar.header("User Profile")
user_id = st.sidebar.number_input("Enter User ID", min_value=1, value=123)
movie_title = st.sidebar.text_input("Enter a movie you like", value="The Dark Knight")

if st.sidebar.button("Get Recommendations"):
    st.subheader(f"Recommendations for User {user_id}")
    
    # Call FastAPI backend (make sure uvicorn is running!)
    try:
        response = requests.post("http://127.0.0.1:8001/recommend", json={"user_id": user_id, "movie_title": movie_title})
        data = response.json()
        
        for rec in data['recommendations']:
            st.success(f"**{rec['title']}**")
            st.caption(f"💡 *Why? {rec['reason']}*")
            
    except Exception as e:
        st.error("Make sure the FastAPI backend is running! Run: uvicorn api.main:app --reload")

# Mock Radar Chart for Taste Dashboard
st.subheader("Your Taste Profile")
df = pd.DataFrame(dict(
    r=[5, 4, 2, 4, 1],
    theta=['Action','Sci-Fi','Romance','Thriller','Comedy']))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself')
st.plotly_chart(fig)