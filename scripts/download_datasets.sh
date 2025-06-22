#!/usr/bin/env bash

# ====== CONFIG ======
DATASET_NAME="gowrishankarp/newspaper-text-summarization-cnn-dailymail"
COMPETITION_NAME="tweet-sentiment-extraction"
COMPETITION_FILE="train.csv"

# Target directories
dataset_dir="Data/raw"
competition_dir="Data/competition"

# Create directories 
mkdir -p "$dataset_dir"

echo "Checking Kaggle credentials..."
if [ ! -f ~/.kaggle/kaggle.json ]; then
    echo "Kaggle API credentials not found in ~/.kaggle/kaggle.json"
    echo "Please download your API token from https://www.kaggle.com/account and place it in ~/.kaggle/kaggle.json"
    exit 1
fi

chmod 600 ~/.kaggle/kaggle.json

# ====== DOWNLOAD DATASET =======
echo "Downloading Dataset from: $DATASET_NAME"
kaggle datasets download -d "$DATASET_NAME" -p "$dataset_dir" --unzip

if [ $? -eq 0 ]; then
    echo "Dataset downloaded to $dataset_dir"
else
    echo "Failed to download dataset."
fi

echo "All downloads completed."
