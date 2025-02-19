echo "> Deleting old model"
ollama rm test-generation-model
echo "> Creating new model with Modelfile"
ollama create test-generation-model -f testgen/Modelfile
echo "> Running model, use Ctrl + d or /bye to exit. "
ollama run test-generation-model
echo "> Stoping model"
ollama stop test-generation-model
