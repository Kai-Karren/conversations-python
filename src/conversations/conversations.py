import uuid
from dataclasses import dataclass, field
from typing import List


@dataclass
class Intent:
    name: str 
    confidence: float
    classifier: str

@dataclass
class Entity:
    entity: str 
    value: str
    confidence: float
    extractor: str

@dataclass
class Label:
    name: str
    confidence: float
    assigned_by: str

@dataclass
class Slot:
    name: str
    value: str

@dataclass
class Message:
    id: str = str(uuid.uuid4())
    participant: str = ""
    text: str = ""
    timestamp: str = ""
    intents: List[Intent] = field(default_factory=list)
    intent_ranking: List[Intent] = field(default_factory=list)
    entities: List[Entity] = field(default_factory=list)
    slots: List[Slot] = field(default_factory=list)
    labels: List[Label] = field(default_factory=list)

@dataclass
class Conversation:
    id: str = str(uuid.uuid4())
    timestamp: str = ""
    participants: List[str] = field(default_factory=list)
    messages: List[Message] = field(default_factory=list)
    slots: List[Slot] = field(default_factory=list)
    labels: List[Label] = field(default_factory=list)

    def add_message(self, message: Message):

        self.messages.append(message)

        if message.participant not in self.participants:
            self.participants.append(message.participant)