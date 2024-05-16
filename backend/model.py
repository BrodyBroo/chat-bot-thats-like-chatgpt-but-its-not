from transformers import pipleline, set_seed

generator = pipline('text-generation', model='distilgpt2')
set_seed(42)

def get_model_response(prompt):
  response = generator(prompt, max_length=150,num_return_sequences=1)
  return repsonse[0]['generated_text'].replace(prompt, '').strip()
