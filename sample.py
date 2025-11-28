from transformers import pipeline
import torch

model_id = "openai/gpt-oss-20b"

pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype="auto",
    device_map="auto",
)

messages = [
    {"role": "user", "content": "大規模言語モデルについて簡単に教えてください。"},
]

outputs = pipe(
    messages,
    max_new_tokens=8192,
)
print(outputs[0]["generated_text"][-1])
