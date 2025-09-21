import json

"""
This module is used by main function to load and save the kwnowledge base.
"""


# Knowledges Parser
class KnowledgeParser:

    def __init__(self, dict_data):
        self.data = dict_data
    
    def get_contents(self):
        return self.data.get("contents")
    
    def get_type(self):
        return self.data.get("type")
    
    def get_evidence_text(self):
        return self.data.get("evidence_text")
    
    def get_evidence_figure(self):
        return self.data.get("evidence_figure")

# Function Parser
class FunctionParser:

    def __init__(self, dict_data):
        self.data = dict_data
    
    def get_contents(self):
        return self.data.get("contents")
    
    def get_type(self):
        return self.data.get("type")
    
    def get_num_of_args(self):
        return self.data.get("num_of_args")
    
    def get_meaning_text(self):
        return self.data.get("meaning_text")
    
    def get_explanation_text(self):
        return self.data.get("explanation_text")

# Entire Knowledge Base Manager
class KnowledgeBase:

    def __init__(self, filepath="knowledge_base.json"):
        self.filepath = filepath
        self.data = self.load_knowledge_base()

    def load_knowledge_base(self):
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        
    def save_knowledge_base(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.data, file, indent=4)
    
    def get(self, id, type):
        for item in self.data.get(type, []):
            if item.get("id") == id:
                return item
        return None
        

if __name__ == "__main__":
    kb = KnowledgeBase("sample_knowledge_base.json")

    # Knowledge Example
    knowledge = KnowledgeParser(kb.get(0, "knowledges"))
    print(knowledge.get_contents())
    print(knowledge.get_type())
    print(knowledge.get_evidence_text())
    print(knowledge.get_evidence_figure())

    # Function Example
    function = FunctionParser(kb.get(0, "functions"))
    print(function.get_contents())
    print(function.get_type())
    print(function.get_num_of_args())
    print(function.get_meaning_text())
    print(function.get_explanation_text())
    