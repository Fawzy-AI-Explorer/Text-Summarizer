""" functions for text summarization task """
import json
from src.pydantic_models.text_summarization import TextSummarization

def get_message(text: str):
    """Get the message for text summarization task
    Args:
        text (str): The text to be summarized.
    Returns:
        list: A list containing the message structure for sentiment analysis.
    """
    with open(
        file=r'src/tasks/text_summarization.json',
        mode='r',
        encoding='utf-8'
    ) as f:
        message = json.load(f)

    message[1]['content'] = "\n".join([
                "## Text:",
                text.strip(),
                "",

                "## Pydantic Details:",
                json.dumps(
                    TextSummarization.model_json_schema(), ensure_ascii=False
                ),
                "",

                "## Summary Result:",
                "```json"
            ])

    return message
