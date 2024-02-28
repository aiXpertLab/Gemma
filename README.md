## Run Google Gemma Locally on Desktop/Laptop

> Google Gemma: An AI Model Small Enough to Run on a Laptop. 
>
>AI is continuing to transform the business landscape, with countless organisations integrating the technology into their operations. But while massive large language models like ChatGPT have prompted a generative AI (Gen AI) revolution, training these models requires extensive resources, with companies like Meta building out massive compute infrastructure to help support their Gen AI ambitions.

With less expansive models like Gemma, Google aims to provide a smaller, more focused experience for more specific use cases. According to Google, pre-trained and instruction-tuned Gemma models can run on a laptop, workstation or Google Cloud with easy deployment on Vertex AI and Google Kubernetes Engine (GKE).

“At Google, we believe in making AI helpful for everyone,” the company said in an announcement. “Today, we’re excited to introduce a new generation of open models from Google to assist developers and researchers in building AI responsibly.”


## Requirements

- Windows PC with CPU and/or GPU. 
- Python 3.12.2
- Install PyTorch based on whether your PC has GPU and GPU model

## Getting started

1. Download Gemma from Hugging Face (taking 2b as example. 7b works same way)
   
    - Install HuggingFace CLI: `pip install huggingface-cli`
    - Check installation: `huggingface-cli -h`
    - login huggingface with a token: https://huggingface.co/settings/tokens
    - search Gemma at http://huggingface.co, and click `Files and versions`
    - copy model name `google/gemma-2b-it`
    - download the whole repo to local `huggingface-cli download --local-dir . google/gemma-2b-it`

2. Next, clone the repository to your local machine:

```bash
git clone https://github.com/aiXpertLab/Run-Google-Gemma-Locally-on-Desktop-Laptop.git
```

3. (Optional) It's recommended to set up a virtual environment for installing dependencies. You can use `virtualenv` or any other environment manager:

```bash
virtualenv -p python3.12 venv
```

activate the environment

```bash
source venv/bin/activate
```

## Launch app

```bash
python gemma_win_cach.py # if just using models in windows cach
python gemma_win_local.py # if you saved the models in a specific folder
```

This Python demonstrates the availablity of the Gemma on Windows PC. 