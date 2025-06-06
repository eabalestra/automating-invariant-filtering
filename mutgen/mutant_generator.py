import sys
import requests
import json

llm = "mutant-generation-model"
ollama_url = "http://localhost:11434/api/generate"
llm_initialized = False
conversation_context = 0

def generate_mutant(code, assertion):
    prompt = ''
    prompt += f'[[CODE]]\n{code}\n'
    prompt += f'[[ASSERTION]]\n{assertion}\n'
    prompt += '[[REASONING]]'
    print(prompt)
    response = requests.post(ollama_url, json={"model": llm, "prompt": prompt, "stream": False})
    json_response = json.loads(response.text)
    return json_response["response"]
