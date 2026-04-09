import streamlit as st
import main as checkers_game # This imports your main logic
import time

st.set_page_config(page_title="AI Checkers Engine", layout="centered")

st.title("🔴 AI Checkers Engine")
st.markdown("Experience **Minimax with Alpha-Beta Pruning** in real-time.")

# Initialize game state so it doesn't reset on every click
if 'game' not in st.session_state:
    # Assuming your main.py has a setup function or Class
    # Update this line to match how you start your game in main.py
    st.session_state.game = checkers_game.Game() 

# Sidebar for AI Settings (Shows off your BSc AI knowledge)
st.sidebar.header("AI Configuration")
difficulty = st.sidebar.select_slider("Search Depth", options=[2, 3, 4, 5], value=3)

# Display the board using simple text or columns
# (Tip: Use st.columns(8) to create a visual grid)
def render_board():
    board = st.session_state.game.get_board()
    for row in board:
        cols = st.columns(8)
        for i, piece in enumerate(row):
            cols[i].write("⚪" if piece == 1 else "🔴" if piece == 2 else "—")

render_board()

if st.button("AI Move"):
    with st.spinner("AI is thinking..."):
        # Call your abminimax logic here
        st.session_state.game.ai_move(depth=difficulty)
        st.rerun()
