# Libraries
from knowledge_base import KnowledgeBase, KnowledgeParser
from language_model import LanguageModel, ChatHistory

if __name__ == "__main__":
    print(KnowledgeParser(KnowledgeBase("sample_knowledge_base.json").get(0, "knowledges")).get_contents())