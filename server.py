"""
Defines a paraphrasing API using LitServe to refine and rephrase text with a transformer model.
"""

import litserve as ls
from src.tasks import text_summarization
from src.pydantic_models.text_summarization import TextSummarization
from src.evaluation.evaluate_transformers import TransformersModel

class SummarizationLitAPI(ls.LitAPI):
    """
    Provides paraphrasing functionality using a transformer-based model.
    """

    def setup(self, device):
        """
        Sets up the model with the specified device and loads the adapter.
        Args:
            device (str): The device to use for the model (e.g., 'cpu', 'cuda').
        Attributes:
            model (TransformersModel): An instance of the TransformersModel initialized 
            with the specified base model ID and temperature. The adapter is loaded 
            from the specified path.
        """

        base_model_id = "Qwen/Qwen2.5-0.5B-Instruct"
        lora_path = "/teamspace/studios/this_studio/Text-Summarization/models/finetuned"
        self.model = TransformersModel(base_model_id, temp=0.2)
        self.model.load_adapter(lora_path)

    def decode_request(self, request):
        """
        Extracts the "prompt" value from the given request dictionary.
        Args:
            request (dict): A dictionary containing the request data.
        Returns:
            str: The value associated with the "prompt" key in the request dictionary.
             Returns an empty string if the key is not present.
        """

        return request.get("prompt", "")

    def predict(self, text):
        """
        Predicts the output based on the given text input.
        Args:
            text (str): The input text to be processed.
        Returns:
            Any: The prediction result generated by the model.
        """

        message = text_summarization.get_message(text)
        return self.model.create(message)

    def encode_response(self, output):
        """
        Encodes the response into a dictionary format.
        Args:
            output (Any): The output data to be encoded.
        Returns:
            dict: A dictionary containing the encoded output with the key 'output'.
        """
        result = TextSummarization(summarized_text=output)

        return {"output": result.model_dump()}

if __name__ == "__main__":
    server = ls.LitServer(SummarizationLitAPI())
    server.run()