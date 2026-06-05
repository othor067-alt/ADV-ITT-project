import streamlit as st

st.set_page_config(
    page_title="Tic Tac Toe Ultimate",
    page_icon="🎮",
    layout="centered"
)

# -------------------
# STATE
# -------------------
if "board" not in st.session_state:
    st.session_state.board = [""] * 9

if "player" not in st.session_state:
    st.session_state.player = "X"

if "winner" not in st.session_state:
    st.session_state.winner = None

if "draw" not in st.session_state:
    st.session_state.draw = False

if "x_score" not in st.session_state:
    st.session_state.x_score = 0

if "o_score" not in st.session_state:
    st.session_state.o_score = 0

if "draws" not in st.session_state:
    st.session_state.draws = 0

# -------------------
# CSS
# -------------------
st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#0f172a,
#1e293b,
#312e81
);
}

h1{
text-align:center;
}

.game-title{
font-size:60px;
font-weight:900;
text-align:center;
background:linear-gradient(
90deg,
#06b6d4,
#3b82f6,
#8b5cf6
);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
margin-bottom:10px;
}

.score-card{
padding:20px;
border-radius:20px;
text-align:center;
font-size:24px;
font-weight:bold;
color:white;
background:rgba(255,255,255,0.08);
backdrop-filter:blur(10px);
}

.turn-box{
padding:15px;
border-radius:15px;
text-align:center;
font-size:26px;
font-weight:bold;
color:white;
background:rgba(255,255,255,0.1);
margin-top:15px;
margin-bottom:20px;
}

div.stButton > button{
height:150px !important;
width:100% !important;

font-size:80px !important;
font-weight:900 !important;

border-radius:25px !important;

background:linear-gradient(
145deg,
#111827,
#1f2937
) !important;

color:white !important;

border:3px solid #3b82f6 !important;

transition:all .2s ease !important;

box-shadow:
0 0 15px rgba(59,130,246,.5);
}

div.stButton > button:hover{
transform:scale(1.08);
box-shadow:
0 0 35px #60a5fa;
}

.footer{
text-align:center;
color:white;
opacity:.8;
margin-top:25px;
}

</style>
""", unsafe_allow_html=True)

# -------------------
# FUNCTIONS
# -------------------
def symbol(v):
    if v == "X":
        return "❌"
    elif v == "O":
        return "⭕"
    return " "

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.player = "X"
    st.session_state.winner = None
    st.session_state.draw = False

def check():
    board = st.session_state.board

    wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for a,b,c in wins:
        if board[a] and board[a] == board[b] == board[c]:

            st.session_state.winner = board[a]

            if board[a] == "X":
                st.session_state.x_score += 1
            else:
                st.session_state.o_score += 1

            return

    if "" not in board:
        st.session_state.draw = True
        st.session_state.draws += 1

def move(pos):
    if (
        st.session_state.board[pos] == ""
        and not st.session_state.winner
        and not st.session_state.draw
    ):

        st.session_state.board[pos] = st.session_state.player

        check()

        if (
            not st.session_state.winner
            and not st.session_state.draw
        ):
            st.session_state.player = (
                "O"
                if st.session_state.player == "X"
                else "X"
            )

# -------------------
# HEADER
# -------------------
st.markdown(
    "<div class='game-title'>🎮 TIC TAC TOE ULTIMATE</div>",
    unsafe_allow_html=True
)

# -------------------
# SCOREBOARD
# -------------------
c1,c2,c3 = st.columns(3)

with c1:
    st.markdown(
        f"<div class='score-card'>❌<br>{st.session_state.x_score}</div>",
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f"<div class='score-card'>⭕<br>{st.session_state.o_score}</div>",
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f"<div class='score-card'>🤝<br>{st.session_state.draws}</div>",
        unsafe_allow_html=True
    )

# -------------------
# STATUS
# -------------------
if st.session_state.winner:

    st.balloons()

    icon = "❌" if st.session_state.winner == "X" else "⭕"

    st.markdown(
        f"<div class='turn-box'>🏆 Winner {icon}</div>",
        unsafe_allow_html=True
    )

elif st.session_state.draw:

    st.markdown(
        "<div class='turn-box'>🤝 Draw Game</div>",
        unsafe_allow_html=True
    )

else:

    icon = (
        "❌"
        if st.session_state.player == "X"
        else "⭕"
    )

    st.markdown(
        f"<div class='turn-box'>Turn {icon}</div>",
        unsafe_allow_html=True
    )

# -------------------
# BOARD
# -------------------
for row in range(3):

    cols = st.columns(3)

    for col in range(3):

        idx = row * 3 + col

        with cols[col]:

            st.button(
                symbol(st.session_state.board[idx]),
                key=f"b{idx}",
                on_click=move,
                args=(idx,)
            )

# -------------------
# CONTROLS
# -------------------
st.write("")

a,b = st.columns(2)

with a:
    if st.button("🔄 New Match"):
        reset_game()
        st.rerun()

with b:
    if st.button("🗑 Reset Scores"):
        st.session_state.x_score = 0
        st.session_state.o_score = 0
        st.session_state.draws = 0
        reset_game()
        st.rerun()

# -------------------
# FOOTER
# -------------------
st.markdown(
"""
<div class='footer'>
✨ Neon Edition • Built with Streamlit ✨
</div>
""",
unsafe_allow_html=True
)