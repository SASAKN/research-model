# Libraries
from knowledge_base import KnowledgeBase, KnowledgeParser
from language_model import LanguageModel, ChatHistory
import re
import json

def turn_into_json(prompt):
    cleaned = re.sub(r"^```json\s*|\s*```$", "", prompt.strip())
    cleaned = cleaned.replace("'", '"')
    return json.loads(cleaned) 


if __name__ == "__main__":
    lm = LanguageModel()
    lm.chat([
    {
        "role": "system",
        "content": """Follow the rules below:

1. Output **only JSON** in the following format.
2. All fields must be included, even if empty (use [] or "").
3. Use **nested "process" arrays** to represent subtasks recursively.
4. Each task object contains:
    - "task": Task name or title (string)
    - "description": Task details (string)
    - "evidence": Array of evidence or references supporting the task (array of strings)
    - "explanation": Optional explanation why this task is needed (string)
    - "data": Optional data relevant for execution (object)
    - "process": Array of subtasks (array of task objects)
5. The top-level object contains:
    - "goal": Overall goal of the reasoning, according to user prompt (string)
    - "process": Array of top-level tasks (array of task objects)
6. You must follow this rule exactly as it is.
7. In this chat, you are an expert in

Example:

{
  "goal": "Goal of this reasoning according to user prompt",
  "process": [
    {
      "task": "1st Task",
      "description": "1st Task description",
      "evidence": ["Evidence1", "Evidence2"],
      "explanation": "Why this task is needed",
      "data": {},
      "process": [
        {
          "task": "1st Subtask",
          "description": "Subtask description",
          "evidence": [],
          "explanation": "",
          "data": {},
          "process": []
        }
      ]
    }
  ]
}
"""
    },
    {"role" : "user", "content" : "create operating system fundamentals"}
])

print(turn_into_json(lm.response["message"]["content"]))