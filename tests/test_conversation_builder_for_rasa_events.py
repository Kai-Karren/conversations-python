from conversations.utils import ConversationBuilderForRasaEvents


def test_create_conversation_builder_for_rasa_events():

    conversation_builder = ConversationBuilderForRasaEvents()

    assert conversation_builder.conversations == {}
    assert conversation_builder.system_name == "system"


def test_add_rasa_event():

    conversation_builder = ConversationBuilderForRasaEvents()

    event = {
        "event": "user",
        "text": "Hello",
        "parse_data": {
            "intent": {
                "name": "greeting"
            },
            "intent_ranking": [
                {
                    "name": "greeting",
                    "confidence": 0.9
                }
            ],
            "entities": []
        },
        "sender_id": "user"
    }

    conversation_builder.add_rasa_event(event)

    assert len(conversation_builder.conversations) == 1
    assert "user" in conversation_builder.conversations

    conversation = conversation_builder.conversations["user"]

    assert conversation.participants == ["user"]
    assert len(conversation.messages) == 1

    message = conversation.messages[0]

    assert message.participant == "user"
    assert message.text == "Hello"
    assert message.intents == ["greeting"]
    assert message.intent_ranking == [
        {
            "name": "greeting",
            "confidence": 0.9
        }
    ]
    assert message.entities == []


def test_add_rasa_events():

    conversation_builder = ConversationBuilderForRasaEvents()

    event_list = [
        {
            "event": "user",
            "text": "Hello",
            "parse_data": {
                "intent": {
                    "name": "greeting"
                },
                "intent_ranking": [
                    {
                        "name": "greeting",
                        "confidence": 0.9
                    }
                ],
                "entities": []
            },
            "sender_id": "user"
        },
        {
            "event": "bot",
            "text": "Hi there!",
            "parse_data": {
                "intent": {
                    "name": "greeting"
                },
                "intent_ranking": [
                    {
                        "name": "greeting",
                        "confidence": 0.9
                    }
                ],
                "entities": []
            },
            "sender_id": "user"
        }
    ]

    conversation_builder.add_rasa_events(event_list)

    assert len(conversation_builder.conversations) == 1
    assert "user" in conversation_builder.conversations

    conversation = conversation_builder.conversations["user"]

    assert conversation.participants == ["user", "system"]
    assert len(conversation.messages) == 2

    message = conversation.messages[0]

    assert message.participant == "user"
    assert message.text == "Hello"
    assert message.intents == ["greeting"]
    assert message.intent_ranking == [
        {
            "name": "greeting",
            "confidence": 0.9
        }
    ]
    assert message.entities == []

    message = conversation.messages[1]

    assert message.participant == "system"
    assert message.text == "Hi there!"
    assert message.intents == []
    assert message.intent_ranking == []
    assert message.entities == []


def test_get_conversations():

    conversation_builder = ConversationBuilderForRasaEvents()

    event_list = [
        {
            "event": "user",
            "text": "Hello",
            "parse_data": {
                "intent": {
                    "name": "greeting"
                },
                "intent_ranking": [
                    {
                        "name": "greeting",
                        "confidence": 0.9
                    }
                ],
                "entities": []
            },
            "sender_id": "user"
        },
        {
            "event": "bot",
            "text": "Hi there!",
            "parse_data": {
                "intent": {
                    "name": "greeting"
                },
                "intent_ranking": [
                    {
                        "name": "greeting",
                        "confidence": 0.9
                    }
                ],
                "entities": []
            },
            "sender_id": "user"
        }
    ]

    conversation_builder.add_rasa_events(event_list)

    conversations = conversation_builder.get_conversations()

    assert len(conversations) == 1
    assert "user" in conversations

    conversation = conversations["user"]

    assert conversation.participants == ["user", "system"]
    assert len(conversation.messages) == 2

    message = conversation.messages[0]

    assert message.participant == "user"
    assert message.text == "Hello"
    assert message.intents == ["greeting"]
    assert message.intent_ranking == [
        {
            "name": "greeting",
            "confidence": 0.9
        }
    ]
    assert message.entities == []

    message = conversation.messages[1]

    assert message.participant == "system"
    assert message.text == "Hi there!"
    assert message.intents == []
    assert message.intent_ranking == []
    assert message.entities == []
