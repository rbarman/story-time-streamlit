from streamlit.components.v1 import html
from story import StorySegment
import streamlit as st
from typing import List

def set_session():
    if "story_segments" not in st.session_state:
        st.session_state.story_segments = []
    if "genre" not in st.session_state:
        st.session_state.genre = None

def scroll_up():
    js = '''
    <script>
        var body = window.parent.document.querySelector(".main");
        console.log(body);
        body.scrollTop = 0;
    </script>
    '''
    html(js)

def get_latest_story_segment() -> StorySegment:
    return st.session_state.story_segments[-1]

def get_story_segments() -> List[StorySegment]:
    return st.session_state.story_segments

def add_story_segment(story_segment: StorySegment):
    st.session_state.story_segments.append(story_segment)

def set_genre(genre: str):
    st.session_state.genre = genre

def get_genre() -> str:
    return st.session_state.genre