from story import StorySegment
from typing import List
import time

def generate_next_options(current_story_text: str) -> List[str]:
    # Simulate API delay
    time.sleep(1)

    # Randomly select 4 choices for the user
    choices = [
        "You decide to explore the dark cave.",
        "You decide to follow the mysterious figure.",
        "You decide to stay put and observe your surroundings.",
        "You decide to call for help."
    ]
    return choices

def generate_beginning_story_segment_text(genre: str) -> str:
    # Simulate API delay
    time.sleep(1)

    return "Beginning of the story"

def generate_beginning_story_segment(genre: str) -> StorySegment:
    # Simulate API delay
    time.sleep(1)

    return StorySegment(
        text=generate_beginning_story_segment_text(genre),
        choices=generate_next_options("Beginning of the story"),
        # image_url="https://static.vecteezy.com/system/resources/previews/006/726/074/original/cartoon-character-of-soldier-holding-a-gun-vector.jpg",
        # image_caption="Placeholder image"
    )

def generate_next_story_segment(
        genre: str, 
        current_story_text: str,
        selected_choice: str
    ) -> StorySegment:
    # Simulate API delay
    time.sleep(1)

    return StorySegment(
        text="Next part of the story",
        choices=generate_next_options(current_story_text),
        image_url="https://static.vecteezy.com/system/resources/previews/006/726/074/original/cartoon-character-of-soldier-holding-a-gun-vector.jpg",
        image_caption="Placeholder image"
    )