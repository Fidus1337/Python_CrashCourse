"""
Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.
"""


def show_messages(messages: list):
    for msg in messages:
        print(msg)


messages_list = [
    'Hello! How are you?',
    'How are you doing?',
    'Could you help me today?',
    'Hi!'
]

show_messages(messages_list)
