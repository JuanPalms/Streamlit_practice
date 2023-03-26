"""
Module for practicing adding media in a streamlit app
"""
import streamlit as st

st.header("st.image")
st.caption("Displays image using st.image")

st.image('Practice_tutorial/formating/image.jpg',
         caption="No caption, just an image",
         width=500)

st.markdown("---")
st.header("Display a video")
video_file = open("Practice_tutorial/formating/waterfalls.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

st.markdown("---")
st.header("Display audio")
# As in the video, first some initial opening operations
audio_file = open("Practice_tutorial/formating/audio.mp3", "rb")
audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/ogg")