from conversations import Intent, Message, Conversation


def test_create_simple_conversation():

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

    assert conversation.participants == ["user", "bot"]
    assert len(conversation.messages) == 2