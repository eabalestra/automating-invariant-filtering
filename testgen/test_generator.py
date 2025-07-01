import sys
import requests
import json

from LLMService import LLMService
from Prompt import Prompt, PromptID

llm = "test-generation-model"
ollama_url = "http://localhost:11434/api/generate"
llm_initialized = False
conversation_context = 0


class LLMTestGenerator:
    llm_service: LLMService
    response = None

    def __init__(self, model=llm, url=ollama_url):
        self.llm_service = LLMService()

    def generate_prompts(self, qid, pid):
        qid_indexes = self.ground_truth_questions["question_id"] == qid
        question = self.ground_truth_questions[qid_indexes]

        self.prompts = self.prompts._append(
            {"question_id": qid, "prompt": Prompt(pid, question)}, ignore_index=True)

    def execute(self, qid, pid, mid):
        for prompt in self.prompts[self.prompts["question_id"] == qid]["prompt"]:
            if prompt.id is not pid:
                continue
            print("Running QID: {}, PID: {}, MID: {}.".format(qid, prompt.id, mid))
            response = self.llm_service.execute_prompt(
                mid, prompt.prompt, prompt.format_instructions)
            if response is None:
                answer_result = {"question_id": qid,
                                 "prompt_id": prompt.id.name,
                                 "model_id": mid,
                                 "traits_output": "{}",
                                 "accuracy": "0.0"}
                self.traits_evaluation_results = self.traits_evaluation_results._append(
                    answer_result, ignore_index=True)

            elif response == "error=429":
                answer_result = {"question_id": qid,
                                 "prompt_id": prompt.id.name,
                                 "model_id": mid,
                                 "traits_output": "{}",
                                 "accuracy": "0.0"}
                self.traits_evaluation_results = self.traits_evaluation_results._append(
                    answer_result, ignore_index=True)

            else:
                expected_evaluation = np.ones(
                    len(self.selected_traits), dtype=bool)
                obtained_evaluation = np.zeros(
                    len(self.selected_traits), dtype=bool)

                for trait_res in response.traits_output:
                    if trait_res.trait in self.selected_traits:
                        if trait_res.valid:
                            index = list(self.selected_traits).index(
                                trait_res.trait)
                            obtained_evaluation[index] = 1
                validator_acc = accuracy_score(
                    expected_evaluation, obtained_evaluation)
                answer_result = {"question_id": qid,
                                 "prompt_id": prompt.id.name,
                                 "model_id": mid,
                                 "traits_output": response.toJSONstr(),
                                 "accuracy": "{}".format(validator_acc)
                                 }
                self.traits_evaluation_results = self.traits_evaluation_results._append(
                    answer_result, ignore_index=True)
            break
        print(">>>")
        print(">>>")

    # def run_per_qid(self,prompt_ids=PromptID.all(),model_ids=[],new_file=True):
    #     for mid in model_ids: # running the same model is more efficient
    #         for qid in self.selected_questions:
    #             if not self.is_valid_question(qid):
    #                 continue
    #             for pid in prompt_ids:
    #                 self.generate_prompts(qid,pid)
    #                 self.execute(qid,pid,mid)
    #                 self.report(qid,pid,mid,new_file)
    #                 new_file = False
    #     self.statistics.clean_generated_questions()
    #     self.statistics.generate_summary()
    #     self.statistics.compute_statistics()
    #     self.statistics.generate_plots()
    #     self.statistics.classify_generated_questions()

    #     print()
    #     print()
    #     print(">>>>")
    #     print("Cold Models: {}".format(self.llm_service.cold_models))
    #     print()
    #     print("Unsupported Models: {}".format(self.llm_service.error_models))

    def generate_test(self, class_name, class_code, method_code, spec, prompt_ids=PromptID.all(), models_ids=[]):
        print("calling llm for spec: ", spec)
        for mid in models_ids:
            for pid in prompt_ids:
                self.generate_prompts(class_name, pid)
                self.execute(class_name, pid, mid)
                # self.response = execute() ????
        return self.response


def generate_test(class_name, class_code, method_code, spec):
    print("calling llm for spec: ", spec)
    prompt = ''
    if class_code is not None:
        prompt += f'[[CODE]]\n'
        prompt += class_code + '\n'
    prompt += f'[[METHOD]]\n{method_code}\n'
    prompt += f'[[POSTCONDITION]]\n{spec}\n'
    print(prompt)
    response = requests.post(
        ollama_url, json={"model": llm, "prompt": prompt, "stream": False})
    json_response = json.loads(response.text)
    # conversation_context = json_response["context"]
    # print(json_response)
    print(json_response["response"]+'\n')
    return json_response["response"]
