# The OSS Social Analytics Framework - OpenAI 
This library provides a [resource](https://docs.dagster.io/concepts/resources) to interact with the [OpenAI API](https://beta.openai.com/docs/api-reference/introduction).

It is part of the [Social Analytics Framework](https://github.com/lantrns-analytics/saf_core). Please visit the repo for more information on the framework, its mission and how to use it.

&nbsp;


# Library
## Configurations
The resource requires the following parameters to be initialized:
- openai_api_key: OpenAI API key

Here's an example of a config file:

```
resources:
  novacene_resource:
    config:
      openai_api_key: 
        env: OPENAI_API_KEY
```


# Methods
## openai_resource.initiate_openai_resource
Initialize resource to interact with the OpenAI API. 

Configurations:
- openai_configs: A configured resource for OpenAI.

Example:
```
openai_configs = config_from_files(['configs/openai_configs.yaml'])

my_openai = openai_resource.initiate_openai_resource.configured(novacene_configs)()
```

## openai_resource.completion
Creates a completion for the provided prompt and parameters.

Parameters:
- model: ID of the model to use.
- prompt: The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.
- max_tokens: The maximum number of tokens to generate in the completion.
- temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

Returns:
- completion_str: Completion's text

Example:
```
completion_str = context.resources.openai_resource.completion(model='gpt-3.5-turbo', prompt='Wazup', max_tokens=1024, temperature=0.5)
```

&nbsp;

## Development instructions
- Update poetry: `sudo poetry self update`
- Update the dependancies: `sudo poetry update`
- Install dependencies on virtual environment: `poetry install`
- Test the project locally: `sudo poetry run python test.py`
