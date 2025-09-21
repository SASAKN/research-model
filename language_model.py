import ollama

response = ollama.chat(
    model="gemma3:4b",  # 使いたいモデル (事前に `ollama pull llama3` でダウンロード)
    messages=[
        {"role": "user", "content": "JSONで、タスクについてやることを並べて、タスク: 新しいOSを作る。"}
    ]
)

print(response["message"]["content"])
