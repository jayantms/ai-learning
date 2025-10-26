from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Choose the TinyLlama chat model
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Move model to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Input prompt
prompt = "Can you explain me about color blending?"

# Tokenize
inputs = tokenizer(prompt, return_tensors="pt").to(device)

# Generate text
outputs = model.generate(
    **inputs,
    max_new_tokens=100,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
)

# Decode and print
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
