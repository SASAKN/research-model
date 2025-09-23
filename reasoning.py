import json
from language_model import LanguageModel, ChatHistory
from knowledge_base import KnowledgeBase, KnowledgeParser

system_prompt_1 = {
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
7. In this chat, you are an expert

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
""",
}

system_prompt_2 = {
    "role" : "system",
    "content" : """You are an AI assistant that outputs **only valid Python code**.  
Do not include any explanations, comments, or markdown.  
Return the Python program exactly as it should be executed.  
Always ensure that the code is syntactically correct and self-contained.
"""
}


class Reasoning:
    def __init__(self, json_data):
        # json_data は必ず JSON 文字列で渡す
        self.data = json.loads(json_data)

    def execute_process(self, process_list=None, level=0):
        if process_list is None:
            process_list = self.data["process"]
        indent = "  " * level
        for task in process_list:
            print(f"{indent}- Task: {task['task']}")
            lm = LanguageModel()
            lm.chat([{"role" : "user", "content" : f"Execute the following task : {task["task"]}"}])
            print(f"{indent}  Response: {lm.response['message']['content']}")
            print(f"{indent}  Description: {task['description']}")
            if task.get("process"):
                self.execute_process(task["process"], level + 1)


# JSON文字列を用意する
json_string = """
{'goal': 'Explain fundamental concepts of Operating Systems.', 'process': [{'task': 'Define Operating Systems', 'description': 'Describe what an Operating System (OS) is and its primary functions.', 'evidence': ['POSIX standard documentation', 'Operating Systems: Three Easy Pieces (book)'], 'explanation': 'An OS is a software layer that manages computer hardware and software resources, providing common services for computer programs. It acts as an intermediary between the user and the hardware.', 'data': {}, 'process': [{'task': 'Hardware Abstraction', 'description': 'Explain how the OS hides the complexity of hardware from applications.', 'evidence': ['Abstraction layers in programming', 'Virtual Machines'], 'explanation': 'The OS provides a simplified view of hardware, allowing applications to interact with the system without needing to know the specific details of each device. This is achieved through device drivers and APIs.', 'data': {'hardware_types': ['CPU', 'Memory', 'Storage', 'Input/Output Devices']}, 'process': [{'task': 'CPU Scheduling', 'description': 'Describe how the OS manages CPU time allocation among processes.', 'evidence': ['Multiprocessing concepts', 'Scheduling algorithms (FCFS, SJF, Priority, Round Robin)'], 'explanation': 'The OS decides which process gets to use the CPU at any given time, optimizing resource utilization and minimizing response times.', 'data': {'scheduling_algorithms': ['FCFS (First-Come, First-Served)', 'SJF (Shortest Job First)', 'Priority Scheduling', 'Round Robin']}, 'process': []}]}]}]}
"""
json_string = json_string.replace("'", '"')
reasoning = Reasoning(json_string)
print("Goal:", reasoning.data["goal"])
reasoning.execute_process()
