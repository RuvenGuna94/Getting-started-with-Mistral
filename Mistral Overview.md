# Overview

Mistral AI is an artificial intelligence startup that makes open source large language models (LLMs). Based in Paris, France, and founded by former researchers at Google DeepMind and Meta, Mistral is known for its open, portable, customizable and cost-effective models that require fewer computational resources than other popular LLMs. All of Mistral AI's LLMs are foundation models, which means they can be fine-tuned and used in a wide-range of natural language processing tasks.

# Model Offerings

## Open-sourced models
The following models can be leveraged with no restrictions. They can also be leveraged for commercial use.

### Mistral 7B
- First Mistral model
- Outperforms Llama models with similar and slightly greater sizes
- Only requires 1 GPU

### Mistral 8X7B
- Sparse mixture of expert model (SMoE model)
- Based on Transformer architecture
- Model has 46B parameters but only requires 12.9B for inference
- Better performance for fast inference
- Outperforms LLaMa 2 (70B params) and GPT-3.5 in most benchmarks with 8X faster inference than LLaMa 2

## Optimized enterprise grade models
- Mistral Small is the best for low latency use cases.
- Mistral Medium is suitable for all language-based tasks that only require moderate reasoning such as Data Extraction, Summarization and Email writing.
- Mistral large the the flagship model for most sophisticated needs with advanced reasoning capabilities. 
    - Mistral Large approaches the performance of GPT4 
    - Has multi-lingual support in English, French, Spanish, German and Italian with a nuanced understanding for grammar and cultural context. (Outperforms LLaMA 2 70B in many multi-lingual tasks in the specified languages)
    - 32K context window (applies to all enterprise grade models)
    - Its precise instruction-following enables developers to design their moderation policies
    - It is natively capable of function calling. This, along with constrained output model, implemented on La Plateforme, enables application development and tech stack modernization at scale
- Lastly, Mistral offers an embedding model that can be used for many use cases such as clustering and classification. 

# Le Chat
- Chat interface to interact directly with Mistral Models
- <http://chat.mistral.ai>
- Free to use   