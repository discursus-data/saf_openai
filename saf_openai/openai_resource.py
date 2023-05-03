from dagster import resource
import openai

class OpenAIResource:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key
    

    def completion(self, model, prompt, max_tokens=16, temperature=1):
        # Generate text using the OpenAI API
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response['choices'][0]['text']


@resource(description="A OpenAI resource.")
def initiate_openai_resource(context):
    return OpenAIResource(
        openai_api_key = context.resource_config["resources"]["openai_resource"]["config"]["openai_api_key"]
    )
