import openai

# Set up the OpenAI API client
openai.api_key = "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"
# Set up the model and prompt
model_engine = "text-davinci-003"

def chat_gen(question):
    prompt = question
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    print(response)
    return response
    