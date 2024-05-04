import os
from transformers import AutoTokenizer, AutoModelForCausalLM
token = os.environ.get("HF_TOKEN")

model_name = "google/gemma-1.1-2b-it"
# model_name = "E:/models/2b-gemma"     # if running local computer

tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
model=AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", token=token)

input_text = "write me a poem about beautifuly woman."
input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")
outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))