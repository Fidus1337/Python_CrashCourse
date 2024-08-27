"""
Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original 
list has retained its messages.
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

send_messages(messages_list[:], sent_messages)
print(sent_messages)
print(messages_list)  # as you see, we added to argument copy
