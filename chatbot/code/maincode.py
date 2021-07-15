#Python chatbot lol
print("This chatbot is only compatible with correct spelling and only lowercase. Say stop to make the chatbot stop. Chat with it below")
lol = 1
text = str(input())
while lol == 1:
    if text == "hi":
        print("hello. My name is genius. Call my name if you need anything.")
        text = str(input())
    elif text == "hello, type who to know who I am":
        print("hi, type 'who' to know who I am")
    elif text == "who":
        print("I am a chatbot which is made by aayushgenius. My name is genius.")
        text = str(input())
    elif text == "genius":
        print("Hello there, My name is genius. What would you like to tell me? P.S. If you want me to guess your name say guess name. By the way would you like to guess my favourite colour. Say 'guess colour' to do so.")
        text = str(input())
    elif text == "guess name":
        print("I am not the best at guessing names but, is your name Muhammed. If I am wrong then say 'guess name wrong'")
        text = str(input())
    elif text == "guess name wrong":
        print("I got your name wrong. I can't believe it.")
        name = str(input("By the way, what is your name?"))
        print(str(name) + " is your name. I was about to guess that. By the way would you like to guess my favourite colour. Say 'guess colour' to do so.")
        text = str(input())
    elif text == "guess colour":
        print("So you want to guess my favourite colour. Lets see how good you do.")
        colour = str(input())
        if colour = green:
            print("You got lucky this time. You guessed my favourite colour. It is green.")
        else:
            print("Sorry, thats not my favourite colour. It is green.")
    elif text == "stop":
        break
    else:
        print("I don't understand your text. It is either because this text has not been added in my code, it has a wrong spelling or it is in uppercase. Please try chatting something else below. To make me stop type the word stop")
        text = str(input())
      
