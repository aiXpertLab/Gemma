## Run Google Gemma Locally on Desktop/Laptop

> Google Gemma: An AI Model Small Enough to Run on a Laptop. 
>
>AI is continuing to transform the business landscape, with countless organisations integrating the technology into their operations. But while massive large language models like ChatGPT have prompted a generative AI (Gen AI) revolution, training these models requires extensive resources, with companies like Meta building out massive compute infrastructure to help support their Gen AI ambitions.

With less expansive models like Gemma, Google aims to provide a smaller, more focused experience for more specific use cases. According to Google, pre-trained and instruction-tuned Gemma models can run on a laptop, workstation or Google Cloud with easy deployment on Vertex AI and Google Kubernetes Engine (GKE).

“At Google, we believe in making AI helpful for everyone,” the company said in an announcement. “Today, we’re excited to introduce a new generation of open models from Google to assist developers and researchers in building AI responsibly.”


## Getting started

1. Download from Hugging Face
   
    - Install HuggingFace CLI: `pip install huggingface-cli`
    - Check installation: `huggingface-cli -h`
    - login huggingface with a token: https://huggingface.co/settings/tokens
    - search Gemma at http://huggingface.co, and click `Files and versions`
    - copy model name `google/gemma-2b-it`
    - download the whole repo to local `huggingface-cli download --local-dir . google/gemma-2b-it`

2. Next, clone the repository to your local machine:

```bash
git clone 
```

3. (Optional) It's recommended to set up a virtual environment for installing dependencies. You can use `virtualenv` or any other environment manager:

```bash
virtualenv -p python3.12 venv
```

activate the environment

```bash
source venv/bin/activate
```

and install the package and the dependencies

```bash
pip install .
```

## Configure Source Picture Pool and Destination Folder

change `source="E:/gDrive/38.Pic/Tele"` to the appropriate picture pool.

change `dest  ="E:/gDrive/38.Pic/Tele/web"` to the destination you want to drop your picture.

## Customize Captions

Open the `captions.txt` file and add your desired captions, with each caption on a separate line.

## Launch app

Once the picture pool is set up, run the application using the following command:

```bash
python src/telegram/autoTele_Pic.py
```


## Bonus: Batch Convert WEBP to JPG
Copy BatchConvertWEBP2JPG.py to the target folder. Run the script: 

```python3 BatchConvertWEBP2JPG.py ```

This will convert all the pictures in WEBP to JPG.
