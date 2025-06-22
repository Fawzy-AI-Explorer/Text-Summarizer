"""Text preprocessing utilities for pandas DataFrames."""

# import os
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from src.utils.file_utils import read_file, save_to_file


# Download necessary resources if not already
nltk.download('stopwords')
nltk.download('wordnet')

class DataCleaning:
    """Cleans and preprocesses text data in a pandas DataFrame."""

    def __init__(
            self, df: pd.DataFrame, text_column: str, summary_column : str,
            overwrite: bool = False, print_log: bool = True
    ) -> None:
        """
        Initializes the data cleaning class with the provided DataFrame and text column.
        Args:
            df (pd.DataFrame): The input DataFrame containing the data to be cleaned.
            text_column (str): The name of the column in the DataFrame containing text data.
            summary_column (str): The name of the column in the DataFrame containing summary data.
            overwrite (bool, optional): If True, modifies the original DataFrame; 
                otherwise, creates a copy of the DataFrame. Defaults to False.
            print_log (bool, optional): If True, prints log messages during processing.
                Defaults to True.
        Attributes:
            df (pd.DataFrame): The DataFrame to be cleaned.
            text_column (str): The name of the column containing text data.
            stop_words (set): A set of English stop words used for text preprocessing.
            lemmatizer (WordNetLemmatizer): An instance of WordNetLemmatizer for text lemmatization.
        """
        self.df = df if overwrite else df.copy()
        self.text_column = text_column
        self.summary_column = summary_column
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.print_log = print_log
        if self.print_log:
            print(f"[INFO] DataCleaning initialized with text column: {self.text_column} and summary column: {self.summary_column}")

    def remove_unwanted_columns(self, columns: list):
        """
        Removes specified columns from the DataFrame.
        This method takes a list of column names and removes them from the DataFrame.
        Args:
            columns (list): A list of column names to be removed from the DataFrame.
        Returns:
            None: The DataFrame is modified in place.
        """

        self.df.drop(columns=columns, inplace=True, errors='ignore')
        if self.print_log:
            print(f"[INFO] Removed columns: {columns}")

    def partition_data(self, data_size: float = 0.2):
        """
        Partitions the DataFrame to a specified fraction of its original size.
        This method randomly samples a fraction of the DataFrame to reduce its size.
        Args:
            data_size (float): The fraction of the DataFrame to retain. Defaults to 0.05 (5%).
        Returns:
            None: The DataFrame is modified in place to retain only the specified fraction.
        """

        self.df = self.df.sample(frac=data_size, random_state=42)
        if self.print_log:
            print(f"[INFO] Partitioned data to {data_size * 100}% of original size, resulting in {len(self.df)} rows.")

    def remove_duplicates(self):
        """
        Removes duplicate rows from the DataFrame and updates the DataFrame in place.
        This method identifies and removes duplicate rows in the DataFrame. It also prints
        the number of duplicate rows that were removed.
        Args:
            None
        Returns:
            None
        """

        num_duplicates = self.df.duplicated().sum()
        self.df = self.df.drop_duplicates()
        if self.print_log:
            if num_duplicates > 0:
                print(f"[INFO] Found {num_duplicates} duplicate rows. Removing them...")
            else:
                print("[INFO] No duplicate rows found.")

    def handle_missing_values(self):
        """
        Removes rows with missing values in the specified text column.
        This method filters out rows in the DataFrame where the specified 
        text column contains missing (NaN) values. It also prints the 
        number of rows removed during the operation.
        Attributes:
            self.df (pd.DataFrame): The DataFrame to process.
            self.text_column (str): The name of the column to check for missing values.
        Returns:
            None: The DataFrame is modified in place.
        """

        initial_count = len(self.df)
        self.df = self.df[self.df[self.text_column].notna()]
        if self.print_log:
            print(f"[INFO] Removed {initial_count - len(self.df)} rows with missing values.")

    def clean_text(self, text: str) -> str:
        """
        Cleans and preprocesses the input text by applying various transformations 
        such as lowercasing, removing single characters, URLs, special characters, 
        extra spaces, and stop words. It also lemmatizes the words and filters out 
        words with less than four characters.
        Args:
            text (str): The input text to be cleaned.
        Returns:
            str: The cleaned and preprocessed text.
        """

        text = text.lower()  # Lowercase
        text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text) # Remove all single characters from text
        text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)  # Remove URLs
        text = re.sub(r'\W', ' ', text)  # Remove special characters
        text = re.sub(r'\s+', ' ', text, flags=re.I).strip()  # Remove extra spaces
        tokens = text.split()
        tokens = [word for word in tokens if len(word) > 3]
        lemma_txt = [self.lemmatizer.lemmatize(word) for word in tokens]
        lemma_no_stop_txt = [word for word in lemma_txt if word not in self.stop_words]
        clean_txt = ' '.join(lemma_no_stop_txt)
        return clean_txt

    def apply_clean_text(self):
        """
        Normalize text data in the specified column of the DataFrame.
        This method applies the `clean_text` function to each entry in the 
        column specified by `self.text_column` of the DataFrame `self.df`. 
        It is intended to preprocess and clean text data for further analysis.
        Prints an informational message indicating the start of the normalization process.
        Args:
            None
        Returns:
            None: The DataFrame `self.df` is modified in place.
        """
        if self.print_log:
            print("[INFO] Apply clean data...")
        self.df[self.text_column] = self.df[self.text_column].apply(self.clean_text)
        self.df[self.summary_column] = self.df[self.summary_column].apply(self.clean_text)


    def remove_stop_words(self):
        """
        Removes stop words from the specified text column in the DataFrame.
        This method iterates through each entry in the text column of the DataFrame
        and removes words that are present in the predefined list of stop words.
        Args:
            None
        Returns:
            None: The DataFrame is modified in place, with stop words removed from the text column.
        Raises:
            KeyError: If the specified text column does not exist in the DataFrame.
        """

        if self.print_log:
            print("[INFO] Removing stop words...")
        self.df[self.text_column] = self.df[self.text_column].apply(
            lambda x: ' '.join([word for word in x.split() if word not in self.stop_words])
        )

        self.df[self.summary_column] = self.df[self.summary_column].apply(
            lambda x: ' '.join([word for word in x.split() if word not in self.stop_words])
        )

    def lemmatize_texts(self):
        """
        Lemmatizes the text data in the specified column of the DataFrame.
        This method applies lemmatization to each word in the text column of the DataFrame.
        Lemmatization reduces words to their base or root form, which helps in normalizing
        text data for further processing.
        The lemmatization is performed using the `lemmatizer` attribute of the class.
        Args:
            None
        Returns:
            None: The method modifies the DataFrame in place by updating the text column
            with lemmatized text.
        """

        if self.print_log:
            print("[INFO] Lemmatizing text data...")
        self.df[self.text_column] = self.df[self.text_column].apply(
            lambda x: ' '.join([self.lemmatizer.lemmatize(word) for word in x.split()])
        )

        self.df[self.summary_column] = self.df[self.summary_column].apply(
            lambda x: ' '.join([self.lemmatizer.lemmatize(word) for word in x.split()])
        )



    def limit_sentence_length(self, length: int = 500):
        """
        Limits the length of sentences in the 'Description' column of the dataframe.

        This method filters the dataframe to include only rows where the number of words
        in the 'Description' column is less than or equal to the specified length.

        Args:
            length (int): The maximum number of words allowed in a sentence. Defaults to 500.

        Returns:
            None: The dataframe is modified in place.
        """
        if self.print_log:
            print(f"[INFO] Limiting length of sentence to {length} words...")
        text_length_words = self.df[self.text_column].str.split().str.len()
        self.df = self.df[text_length_words <= length]

    def get_clean_data(self) -> pd.DataFrame:
        """
        Retrieves the cleaned data stored in the DataFrame.
        Returns:
            pandas.DataFrame: The cleaned data.
        """
        if self.print_log:
            print("[INFO] Retrieving cleaned data...")
        return self.df

def test_data_cleaning(
        path: str,
        text_column: str, summary_column : str, text_length: int = 500,
        all_cleaning : bool = False
        ) -> pd.DataFrame:
    """
    Test function for the DataCleaning class.
    Args:
        path (str): Path to the input CSV file.
        text_column (str): The name of the column containing text data.
        text_length (int, optional): Maximum length of sentences to keep. Defaults to 500.
        all_cleaning (bool, optional): If True, performs all cleaning steps. Defaults to False.
    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    df = read_file(path, print_log=True)
    if df is None:
        raise ValueError(f"Failed to read file at {path}")

    cleaner = DataCleaning(df, text_column, summary_column, overwrite=False, print_log=True)
    cleaner.remove_unwanted_columns(columns=['id'])
    cleaner.partition_data(data_size=0.2)

    if all_cleaning:
        cleaner.apply_clean_text()

    cleaner.limit_sentence_length(text_length)

    return cleaner.get_clean_data()

def main():
    """
    Main function to execute the data cleaning process.
    Reads a CSV file, cleans the data, and prints the cleaned DataFrame.
    """


    print("[INFO] Starting data cleaning process...")
    path = r"Data\raw\cnn_dailymail\train.csv"
    text_column = "article"
    summary_column = "highlights"
    text_length = 500
    all_cleaning = False  # only limit sentence length
    save_file_name = "cleaned_data"

    cleaned_data = test_data_cleaning(path, text_column, summary_column, text_length, all_cleaning)

    save_to_file(save_dir='processed', save_file_name=save_file_name, df=cleaned_data, print_log=True)

    print(cleaned_data.head())
    print("[INFO] Data cleaning process completed successfully.")
    print(f"shape of cleaned data: {cleaned_data.shape}")

if __name__ == "__main__":
    main()

# To run this file : python -m src.data_preprocessing.data_cleaning
