#Python chatbot lol
from time import sleep
import time
print("This chatbot is only compatible with correct spelling and only lowercase. Say stop to make the chatbot stop. Say hi or hello to start the conversation.")
lol = 1
text = str(input())
while lol == 1:
    if text == "hi":
        print("hello. My name is genius. Call my name.")
        text = str(input())
    elif text == "hello":
        print("hi, type 'who' to know who I am")
    elif text == "who":
        print("I am a chatbot which is made by aayushgenius. My name is genius. Call my name. ")
        text = str(input())
    elif text == "genius":
        print("Hello there, My name is genius. What would you like to tell me? If you want me to guess your name say guess name. You can also say guess colour and guess gem")
        text = str(input())
    elif text == "guess name":
        print("I am not the best at guessing names but, is your name John, maybe Michelle. If I am wrong then say 'guess name wrong'. Otherwise guess my favourite colour by saying guess colour")
        text = str(input())
    elif text == "guess name wrong":
        print("I got your name wrong. I can't believe it.")
        name = str(input("By the way, what is your name?"))
        print(str(name) + " is your name. I was about to guess that. By the way would you like to guess my favourite colour. Say 'guess colour' to do so.")
        text = str(input())
    elif text == "guess colour":
        print("So you want to guess my favourite colour. Lets see how good you do.")
        colour = str(input("Write my favourite colour here."))
        if colour == "green":
            print("You got lucky this time. You guessed my favourite colour. It is green. Lets see if you get even luckier when I ask you about my favourite gem. Say guess gem")
            text = str(input())
        else:
            print("Sorry, thats not my favourite colour. It is green. Lets see if you can get luckier when I ask you about my favorite gem. Ask me guess gem. ")
            text = str(input())
    elif text == "guess gem":
        print("You've followed my instuctions over the last few text options. Thats good. Lets see how good you are at guessing my favourite gem.")
        gem = str(input("Write my favourite gem here."))
        if gem == "emerald":
            print("You guessed it!!! You are pretty good at guessing. Lets see your luck at riddles. Say answer riddle to see if you are lucky over there. ")
            text = str(input())
        else:
            print("Hard luck. It was the emerald. Wanna see how good you do at riddles. Say answer riddle.")
            text = str(input())
    elif text == "answer riddle":
        print("I know a few good ones  for them say answer riddle 2 or 3 for more. For now let me ask you this one.")
        print("What is so fragile that saying it breaks it.")
        riddle1 = str(input("Answer the first riddle here"))
        if riddle1 == "clock":
            print("Congratulations you got the correct answer it is a clock. Say answer riddle 2 for more. If you wanna hear a joke then say joke")
            text = str(input())
        else:
            print("Sorry, the answer is clock. Say answer riddle 2 to see if you can do better next time. Otherwise say joke for some funny ones. ")
            text = str(input())
    elif text == "answer riddle 2":
        print("Lets see if you can answer this one.")
        print("What is harder to catch when you run faster. Hint: Its 1 word")
        riddle2 = str(input("Answer the second riddle here"))
        if riddle2 == ("breath"):
            print("It is breath. You are right. Can you answer another one? Say answer riddle 3 for my last riddle.")
            text = str(input())
        else: 
            print("Oh no. You are wrong. It is breath. Say answer riddle 3 for my last riddle. ")
            text = str(input())
    elif text == "answer riddle 3":
        print("In for another riddle. I must warn you. It is the hardest")
        print("I have billions of eyes, yet I live in darkness. I have millions of ears, yet only four lobes. I have no muscle, yet I rule two hemispheres. What am I? Hint: I am made of 2 words")
        riddle3 = str(input("Answer the third riddle here"))
        if riddle3 == "human brain":
            print("Correct. You answered the hardest question!!! Say joke for some funny jokes")
            text = str(input())
        else:
            print("Sorry, thats wrong. It is human brain. It was the hardest question. say joke for some funny jokes. ")
            text = str(input())
    elif text == "joke":
        print("What’s the best thing about Switzerland? I don’t know, but the flag is a big plus.")
        sleep(0.75)
        print("What do you call bears with no ears?")
        sleep(0.75)
        print("b")
        sleep(0.75)
        print("What did the shark say when he ate the clownfish")
        sleep(0.75)
        print("This tastes funny")
        print("That all I've got for you today. You can visit my brother project AlphaQuad at https://github.com/QuantzLab/AlphaQuad. ")
        text = str(input())
    elif text == "stop":
        break
    else:
        print("I don't understand your text. It is either because this text has not been added in my code, it has a wrong spelling or it is in uppercase. Please try chatting something else below. To make me stop type the word stop")
        text = str(input())
      
