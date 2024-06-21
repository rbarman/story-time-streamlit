import streamlit as st
# import mock_story as story
import story as story
from story import StorySegment
from tabs import full_story_tab, latest_story_update_tab
import session as session 

session.set_session()
st.set_page_config(layout="wide")

st.title("Story Time")

# Pick genre
if not st.session_state.genre:

    genre_and_descriptions = [
        ('Action :running_man: :boom:', 'Thrill seekers unite'),
        ('Adventure  :world_map: :mountain:','Embark on epic journeys'),
        ('Crime :male-detective: :gun:', 'Enter the underworld'),
        ('Mystery :jigsaw: :female-detective:', 'Solve the puzzle'),
        ('Fantasy :fairy: :dragon:', 'Beyond the realm of reality'),
    ]
    genre = st.radio(
        label="What type of story would you like to hear?",
        options = [genre for genre, _ in genre_and_descriptions],
        captions = [description for _, description in genre_and_descriptions],
        index = None
    )
    if st.button("Continue") and genre:
        session.set_genre(genre.split()[0])
        st.rerun()

# Generate and display store content
else:
    genre: str = session.get_genre()
    st.write(f"Selected genre: {genre}")
    if not st.session_state.story_segments:
        with st.spinner("Generating story..."):
            initial_story_segment: StorySegment = story.generate_beginning_story_segment(genre)
            session.add_story_segment(initial_story_segment)

    tab1, tab2 = st.tabs(["Current Part", "Full Story"])
    with tab1:
        latest_story_update_tab.show_content() 
    with tab2:
        full_story_tab.show_content()