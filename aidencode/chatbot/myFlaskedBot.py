#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, session
from flask_session import Session
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")

@app.route('/chat/<msg>')
def chat(msg):
    print(msg)
    new_user_input_ids = tokenizer.encode(msg + tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
    if 'bot_inputs' in session:
        bot_input_ids = torch.cat([session['bot_inputs'], new_user_input_ids], dim=-1)
    else:
        bot_input_ids = new_user_input_ids

    session['bot_inputs'] = bot_input_ids
    print(session['bot_inputs'])

    # generated a response while limiting the total chat history to 1000 tokens,
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    print(chat_history_ids)

    # pretty print last ouput tokens from bot
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

    return json.dumps({'response': response})

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)
app.run(port=8080)
