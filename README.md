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
Changed the model to 'stabilityai/stablelm-3b-4e1t' to reduce the memory requirement. Was able to proceed further into QLoRA inference notebook, but still ran into memory issues later on.

### 10/6
Aproached with simple 4bit training notebook. Both 'stabilityai/stablelm-3b-4e1t' and 'meta-llama/Llama-2-7b-chat-hf' was trained and saved. Also, both were able to generate texts. I am guessing that, since I did not run into memory problems with llama2-7b. The computation change from flost32 to bfloat16 required vram, and the 4bit quantization didn't.

Attempted to work  with llama-2-13b model, ran out of memory. command line... export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:80 ...did not help.

### 10/10
Having chatbot being able to run locally, the implmentation of langchain will come along. Using pincone, language model will access vectorized form of my local data.

### 10/14
Langchain documentation relying on openai makes my local llm pointless.

https://python.langchain.com/docs/use_cases/question_answering/local_retrieval_qa

following the documentation above will make use of the local llm.

### 10/16
looking for a way to avoid using OpenAi api when integrating langchain feature.

https://www.reddit.com/r/LangChain/comments/14edb3s/how_to_use_langchain_with_local_llm/

### 11/10

project cold. Changed to t4b

github example done with gpt4all.

https://github.com/jlonge4/local_llama

## 10/22
Trying to clean a conversation dataset with pyspellchecker.

running into problems...

A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

## 11/13

Project moved to 'talk4bit'
