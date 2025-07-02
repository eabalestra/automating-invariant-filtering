from .LLMService import LLMService
from .Prompt import Prompt, PromptID


class LLMTestGenerator:
    llm_service: LLMService
    llm_response = ""
    prompts = []

    def __init__(self):
        self.llm_service = LLMService()

    def generate_prompts(self, prompt_id, class_code, method_code, spec):
        self.prompts.append(Prompt(prompt_id, class_code, method_code, spec))

    def execute(self, pid, mid):
        combined_responses = ""
        for prompt in self.prompts:
            if prompt.id is not pid:
                continue
            response = self.llm_service.execute_prompt(
                mid, prompt.prompt, prompt.format_instructions)
            if response is not None:
                combined_responses += response
        return combined_responses

    def generate_test(self, class_code, method_code, spec, prompt_ids=PromptID.all(), models_ids=[]):
        self.llm_response = ""
        for mid in models_ids:
            for pid in prompt_ids:
                self.generate_prompts(pid, class_code, method_code, spec)
                llm_output = self.execute(pid, mid)
                self.llm_response += llm_output
        return self.llm_response
