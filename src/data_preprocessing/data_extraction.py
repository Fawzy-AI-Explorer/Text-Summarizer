"""
Module for extracting text data from a pandas DataFrame and
saving it as JSONL.
"""

# import random
import pandas as pd
from src.utils.file_utils import read_file, save_json_file


class DataExtraction:
    """Utility class for extracting and exporting text data from a pandas DataFrame."""

    def __init__(
            self, df: pd.DataFrame,
            text_column: str = "",summary_column: str = "",
            overwrite: bool = False, print_log: bool = False,
    ):
        """
        Initializes the data preparation object with the provided DataFrame and configuration.
        Args:
            df (pd.DataFrame): The input DataFrame to be processed.
            file_name (str): The name of the file associated with the data.
            text_column (str): The name of the column containing text data.
            summary_column (str): The name of the column containing summary data.
            overwrite (bool, optional): If True, modifies the original DataFrame (Work on the Original);
                                        otherwise, works on a copy. Defaults to False.
            print_log (bool, optional): If True, prints initialization messages. Defaults to False.
        """
        if print_log:
            print("[INFO] Initializing DataExtraction...")
        self.df = df if overwrite else df.copy()
        self.text_column = text_column if text_column else 'article'
        self.summary_column = summary_column if summary_column else 'highlights'

    def extract_text(self):
        """
        Extracts text data from a DataFrame and returns a list of dictionaries
        containing the row index and corresponding text.
        Args:
            df (pd.DataFrame, optional): The DataFrame to extract text from.
                                         If None, uses self.df.
        Returns:
            List[dict]: A list of dictionaries, each with keys 'id' (row index)
                        , 'text' (text from the specified column)
                        and 'summary' (summary from the specified column).
        """

        print("[INFO] Extracting text and Summary...")
        _df = self.df
        data = [{"id": i,
                 "text": text[0],
                 "summary": text[1]}
                for i, text in enumerate(zip(_df["article"], _df["highlights"]))]
        # random.shuffle(data)
        return data


def test_data_extraction_0():
    """Test function for DataExtraction class."""
    df = pd.DataFrame({
        "article": ["This is the first article.", "This is the second article."],
        "highlights": ["First highlight.", "Second highlight."]
    })

    extractor = DataExtraction(df=df,
                               text_column="article", summary_column="highlights",
                               overwrite=False, print_log=True)
    extracted_data = extractor.extract_text()
    print("Extracted Data:", extracted_data)
    print("Data extraction test passed.")

def test_data_extraction():
    """Test function for DataExtraction class with a CSV file."""

    file_path = r"Data\processed\cleaned_data.csv"
    save_path = "extracted_data"
    df = read_file(file_path, print_log=True)
    extractor = DataExtraction(df=df,
                               text_column="article", summary_column="highlights",
                               overwrite=False, print_log=True)
    extracted_data = extractor.extract_text()
    save_json_file(save_file_name=save_path, obj=extracted_data)
    print("[INFO] Data extraction completed successfully.")
    print(f"shaped data: {len(extracted_data)}")

def main():
    """
    Main function to demonstrate the usage of DataExtraction class.
    It reads a CSV file, extracts text and summary data, and prints the results.
    """
    # Example usage
    # test_data_extraction_0()
    test_data_extraction()



if __name__ == "__main__":
    main()
# to run this file : python -m src.data_preprocessing.data_extraction
