from conversations import conversations

def test_to_json_and_back():

    greeting = conversations.Intent(name="greeting", confidence=0.9, classifier="rasa")

    conversation = conversations.Conversation(
        participants=["user", "bot"],
        messages=[
            conversations.Message(
                participant="user",
                text="Hello",
                intents=[greeting],
                intent_ranking=[greeting],
            ),
            conversations.Message(
                participant="bot",
                text="Hi there!",
                intents=[greeting],
                intent_ranking=[greeting],
            ),  
        ],
    )

    conversation_as_json = conversation.to_json()

    assert type(conversation_as_json) == str

    parsed_conversation = conversations.Conversation.from_json(conversation_as_json)

    assert parsed_conversation.participants == ["user", "bot"]

    