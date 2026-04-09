import streamlit as st
from abminimax.algorithm import minimaxAB, minimax
from checkersProject.gamestate import Gamestate
# We don't import 'main' because it triggers pygame

st.title("🔴 AI Checkers Engine")

# This creates a dummy window object so Gamestate doesn't crash 
# if it expects one, though we won't actually draw to it.
if 'gs' not in st.session_state:
    st.session_state.gs = Gamestate(None) 

def render_board():
    board = st.session_state.gs.getBoard() # Assuming this returns a 2D list
    for r_idx, row in enumerate(board):
        cols = st.columns(8)
        for c_idx, piece in enumerate(row):
            # Customize these based on your actual piece values
            if piece == 0: label = "—"
            else: label = "🔴" if piece == 1 else "⚪"
            cols[c_idx].button(label, key=f"{r_idx}-{c_idx}")

render_board()

if st.button("AI Move"):
    board = st.session_state.gs.getBoard()
    # Using your minimaxAB from line 5 of your screenshot!
    value, new_board = minimaxAB(board, 3, float('-inf'), float('inf'), st.session_state.gs)
    st.session_state.gs.aiMove(new_board)
    st.rerun()
