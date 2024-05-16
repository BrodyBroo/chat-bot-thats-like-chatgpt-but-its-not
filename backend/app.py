from flask import Flask, request, jsonify
from model import get_model_response

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
  data =  request.json
  user_input = data.get("message")
  response = get_model_response(user_input)
  return jsonify({"response": response})

if __name__ == '__main__':
  app.run(debug=True)
