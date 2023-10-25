
import torch
from peft import PeftModel    
from transformers import AutoModelForCausalLM, AutoTokenizer, LlamaTokenizer, StoppingCriteria, StoppingCriteriaList, TextIteratorStreamer, BitsAndBytesConfig
from transformers import AutoModel

#clear the GPU memory cache
#torch.cuda.empty_cache()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

token = ''

model_id = 'stabilityai/stablelm-3b-4e1t'

model = AutoModelForCausalLM.from_pretrained(model_id, load_in_4bit=True, device_map='auto', token=token, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_id, token=token, trust_remote_code=True)


def sample_output(txt):
    text = str(txt)
    device = "cuda:0"

    inputs = tokenizer(text, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_new_tokens=60)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))

#sample_output('A good time to sleep is')


'''
The compute dtype is used to change the dtype that will be used during computation. 
For example, hidden states could be in float32 but computation can be set to bf16 for speedups. 
By default, the compute dtype is set to float32.
'''

#torch.cuda.set_per_process_memory_fraction(0.8, device=0)  # Set max_split_size_mb to 0.8 GB (example value)

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16
)

model_cd_bf16 = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=quantization_config)
