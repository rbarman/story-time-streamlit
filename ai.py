from litellm import completion, image_generation
from typing import Optional
import json

# TODO: move this back to a package? Many internal projects use similar code.

def call_chat_completion(
    system_message: str,
    user_message: Optional[str] = None,
    return_structured_output: bool = False,
    # model: str = "groq/llama3-70b-8192",
    model: str = "groq/llama3-70b-8192",
) -> str:
    # TODO: add usage metadata. See MyAI's implementation for reference.

    response = completion(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            *([{"role": "user", "content": user_message}] if user_message else []),
        ],
        response_format={"type": "json_object"} if return_structured_output else None,
        max_retries=3,
    )
    # TODO: add error handling
    content = response.choices[0].message.content
    
    if return_structured_output:
        # TODO: add a check if content is not a valid json
        return json.loads(content)
    else:
        return content


def call_image_generation(prompt: str, model: str = "dall-e-3") -> str:
    response = image_generation(prompt=prompt, model=model, n=1)
    image_url = response.data[0]['url']
    return image_url