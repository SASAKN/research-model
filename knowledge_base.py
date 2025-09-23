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
            with open(self.filepath, 'r', encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        
    def save_knowledge_base(self):
        with open(self.filepath, 'w', encoding="utf-8") as file:
            json.dump(self.data, file,ensure_ascii=False, indent=4)
        
    def calc_next_id(self, type):
        if type not in self.data or not self.data[type]:
            return 0
        return max(item["id"] for item in self.data[type]) + 1

    def add(self, item, type):
        if type not in self.data:
            self.data[type] = []
        self.data[type].append(item)
        self.save_knowledge_base()
    
    def get(self, id, type):
        for item in self.data.get(type, []):
            if item.get("id") == id:
                return item
        return None
    
    def search(self, type=None, keyword=None):
        results = []
        types_to_search = [type] if type else self.data.keys()

        for t in types_to_search:
            for item in self.data.get(t, []):
                 if keyword is None or keyword in str(item.get("contents", "")):
                    results.append(item)
        return results
        

if __name__ == "__main__":
    kb = KnowledgeBase("sample_knowledge_base.json")

    # Knowledge Example
    # knowledge = KnowledgeParser(kb.get(0, "knowledges"))
    # kb.add({"id" : kb.calc_next_id("knowledges"), "type" : "graph_relation2", "contents" : ["知識グラフの中身配列になっている"], "evidence_text" : "Self-study and Online searching"}, "knowledges")

    kb.search(type="knowledges", keyword="知識グラフ")
    print(kb.search(keyword="知識グラフ"))