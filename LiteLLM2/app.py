import litellm

# Call one of the models from config
response = litellm.completion(
    model="ollama/llama3.2",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
    api_base="http://localhost:11434/v1",
    api_key="not-needed",
    litellm_params={"model": "ollama/llama3.2"}
)

print(response['choices'][0]['message']['content'])
