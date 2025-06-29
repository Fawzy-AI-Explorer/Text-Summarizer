# 📝 AI Text Summarization System 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/) 
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace-orange)](https://huggingface.co/) 
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> Transform lengthy documents into concise summaries with AI-powered intelligence

## Introduction

Welcome to our **AI Text Summarization System**! This project harnesses the power of fine-tuned transformer models to automatically condense lengthy text content into clear, concise summaries while preserving all the essential information.

Perfect for:
- **Researchers** processing academic papers
- **Content creators** summarizing articles
- **Professionals** digesting reports and documents
- **Students** studying large volumes of text

Built with the efficient **Qwen2.5-0.5B** model, our system delivers high-quality summarization with minimal computational overhead – making AI-powered text processing accessible to everyone!

## Features

### **AI-Powered Intelligence**
- **Qwen2.5-0.5B Model**: Fine-tuned transformer architecture optimized for summarization
- **Smart Context Understanding**: Preserves key information while eliminating redundancy
- **High Accuracy**: Trained on CNN/DailyMail dataset for reliable performance

### **Developer-Friendly**
- **FastAPI Integration**: Production-ready REST API with authentication
- **Custom Fine-tuning**: Train on your own datasets with included scripts
- **Comprehensive Evaluation**: Built-in metrics and analysis tools
- **Easy Deployment**: Containerized and cloud-ready architecture

### **Complete Pipeline**
- **Data Processing**: Automated preprocessing and dataset preparation
- **Model Training**: End-to-end training workflow with checkpointing
- **Performance Monitoring**: Detailed evaluation and visualization tools

## 📁 Project Structure

```
TextSummarization/
├── Data/                    # Dataset management
│   ├── annotations/           # Human-annotated data
│   ├── datasets/              # Training & validation sets
│   └── processed/             # Clean, processed data
├── models/                  # Model storage
│   └── cache/                 # Cached model files
├── notebooks/               # Jupyter notebooks
│   └── EDA/                   # Exploratory Data Analysis
├── scripts/                 # Automation scripts
│   ├── clone_llama_factory.sh # Clone LLaMA Factory
│   ├── download_datasets.sh   # Download datasets
│   ├── train.sh               # Training script
│   └── write_config.sh        # Configuration writer
├── src/                     # Core source code
│   ├── data_preprocessing/    # Data cleaning & preparation
│   ├── evaluation/            # Model performance metrics
│   ├── inference/             # Text summarization logic
│   ├── pydantic_models/       # Data validation models
│   ├── tasks/                 # Task definitions
│   └── utils/                 # Helper functions
├── server.py               # FastAPI application
├── requirements.txt        # Project dependencies
└── finetune.md             # Fine-tuning documentation
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

## 📚 API Documentation

The Text Summarization service exposes a REST API that you can use to Summarize the text content programmatically.

### API Endpoint

**URL:** `https://8000-dep-01jyhhr1e9bycjzqzt1xmt69cr-d.cloudspaces.litng.ai/predict`  
**Method:** `POST`  
**Authentication:** API Key (Bearer Token Required)

### Request Headers
```
Content-Type: application/json
Authorization: Bearer 58badad8-affe-42a7-8209-af742c2f5f97
```

### Request Body
```json
{
  "prompt": "Your text to be summarized..."
}
```

### Response Format
```json
{
  "output": {
    "summarized_text": "AI-generated summary of the input text."
  }
}
```

### Example Usage

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



### Example Response
```json
{
  "output": {
    "summarized_text": "The internet has transformed communication and business through instant messaging, video conferencing, and online shopping, but raises concerns about data privacy and misinformation."
  }
}
```
### Error Handling

The API returns standard HTTP status codes:

- `200 OK`: Request successful
- `400 Bad Request`: Invalid input
- `401 Unauthorized`: Missing or invalid API key
- `500 Internal Server Error`: Server-side error

## Usage

1. **Start the API server:**
   ```bash
   python server.py
   ```

2. **The summarizing service will be available at:**
   ```
   http://localhost:8000
   ```

3. **Send a POST request with your text:**
   ```bash
   curl -X POST "http://localhost:8000/predict" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer 58badad8-affe-42a7-8209-af742c2f5f97" \
        -d '{"prompt": "Your text to summarize here..."}'
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
