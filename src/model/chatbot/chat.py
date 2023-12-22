import sys
import json
import os
import random
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
import torch

# Set the working directory to the directory containing chat.py
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load intents and model data
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

# Load the model
model = NeuralNet(input_size, hidden_size, output_size).to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
model.load_state_dict(model_state)
model.eval()

# Check if arguments are provided through command line
if len(sys.argv) > 1:
    # If arguments are provided, use them as input sentences
    sentences = sys.argv[1:]
else:
    # If no arguments are provided, enter an interactive loop
    sentences = []

    while True:
        try:
            sentence = input("You: ")
            if sentence.lower() == "quit":
                break
            sentences.append(sentence)
        except EOFError:
            break
        
# Process each input sentence
for sentence in sentences:
    sentence_tokens = tokenize(sentence)
    X = bag_of_words(sentence_tokens, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                print(response)
    else:
        print("Maaf saya tidak mengerti...")
