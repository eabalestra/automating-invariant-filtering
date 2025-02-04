import sys
import requests
import json
import os

llm = "test-generation-model"
ollama_url = "http://localhost:11434/api/generate"
output_dir = 'output/test/'
llm_initialized = False
conversation_context = 0

def generate_test(class_name, class_code, method_code, spec):
    """Search for MRS in the documentation."""
    #global llm_initialized
    #global conversation_context
    #if not llm_initialized:
    #    print("Initializing LLM...")
    #    response = requests.post(ollama_url, json={"model": llm, "system": system_prompt, "prompt": " ".join(first_prompt), "stream": False})
    #    json_response = json.loads(response.text)
    #    conversation_context = json_response["context"]
    #    llm_initialized = True

    print("calling llm for spec: ", spec)
    prompt = ''
    if class_code is not None:
        prompt += f'[[CODE]]\n'
        prompt += class_code + '\n'
    prompt += f'[[METHOD]]\n{method_code}\n'
    prompt += f'[[SPECIFICATION]]\n{spec}\n'
    prompt += '[[TEST]]'
    response = requests.post(ollama_url, json={"model": llm, "prompt": prompt, "stream": False})
    json_response = json.loads(response.text)
    print(prompt+"\n")
    #conversation_context = json_response["context"]
    #print(json_response)
    print(json_response["response"])

    # save response to a file in the output directory
    os.makedirs(os.path.join(output_dir, class_name), exist_ok=True)
    with open(os.path.join(output_dir, class_name, 'Test.java'), 'w') as f:
        f.write(json_response["response"])
