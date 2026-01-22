from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import http_request

ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.1"
)

agent = Agent(
    model=ollama_model,
    tools=[http_request]
)

response = agent("How are you?")
print(response)
