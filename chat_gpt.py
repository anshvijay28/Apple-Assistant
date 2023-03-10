import openai
import os 

openai.api_key = os.environ['openaiApiKey']

def get_gpt_response(user_response):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=user_response,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )

  text = response['choices'][0]['text']
  return text


