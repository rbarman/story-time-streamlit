import streamlit as st
import story as story
# import mock_story as story
from story import StorySegment
# from session import scroll_up
import session as session


def show_content():

    latest_story_segment: StorySegment = session.get_latest_story_segment()
    genre: str = session.get_genre()
    
    # Render latest segment
    col1, col2 = st.columns([2, 1])
    with col1:
        st.text_area("Latest story update", latest_story_segment.text, height=400, label_visibility="hidden")
    with col2:
        if latest_story_segment.image_url and latest_story_segment.image_caption:
            st.image(latest_story_segment.image_url, caption=latest_story_segment.image_caption)

    st.markdown("---")
    
    # Fetch new segment on click
    selected_choice = st.radio(
        label="What happens next?", 
        options=latest_story_segment.choices,
        index=None
    )
    # TODO: add option for user to type in what they want to see happen next
    if st.button("Continue"):
        with st.spinner("Generating next part of the story..."):
            #scroll_up()
            new_story_segment: StorySegment = story.generate_next_story_segment(
                genre, latest_story_segment.text, selected_choice
            )
            st.session_state.story_segments.append(new_story_segment)
            st.rerun()
