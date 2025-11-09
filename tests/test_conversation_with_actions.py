from conversations import Intent, Message, Conversation, Action


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
                actions=[
                    Action(
                        name="initial_db_lookup",
                        content={
                            "response": {
                                "existing_user": False
                            }
                        }
                    )
                ]
            ),  
        ],
    )

    assert conversation.participants == ["user", "bot"]
    assert len(conversation.messages) == 2

    assert len(conversation.messages[1].actions) == 1
    
    action = conversation.messages[1].actions[0]

    assert action.name == "initial_db_lookup"
    assert not action.content["response"]["existing_user"]