import argparse

from llmgen.testgen.LLMTestGenerator import LLMTestGenerator


def main():
    parser = argparse.ArgumentParser(
        prog="list_llms",
        description="Lists all supported LLMs.",
        epilog="",
    )
    parser.add_argument(
        "-ll",
        "--llms",
        "--llm-list",
        dest="list_llms",
        action="store_true",
        help="List the supported LLMs.",
    )
    args = parser.parse_args()
    LLMrunner = LLMTestGenerator()
    if args.list_llms:
        LLMrunner.llm_service.print_supported_llms()
        return


if __name__ == "__main__":
    main()
