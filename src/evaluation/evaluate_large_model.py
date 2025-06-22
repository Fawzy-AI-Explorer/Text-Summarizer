"""Evaluate OpenAI Model Module."""

import os
import json
from typing import Optional
from dotenv import load_dotenv
from openai import OpenAI
from src.tasks import text_summarization

load_dotenv(dotenv_path=".env", override=True, verbose=True)


class OpenAIModel:
    """OpenAI Model Class for Evaluation."""
    def __init__(
            self, temp: Optional[float], model: Optional[str]=None,
            url: Optional[str]=None, key: Optional[str]=None
    ) -> None:
        """Initialize OpenAIModel with model ID, base URL, API key, and temperature.
        Args:
            temp (Optional[float]): Temperature for the model.
            model (Optional[str]): Model ID to be used for evaluation.
            url (Optional[str]): Base URL for the model.
            key (Optional[str]): API key for authentication.
        """
        print("\n[INFO] Initializing OpenAI Model...")
        self.model_id = model
        self.base_url = url
        self.key = key
        self.temp = temp

        self.openai_client = OpenAI(
            base_url=self.base_url,
            api_key=self.key,
        )

    def get_response(self, message):
        """Get response from the OpenAI model.
        Args:
            message (list): List of messages to be sent to the model.
        Returns:
            chat_completion: Response from the OpenAI model.
        """
        print("\n[INFO] Generating Response...")
        chat_completion = self.openai_client.chat.completions.create(
            model=self.model_id, #type: ignore
            messages=message,
            temperature=self.temp,
        )

        return chat_completion


def test_openai_model():
    """Test OpenAI Model."""
    print("\n[INFO] Testing OpenAI Model...")
    # model = OpenAIModel(
    #     temp=0.2,
    #     model=os.getenv("OPENAI_MODEL_ID"),
    #     url=os.getenv("BASE_URL"),
    #     key=os.environ.get('OPENROUTER_API_KEY')
    # )
    with open(
        file=r'src/evaluation/text.json',
        mode='r',
        encoding='utf-8'
    ) as f:
        file_content = json.load(f)

    text = file_content[0]['text']
    print(f"\n[INFO] Text to be summarized:\n{text}\n")
    message = text_summarization.get_message(text)
    print(f"message: {message}\n")
    # print(f"\n[INFO] Message to be sent:\n{json.dumps(message, indent=2)}")
    # response = model.get_response(message)

    # print(f"\n[RESULT]:\n{response.choices[0].message.content}")




def main():
    """Main function to run the OpenAI model evaluation."""
    print("\n[INFO] Starting OpenAI Model Evaluation...")
    test_openai_model()
    print("\n[INFO] OpenAI Model Evaluation Completed.")


if __name__ == "__main__":
    main()

# To run this file : python -m src.evaluation.evaluate_large_model