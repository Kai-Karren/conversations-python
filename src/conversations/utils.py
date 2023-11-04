from .conversations import Message, Conversation, Intent

class ConversationBuilderForRasaEvents:

    def __init__(self, system_name="system"):
        self.conversations = {} # sender_id -> conversation
        self.system_name = system_name

    def add_rasa_event(self, event):
        """Adds a Rasa event to the builder.

        Args:
            event (dict): A Rasa event.
        """

        sender_id = event["sender_id"]

        if sender_id not in self.conversations:
            conversation = Conversation()
            self.conversations[sender_id] = conversation

        conversation = self.conversations[sender_id]

        if event["event"] == "user":
            conversation.add_message(
                Message(
                    participant="user",
                    text=event["text"],
                    intents=[Intent(name=event["parse_data"]["intent"]["name"], confidence=event["parse_data"]["intent"]["confidence"], classifier="rasa")],
                    intent_ranking=event["parse_data"]["intent_ranking"],
                    entities=event["parse_data"]["entities"]
                )
            )
        elif event["event"] == "bot":
            conversation.add_message(Message(participant=self.system_name, text=event["text"]))

    def add_rasa_events(self, event_list):
        """Adds a list of Rasa events to the builder.

        Args:
            event_list (list): A list of Rasa events.
        """

        for event in event_list:
            self.add_rasa_event(event)

    def get_conversations(self):
        """Returns the conversations.

        Returns:
            dict: A dictionary of conversations.
        """

        return self.conversations