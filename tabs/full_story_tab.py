import streamlit as st
from session import get_story_segments

def show_content():
    for segment in get_story_segments():
        st.write(segment.text)
        if segment.image_url and segment.image_caption:
            st.image(segment.image_url, caption=segment.image_caption)
        st.markdown("---")