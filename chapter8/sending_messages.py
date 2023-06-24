txt_msgs = ['Hello World!', 'Hey bby, what\'s up?', 'How is the weather there?', 'You here?']
sent_messages = []

# def print_text_messages(list):
#     for i in list:
#         print(i)

# print_text_messages(txt_msgs)

def send_messages(list):
    while list:
        message = list.pop()
        print(message)
        sent_messages.append(message)

# send_messages(txt_msgs)
send_messages(txt_msgs[:])
print(txt_msgs)
print(sent_messages)



        