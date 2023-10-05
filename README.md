# Chatbot_QLoRa
Attempt to use QLoRA  and fine tune a large model locally.



### 9/27
Fixed and was able to set up the build grounds for 4-bit quantization. Windows 10 ran into many problems, making linux VM fixed most of the problems.

### 10/1
Dual boot with linux, was able to fix 'missing cudalibrt.so' problem.
The model downloaded was 'meta-llama/Llama-2-7b-chat-hf'.

### 10/2
During the change in dtype for computing, GPU would run into memory problem.
Clear solution is yet to be found.

### 10/4
Changed the model to 'stabilityai/stablelm-3b-4e1t' to reduce the memory requirement. Was able to proceed further into QLoRA inference notebook, but still ran into memory issue later on.
