from conversations import Intent, Message, Conversation

def test_to_json_and_back():

    greeting = Intent(name="greeting", confidence=0.9, classifier="rasa")

    conversation = Conversation(
        participants=["user", "bot"],
        messages=[
            Message(
                participant="user",
                text="Hello",
                intents=[greeting],
                intent_ranking=[greeting],
            ),
            Message(
                participant="bot",
                text="Hi there!",
                intents=[greeting],
                intent_ranking=[greeting],
            ),  
        ],
    )

    conversation_as_json = conversation.to_json()

    assert type(conversation_as_json) == str

    parsed_conversation = Conversation.from_json(conversation_as_json)

    assert parsed_conversation.participants == ["user", "bot"]

    