import ollama

# Chat History Management Class
class ChatHistory:
    def __init__(self):
        self.messages = []
    
    def add_user_message(self, content):
        self.messages.append({"role": "user", "content": content})
    
    def add_assistant_message(self, content):
        self.messages.append({"role": "assistant", "content": content})

    def add_original_messages(self, original_messages):
        self.messages.append(original_messages)
    
    def get_messages(self):
        return self.messages

# Language Model Class
class LanguageModel:
    def __init__(self, model_name="gemma3:4b"):
        self.model_name = model_name
    
    def chat(self, messages):
        self.response = ollama.chat(
            model=self.model_name,
            messages=messages
        )
        return self.response["message"]
