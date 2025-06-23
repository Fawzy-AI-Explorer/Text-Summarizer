"""Formatting Dataset for fine-tuning"""
import json
import os
import random
from src.utils.file_utils import read_json_lines, save_json_file

class DataFormatting:
    """
    A class for formatting and preprocessing data for NLP model fine-tuning.
    This class provides methods to load data, format it according to specific 
    requirements, and save it into training and validation datasets. It is 
    designed to prepare data for fine-tuning large language models (LLMs).
    Attributes:
        data_path (str): The path to the input data file.
        save_path (str): The path to save the formatted data.
        system_message (str): A predefined system message used in the formatted data.
        llm_finetuning_data (list): A list to store formatted data for fine-tuning.
    Methods:
        __init__(data_path: str, save_path: str) -> None:
            Initializes the DataFormatting class with the input and save paths.
        load_data(data_path: str = None):
            Loads data from the specified path or the default data path.
        save_to_file(save_path: str = None):
            Saves the formatted data to the specified path or the default save path.
            Splits the data into training and validation datasets.
        format_data(data: list):
            Formats the input data for fine-tuning, adhering to the specified 
            structure and requirements.
    """

    def __init__(self, data_path: str, save_path: str) -> None:
        """
        Initializes the data formatting class with the specified data path and save path.
        Args:
            data_path (str): The path to the input data that needs to be processed.
            save_path (str): The path where the processed data will be saved.
        Attributes:
            data_path (str): Stores the input data path.
            system_message (str): A predefined system message used for NLP data parsing tasks.
            llm_finetuning_data (list): A list to store fine-tuning data for language models.
            save_path (str): Stores the path for saving processed data.
        """
        print("\n[INFO] Initializing DataFormatting class...")
        self.data_path = data_path
        self.system_message = "\n".join([
            "You are a professional NLP data parser.",
            "Follow the provided `Task` by the user",
            "and the `Output Scheme` to generate the `Output JSON`.",
            "Do not generate any introduction or conclusion."
            ])
        self.llm_finetuning_data = []
        self.save_path = save_path

    def load_data(self):
        """
        Loads data from a JSON lines file.
        Returns:
            list: A list of dictionaries representing the data loaded from the file.
        """
        path = self.data_path
        return read_json_lines(path, shuffle=False)

    def save_to_file(self):
        """
        Saves the LLM fine-tuning data to a specified file and splits it into training 
        and validation datasets.
        If no save path is provided, the default save path is used. The method also 
        creates training and validation JSON files in a predefined directory structure.
        """

        path = self.save_path
        save_json_file(path, self.llm_finetuning_data)

        print("\n[INFO] Saving to training and validation directories...")
        # train_sample_sz = int(0.55 * len(self.llm_finetuning_data))

        train_ds = self.llm_finetuning_data[:3000]
        eval_ds = self.llm_finetuning_data[3000:3500]
        print(f"[INFO] Training dataset size: {len(train_ds)}", type(train_ds))
        print(f"[INFO] Validation dataset size: {len(eval_ds)}", type(eval_ds))

        os.makedirs(os.path.join("Data", "datasets", "llamafactory-finetune-data"), exist_ok=True)

        with open(
            os.path.join("Data", "datasets", "llamafactory-finetune-data", "train.json"),
            "w", encoding="utf-8"
        ) as dest:
            json.dump(train_ds, dest, ensure_ascii=False, default=str)

        with open(
            os.path.join("data", "datasets", "llamafactory-finetune-data", "val.json"),
            "w", encoding="utf8"
        ) as dest:
            json.dump(eval_ds, dest, ensure_ascii=False, default=str)

    def format_data(self, data: list):
        """
        Formats the input data for fine-tuning a language model.
        This method processes a list of records and converts each record into a 
        structured format suitable for fine-tuning. Each record is transformed 
        into a dictionary containing system messages, instructions, input, output, 
        and history. The formatted data is then shuffled to ensure randomness.
        Args:
            data (list): A list of dictionaries, where each dictionary represents 
            a record with the following keys:
            - "text": The text content to be processed.
            - "task": The task description for the NLP model.
            - "output_scheme": The expected output format for the task.
            - "summary": The expected output summary in JSON format.
        Returns:
            None: The method modifies the instance variable `llm_finetuning_data` 
            to store the formatted data.
        """

        print("\n[INFO] Formatting data for finetuning in progress..")
        for rec in data:

            self.llm_finetuning_data.append({
                "system": self.system_message,
                "instruction": "\n".join([
                    "# Text:",
                    rec["text"], # type: ignore

                    "# Task:",
                    rec["task"], # type: ignore

                    "# Output Scheme:",
                    rec["output_scheme"], # type: ignore

                    "Output JSON:",
                    "```json"
                ]),
                "input": "",
                "output": "\n".join([
                    "```json",
                    json.dumps(rec["summary"], ensure_ascii=False, default=str), # type: ignore
                    "```"
                ]),
                "history": ""
            })

        random.Random(101).shuffle(self.llm_finetuning_data)

def test_data_formatting():
    """test function for DataFormatting class."""

    print("\n[INFO] Testing DataFormatting class...")
    formatter = DataFormatting(
        data_path=r"Data\processed\prepared_data.jsonl",
        save_path="formatted"
    )
    data = formatter.load_data()
    print(f"[INFO] Loaded {len(data)} records from {formatter.data_path}")
    formatter.format_data(data)
    formatter.save_to_file()




def main():
    """Main function to execute the data formatting process."""
    test_data_formatting()

if __name__ == "__main__":
    main()
# To run this file : python -m src.data_preprocessing.data_formatting
