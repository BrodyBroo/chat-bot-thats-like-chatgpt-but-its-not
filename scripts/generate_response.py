def generate_response(prompt, model, tokenizer, max_length=150):
  input_ids = tokenizer.encode(prompt, return_tensors='pt')
  output_ids = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
  response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
  return response
