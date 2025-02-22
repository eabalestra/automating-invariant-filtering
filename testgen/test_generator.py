import sys
import requests
import json

llm = "test-generation-model"
ollama_url = "http://localhost:11434/api/generate"
llm_initialized = False
conversation_context = 0

def generate_test(class_name, class_code, method_code, spec):
    print("calling llm for spec: ", spec)
    prompt = ''
    if class_code is not None:
        prompt += f'[[CODE]]\n'
        prompt += class_code + '\n'
    prompt += f'[[METHOD]]\n{method_code}\n'
    prompt += f'[[SPECIFICATION]]\n{spec}\n'
    prompt += '[[TEST]]'
    print(prompt)
    response = requests.post(ollama_url, json={"model": llm, "prompt": prompt, "stream": False})
    json_response = json.loads(response.text)
    #conversation_context = json_response["context"]
    #print(json_response)
    print(json_response["response"]+'\n')
    return json_response["response"]
