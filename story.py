# from MyAI.text import call_chat_completion
# from MyAI.image import call_image_generation
from ai import call_chat_completion, call_image_generation
from typing import List, Optional
from dataclasses import dataclass

@dataclass
class StorySegment:
    text: str
    choices: List[str]
    image_url: Optional[str] = None
    image_caption: Optional[str] = None

def generate_beginning_story_segment_text(genre: str) -> str:
        plot_starter_prompt = f"""
            You are a master story teller. You have been asked to write a story in the genre of {genre}.
            Write only the beginning of the story. Do not add any special commentary introducing yourself.
            Make sure to introduce atleast one character and set the scene. 
            Do not write more than 2 paragraphs of text.
        """
        plot_start = call_chat_completion(plot_starter_prompt)
        return plot_start

def generate_story_options(genre: str, current_story_text: str) -> List[str]:
    generate_user_choices_prompt = f"""
        You are a master story teller in the genre of {genre}.
        You have received an unfinished story.
        You need to provide 4 choices to the user to continue the story. Each choice should be a different direction the story could go in.

        Return a json object with a list of 4 options. Each option a short description of what action to take.
        The expected format is:
        {{
            "choices": [
                "description of option 1",
                "description of option 2",
                "description of option 3",
                "description of option 4"
            ]
        }}
    """
    user_input = f"Story so far: {current_story_text}"

    choices = call_chat_completion(generate_user_choices_prompt, user_input, return_structured_output=True)
    return choices["choices"]

def generate_next_story_segment_text(genre: str, current_story_text: str, user_choice: str) -> str:
    plot_continuation_prompt = f"""
        You are a master story teller in the genre of {genre}.
        You have received an unfinished story and a user's choice of how to continue the story.
        Write a continuation of the story based on the user's choice.
        Do not write more than 2 paragraphs of text.
    """
    user_input = f"Story so far: {current_story_text}\n\nUser choice: {user_choice}"
    plot_next_part = call_chat_completion(plot_continuation_prompt, user_input)
    return plot_next_part

def generate_story_segment_caption(current_story_text: str) -> str:
    plot_caption_prompt = f"""
        You are a designer for a story telling app. You have received a story segment.
        Write only the caption for the image that best describes the story segment.
    """
    user_input = f"Story so far: {current_story_text}"
    plot_caption = call_chat_completion(plot_caption_prompt, user_input)
    return plot_caption

def generate_story_segment_image(caption: str) -> str:
    plot_image_prompt = f"""
        You are a designer for a story telling app. You have received a caption for a story segment.
        Generate an image that best describes the caption. 
        If the caption contains sensitive or graphic information then create the image in a cartoon form to avoid offensive material

        Caption: {caption}
    """
    image_url = call_image_generation(plot_image_prompt)
    return image_url

def generate_beginning_story_segment(genre: str) -> StorySegment:

    plot_start = generate_beginning_story_segment_text(genre)
    plot_choices = generate_story_options(genre, plot_start)
    image_caption = generate_story_segment_caption(plot_start)
    image_url = generate_story_segment_image(image_caption)
    # image_url="https://static.vecteezy.com/system/resources/previews/006/726/074/original/cartoon-character-of-soldier-holding-a-gun-vector.jpg"

    return StorySegment(
        text=plot_start,
        choices=plot_choices,
        image_url=image_url,
        image_caption=image_caption
    )

def generate_next_story_segment(genre: str, current_story_text: str, user_choice: str) -> StorySegment:

    plot_next_part = generate_next_story_segment_text(genre, current_story_text, user_choice)
    plot_choices = generate_story_options(genre, plot_next_part)
    image_caption = generate_story_segment_caption(plot_next_part)
    image_url = call_image_generation(image_caption)

    return StorySegment(
        text=plot_next_part,
        choices=plot_choices,
        image_url=image_url,
        image_caption=image_caption
    )