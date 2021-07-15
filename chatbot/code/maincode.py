#Python chatbot 
print("This chatbot is only compatible with correct spelling and only lowercase. Say stop to make the chatbot stop. Chat with it below")
lol = 1
text = str(input())
while lol == 1:
    if text == "hi":
        print("hello")
        text = str(input())
    elif text == "stop":
        break
    else:
        print("I don't understand your text. It is either because this text has not been added in my code, it has a wrong spelling or it is in uppercase. Please try chatting something else below. To make me stop type the word stop")
        text = str(input())
      
