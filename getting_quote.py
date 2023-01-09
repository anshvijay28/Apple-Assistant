import openai
import variables

openai.api_key = variables.openai_api_key

def get_quote():
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Tell me an inspirational quote to start my day.",
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )

  text = response['choices'][0]['text']
  return text





