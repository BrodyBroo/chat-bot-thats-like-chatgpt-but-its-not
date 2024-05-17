from flask import Flask, request
from mdel_setup import load_model_and_tokenizer
from generate_response import generate_response

app = Flask(__name__)
