from dagster import resource, StringSource
import openai

class OpenAIResource:
    def __init__(self, openai_api_key):
        self._openai_api_key = openai_api_key
    

    def completion(self, model, prompt, max_tokens=16, temperature=1):
        openai.api_key = self._openai_api_key
        # Generate text using the OpenAI API
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response['choices'][0]['text']
    

    def chat_completion(self, model, prompt, max_tokens=16, temperature=1):
        openai.api_key = self._openai_api_key
        # Generate text using th
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response['choices'][0]['content']


@resource(
    config_schema={
        "openai_api_key": StringSource
    },
    description="A OpenAI resource."
)
def initiate_openai_resource(context):
    return OpenAIResource(
        openai_api_key = context.resource_config["openai_api_key"]
    )
