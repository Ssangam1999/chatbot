from typing import TypedDict, List

class ChatState(TypedDict):
    query: str
    docs: List
    answer: str