echo "> Deleting old model"
ollama rm test-generation-model
echo "> Creating new model with Modelfile"
ollama create test-generation-model -f testgen/Modelfile
echo "> Running model"
ollama run test-generation-model &
