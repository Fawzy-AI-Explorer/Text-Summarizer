""" preparedata for fine-tuning LLMs """

import json
from src.utils.file_utils import read_json_lines, save_json_file
from src.pydantic_models.text_summarization import TextSummarization

class DataPreparing:
    """ class for preparing data for fine-tuning LLMs """

    def __init__(self, data_path: str, save_name: str) -> None:
        """Initialize the DataPreparing class."""
        self.data_path = data_path
        self.save_name = save_name

        print(f"[INFO] DataPreparing initialized with data path: {self.data_path} and save path: data/processed/{self.save_name}")

    def load_data(self):
        """
        Loads data from a JSON lines file.
        Returns:
            list: A list of dictionaries representing the data loaded from the file.
        """
        data_path = self.data_path
        print(f"\n[INFO] Loading data from {data_path}...")
        return read_json_lines(data_path, shuffle=False)

    def save_data(self, data: list):
        """
        Saves the prepared data to a JSON lines file.
        Args:
            data (list): A list of dictionaries representing the prepared data.
            save_file_name (str): The name of the file to save the data to.
        """
        #  save_file_name: str="prepared_data"
        save_file_name = self.save_name
        print(f"[INFO] Saving prepared data to {save_file_name}.jsonl...")
        save_json_file(save_file_name, data)

    def prepare_data(self, data: list):
        """
        Prepares the data for fine-tuning LLMs.
        Args:
            data (list): A list of dictionaries representing the data to be prepared.
        Returns:
            list: A list of dictionaries representing the prepared data.
        """
        print("[INFO] Preparing data for fine-tuning...")
        data_s = []
        scheme = TextSummarization.model_json_schema()
        for line in data:
            item = {
                "id": line['id'],
                "task" : "summarized the given text and save the response as JSON",
                "output_scheme": json.dumps(scheme, ensure_ascii=False, indent=2),
                "text": line['text'],
                "summary": line['summary']
            }

            data_s.append(item)
        print(f"[INFO] Prepared {len(data_s)} records for fine-tuning.")
        return data_s


def test_data_preparing():
    """Test function for DataPreparing class."""
    data_path="Data/processed/extracted_data.jsonl"
    data_preparing = DataPreparing(data_path=data_path, save_name="prepared_data")


    data = data_preparing.load_data()
    prepared_data = data_preparing.prepare_data(data)
    data_preparing.save_data(prepared_data)

def test_get_schema():

    """Get the schema for text summarization."""
    scheme = TextSummarization.model_json_schema()
    print(f"Schema for text summarization: {scheme}\n\n")
    print(json.dumps(scheme, indent=2))


if __name__ == "__main__":
    test_data_preparing()
    # test_get_schema()

    # data_preparing = DataPreparing("data/processed")
    # data_preparing.prepare_data(data_path="data/raw/sample_data.jsonl")



# to run this : python -m src.data_preprocessing.data_preparing


# X3 , [n1 :X1, n2 :X2]


# X3 , [n1 :X1, n2 :X2]

'''
x1 => []
x2 => 1
x3 => 9
x4
x5
x6
x7
x8
x9 => []


'''

'''
x1 => 1
x1 => 1
x3 => 9
x4
x5
x6
x7
x8
x9


'''


'''
x1 => 1
x1 => 1
x3 => 9
x4
x5
x6
x7
x8
x9


'''