from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Choose the Gemma variant you want (e.g., "gemma-base")
model_name = "e:/models/2b-gemma/"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
