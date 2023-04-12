import openai
import json

class chatGPT:
    def __init__(self, api_key, model):
        openai.api_key = api_key
        self.model = model
        
        self.messages = list()
        self.responses = list()
        self.completions = list()        

        self._file_default = "chatbot_data.json"
        
    def message_post(self, prompt):
        self.messages.append({"role": "user", "content": prompt})
        return self.messages

    def generate_response(self):
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        response = completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": response})
        
        self.response = response
        self.responses.append(response)
                
        self.completion = completion
        self.completions.append(completion)
        
        return self.response

    def reset(self):
        self.messages = list()
        self.responses = list()
        self.completions = list()        
        
    def save_data(self, file_path = None):
        data = {
            "responses": self.responses,
            "completions": self.completions,
            "messages": self.messages
        }
        
        if file_path is None:
            file_path = self._file_default
        
        with open(file_path, "w") as f:
            json.dump(data, f)
            
    def load_data(self, file_path = None):
        if file_path is None:
            file_path = self._file_default
        
        with open(file_path, "r") as f:
            data = json.load(f)
            responses = data["responses"]
            completions = data["completions"]
            messages = data["messages"]
            return responses, completions, messages
    
    def load_messages(self, messages):
        self.messages = messages
    def list_messages(self):
        # list all messages
        for e in self.messages:
            print(f"role: {e['role']}")
            print(f"content:\n{e['content']}")
            print(f"\n")