# conversations-python
Python version of my conversations library.

During my master studies I developed an interest in analysing and monitoring conversations between humans,
Conversational User Interfaces (CUIs) and humans, but also of CUIs with each other.

Because this needs a data format and I did not like the formats that e.g. Rasa used that that time,
I created different "conversation" libraries in languages that I used. The focus was on keeping it flexible and simple.
This repo contains the python version.

In my master thesis I used the format for live monitoring and alerting of the performance of the Rasa-LLM Hybrid CUI
that I used there as well as for in-depth analysis of the conversations.

Please note that this repo only contains the data format and a simple converter for Rasa Events in the utils module.

## Usage

### Install 

```bash
pip install git+ssh://git@github.com/Kai-Karren/conversations-python.git
```

## Install from Source

### Pyenv
Using a separate Python environment is recommended e.g. using pyenv

### Requirements

```bash
pip install build
```

### Build

```bash
python -m build
```

### Install

```bash
pip install --force dist/conversations-0.0.6-py3-none-any.whl
```

### Poetry

```bash
poetry install
```

## Documentation

The following provides a short overview of the basic concepts.

### Conversation

A conversation primarily consists of a list of messages between n participants.
Participants can be any combination of humans, chatbots, agents or how you want to call them.

Optionally, it is also possible to add labels and slots.

### Message

A message from a participant has a text. 
It is also possible to add an Intent, an intent ranking (list of intents), extracted entities, slots, labels and actions.

### Intent

An intent is a classification of an intention. E.g. "Good morning" -> greeting
This classical NLU term is seen a bit more general here because in this library it does not only refer to the user intention but
can also be assigned to non-human participants.

### Entity

An entity or named entity is a value from the text input that has been extracted in an entity extraction step. 
For example from the text "I live in New York and I am 25 years old" potential entities would be [New York](city) and [25](number).
This highly depends on what you are using for entity extraction e.g. Rasa or [spacy's entity extraction](https://spacy.io/usage/linguistic-features#named-entities) directly etc.

### Labels

Text labels can be assigned to each message or to the conversation. E.g. for attaching labels from humans or automated analyzers.

### Particpant

The library does not define how you want to name or classify your participants.
You can use their names, ids, "system", "agent", "user", "gpt_42", whatever.

### Action

An action is an abstraction of operations that may be interesting to attached to a message. It has been roughly inspired by Rasa's Actions but can also be used
to include tool calls and responses of LLM-based agents.
An action has a name and a content which is a dict which can be anything. 
