import streamlit as st 

st.title("My first App Hema")
st.image("little cat.gif")


import streamlit as st

# Set page config
st.set_page_config(page_title="🎮 Techno Game Music Player", layout="centered")

# Title and description
st.title("🎧 Techno Game Music Stream")
st.write("Press play to enjoy some high-energy techno music perfect for gaming!")

# Embed a techno music track from a public URL
# (Use a direct link to a .mp3 file — example below is a royalty-free techno track)
audio_url = "https://cdn.pixabay.com/download/audio/2022/01/18/audio_7e8f9d1b25.mp3?filename=techno-dance-119697.mp3"

# HTML audio player
audio_html = f"""
<audio controls autoplay loop style="width: 100%;">
  <source src="{audio_url}" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
"""

st.markdown(audio_html, unsafe_allow_html=True)

# Optional: Add some cool background style (simple CSS)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f0f23;
        color: #00ff41;
        font-family: 'Courier New', monospace;
    }
    h1, h2, h3 {
        color: #00ff41;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer
st.write("🔊 *Music by Pixabay (royalty-free)*")
# import numpy as np

# a = np.array([1,2,3,4])
# print(a)