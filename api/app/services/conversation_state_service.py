from app.repositories.conversation_state_repository import (
    get_state,
    set_state,
    clear_state
)

from app.repositories.conversation_state_repository import (
    get_state,
    set_state,
    clear_state,
    is_inactive
)

class ConversationStateService:

    def get(self, user_id):
        return get_state(user_id)

    def is_inactive(self, user_id: str, hours: int = 2):
        return is_inactive(user_id, hours)

    def set(self, user_id, state):
        set_state(user_id, state)

    def clear(self, user_id):
        clear_state(user_id)
    
    


conversation_state_service = ConversationStateService()