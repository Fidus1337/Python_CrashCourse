"""
Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly
"""


def send_messages(messages_to_send: list, sent_messages: list):
    """For sending messages"""
    # printing the messages (imitating that we are sending messages)
    for msg in messages_to_send:
        print(msg)
    while messages_to_send:  # adding messages_to_send to sent_messages
        sent_messages.append(messages_to_send.pop())


sent_messages = []
messages_list = [
    'Hello! How are you?',
    'How are you doing?',
    'Could you help me today?',
    'Hi!'
]

send_messages(messages_list, sent_messages)
print(sent_messages)
print(messages_list)
