from collections import defaultdict

class ConversationMemoryService:

    def __init__(self):
        self.memory = defaultdict(list)

    def add_message(self, user_id: str, role: str, content: str):
        self.memory[user_id].append({
            "role": role,
            "content": content
        })

        # Mantém apenas as últimas 10 mensagens
        self.memory[user_id] = self.memory[user_id][-10:]

    def get_history(self, user_id: str):
        return self.memory[user_id]


conversation_memory_service = ConversationMemoryService()