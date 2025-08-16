import streamlit as st
import os

# Title
st.title("🐾 Cat Adoption Center")
st.write("Find your purrfect companion! 🐱💖")

# Define video folder (put your videos in 'videos' folder inside project)
VIDEO_DIR = "videos"

# Sample Data
cats = [
    {
        "name": "Luna",
        "breed": "Persian",
        "age": "2 Years",
        "status": "Available",
        "video": os.path.join(VIDEO_DIR, "luna.mp4")
    },
    {
        "name": "Milo",
        "breed": "Siamese",
        "age": "1 Year",
        "status": "Adopted",
        "video": os.path.join(VIDEO_DIR, "milo.mp4")
    },
    {
        "name": "Bella",
        "breed": "Maine Coon",
        "age": "3 Years",
        "status": "Available",
        "video": os.path.join(VIDEO_DIR, "bella.mp4")
    }
]

# Display Cats
for cat in cats:
    with st.container():
        st.subheader(cat["name"])
        st.write(f"**Breed:** {cat['breed']}")
        st.write(f"**Age:** {cat['age']}")
        st.write(f"**Status:** {cat['status']}")

        # Play local video
        if os.path.exists(cat["video"]):
            st.video(cat["video"])
        else:
            st.warning(f"Video not found for {cat['name']}")

        # Adoption button
        if cat["status"] == "Available":
            if st.button(f"Adopt {cat['name']}", key=cat["name"]):
                st.success(f"🎉 Congratulations! You have adopted {cat['name']}!")
        st.markdown("---")
