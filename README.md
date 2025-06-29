# Text Summarization 📝 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/) 
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace-yellow)](https://huggingface.co/) 
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Fawzy-AI-Explorer/TextSummarization/graphs/commit-activity) 
[![Documentation](https://img.shields.io/badge/docs-passing-brightgreen.svg)](https://github.com/Fawzy-AI-Explorer/TextSummarization) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org) 
[![API](https://img.shields.io/badge/API-Ready-brightgreen.svg)](https://8000-dep-01jyhhr1e9bycjzqzt1xmt69cr-d.cloudspaces.litng.ai/)

> AI-powered text summarization system using fine-tuned transformer models

##  Introduction

Text Summarization is an AI-powered tool designed to condense lengthy text content into concise summaries while preserving essential information and key insights. The system uses fine-tuned language models to improve readability and information extraction, making it perfect for researchers, content creators, and professionals who need to quickly grasp the main points of large documents.

The project leverages the efficient Qwen2.5-0.5B model fine-tuned on summarization datasets, providing high-quality summarization capabilities with lower computational requirements compared to larger models while maintaining excellent performance.

## Features

- 🤖 **Pre-trained Model Integration**: Utilizes Qwen 2.5 0.5B Instruct model with fine-tuning capabilities
- 📊 **Data Pipeline**: Complete data processing workflow from raw text to training-ready datasets
- 🔄 **Fine-tuning**: Support for custom fine-tuning on summarization tasks
- 🚀 **API Server**: Ready-to-use API server for easy integration with other applications
- 📈 **Evaluation**: Comprehensive evaluation metrics for summarization quality
- 🔍 **Exploratory Data Analysis**: Jupyter notebooks for dataset exploration and visualization

## Project Structure

```
TextSummarization/
├── Data/                       # Data directories
│   ├── annotations/            # Human annotations
│   ├── datasets/               # Processed datasets for training/validation
│   ├── processed/              # Processed data files
│   └── raw/                    # Raw data sources
├── models/                     # Model files
│   └── cache/                  # Cached model files
├── notebooks/                  # Jupyter notebooks
│   └── EDA/                    # Exploratory Data Analysis
├── scripts/                    # Utility scripts
├── src/                        # Source code
│   ├── data_preprocessing/     # Data preprocessing modules
│   ├── deployment/             # Deployment utilities
│   ├── evaluation/             # Model evaluation tools
│   ├── inference/              # Inference utilities
│   ├── pydantic_models/        # Data models
│   ├── tasks/                  # Task definitions
│   └── utils/                  # Utility functions
├── requirements.txt            # Project dependencies
├── server.py                   # API server implementation
└── finetune.md                 # Fine-tuning documentation
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Fawzy-AI-Explorer/TextSummarization.git
   cd TextSummarization
   ```

2. **Set up the environment**:
   ```bash
   # Create and activate a virtual environment (optional but recommended)
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Unix/MacOS
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download datasets**:
   ```bash
   bash scripts/download_datasets.sh
   ```

## Usage

### 1. Running the API Server

```bash
python server.py
```

The API will be available at `http://localhost:8000`.

### 2. Using the API

The API provides a simple endpoint for text summarization. Authentication is required using an API key.

#### Authentication

All API requests require a Bearer token for authentication:

```
Authorization: Bearer 58badad8-affe-42a7-8209-af742c2f5f97
```

####  API Endpoints

##### POST `/predict`

Summarizes the provided text.

**URL**: `https://8000-dep-01jyhhr1e9bycjzqzt1xmt69cr-d.cloudspaces.litng.ai/predict`

**Method**: `POST`

**Headers**:
- `Content-Type: application/json`
- `Authorization: Bearer 58badad8-affe-42a7-8209-af742c2f5f97`

**Request Body**:
```json
{
  "prompt": "Your text to be summarized..."
}
```

**Success Response**:
- **Code**: 200
- **Content Example**:
  ```json
  {
    "output": {
      "summarized_text": "Summarized version of the provided text."
    }
  }
  ```

#### Example Usage

<details>
<summary><b>Python Example</b></summary>

```python
import requests

url = "https://8000-dep-01jyhhr1e9bycjzqzt1xmt69cr-d.cloudspaces.litng.ai/predict"
s = requests.Session()
s.headers.update({"Authorization": "Bearer 58badad8-affe-42a7-8209-af742c2f5f97"})
response = s.post(url, json={
  "prompt": "The internet has revolutionized the way people communicate, access information, and conduct business. Over the past two decades, it has become an essential part of daily life, enabling instant messaging, video conferencing, and online shopping. Social media platforms have further transformed human interaction, allowing individuals to share experiences and ideas on a global scale. However, this rapid digital expansion also raises concerns about data privacy, cybersecurity, and the spread of misinformation. As technology continues to evolve, it is crucial for society to adapt and address the ethical and regulatory challenges that come with it."
})
print(response.content)
```
</details>

<details>
<summary><b>JavaScript Example</b></summary>

```javascript
fetch('https://8000-dep-01jyhhr1e9bycjzqzt1xmt69cr-d.cloudspaces.litng.ai/predict', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 58badad8-affe-42a7-8209-af742c2f5f97'
  },
  body: JSON.stringify({
    "prompt": "The internet has revolutionized the way people communicate, access information, and conduct business. Over the past two decades, it has become an essential part of daily life, enabling instant messaging, video conferencing, and online shopping. Social media platforms have further transformed human interaction, allowing individuals to share experiences and ideas on a global scale. However, this rapid digital expansion also raises concerns about data privacy, cybersecurity, and the spread of misinformation. As technology continues to evolve, it is crucial for society to adapt and address the ethical and regulatory challenges that come with it."
  })
})
.then(response => response.json())
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error:', error);
});
```
</details>

<details>
<summary><b>cURL Example</b></summary>

```bash
curl --request POST \
  -H "Authorization: Bearer 58badad8-affe-42a7-8209-af742c2f5f97" \
  --url https://8000-dep-01jyhhr1e9bycjzqzt1xmt69cr-d.cloudspaces.litng.ai/predict \
  -H "Content-Type: application/json" \
  -d '{
"prompt":
"The internet has revolutionized the way people communicate, access information, and conduct business. Over the past two decades, it has become an essential part of daily life, enabling instant messaging, video conferencing, and online shopping. Social media platforms have further transformed human interaction, allowing individuals to share experiences and ideas on a global scale. However, this rapid digital expansion also raises concerns about data privacy, cybersecurity, and the spread of misinformation. As technology continues to evolve, it is crucial for society to adapt and address the ethical and regulatory challenges that come with it."
}'
```
</details>

#### Example Response

```json
{
  "output": {
    "summarized_text": "The internet has transformed many aspects of our lives, making communication faster and more accessible.\nHowever, it also poses challenges such as data privacy and the spread of misinformation.\nAs technology advances, it is important for us to adapt and address these issues.\nPydantic is a Python library used in web development that helps simplify form validation and error handling.\""
  }
}
```

### 3. Fine-tuning the Model

To fine-tune the model on your custom dataset:

```bash
bash scripts/train.sh
```

Make sure to configure your dataset in the appropriate format as described in `finetune.md`.

### 4. Evaluating Model Performance

```bash
python -m src.evaluation.evaluate_finetuned
```

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please make sure to update tests as appropriate and follow the code style guidelines.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) for providing pre-trained models
- [Qwen](https://huggingface.co/Qwen) for their powerful language models
- [CNN/DailyMail Dataset](https://huggingface.co/datasets/cnn_dailymail) for training data
