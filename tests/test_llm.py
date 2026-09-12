from app.llm import ask_llm

print("Testing LLM function...")
response = ask_llm("Explain RAG in exactly one sentence.") 
print("LLM responded!")   
print("Response:",repr(response))