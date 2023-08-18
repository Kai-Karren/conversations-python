from conversations import conversations


def test_create_simple_conversation():

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

    assert conversation.participants == ["user", "bot"]
    assert len(conversation.messages) == 2