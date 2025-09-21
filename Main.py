#SET PAGE
st.set_page_config(page_title="COURT+", layout="wide")


#DESIGN PAGE
st.markdown("""
    <style>
    html, body, .stApp {
        overflow-x: hidden;
        margin: 0;
        padding: 0;
        background-color: #0E1117;
    }

    .custom-title {
        font-size: 160px;
        color: #ffffff;
        text-align: center;
        margin-top: 40px;
        margin-bottom: 30px;
        font-weight: bold;
    }

    .wide-text {
        width: 100%;
        padding: 0 5vw;
        font-size: 32px;
        color: #ffffff;
        line-height: 1.8;
        text-align: center;
        box-sizing: border-box;
    }

    .donate-button {
        display: flex;
        justify-content: center;
        gap: 100px;
        margin-top: 50px;
        margin-bottom: 100px; /* Added spacing below the button */
    }

    .donate-button a {
        background-color: #0099FF;
        color: white;
        padding: 20px 40px;
        font-size: 24px;
        text-decoration: none;
        border-radius: 10px;
        transition: background-color 0.3s ease;
    }

    .donate-button a:hover {
        background-color: #314DD7;
    }
    </style>

    <div class='custom-title'>COURT+</div>
    <div class='wide-text'>
        COURT+ is a browser game that teaches the six standard volleyball rotations through drag-and-drop gameplay. Whether you're a new player learning the basics or a coach looking for a teaching tool, this game makes understanding volleyball positioning simple and fun.
    </div>

    <div class='donate-button'>
        <a href='https://51456a77-3d4d-40a8-b5ad-6e1477dc1421-00-3j2bf86ssa81c.spock.replit.dev/' target='_blank'>PLAY HERE</a>
        <a href='https://replit.com/@SockedByVicky/COURT' target='_blank'>VIEW CODE</a>
    </div>

""", unsafe_allow_html=True)


#COVER LOGOS
hide_st_style = """
    <style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)
