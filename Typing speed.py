# -*- coding: utf-8 -*-
import time
string = "Python is a popular programming language. Python can be used on a server to create web applications. "
word_count = len(string.split())
border = '-+-'*10

def createbox():
    print(border)
    print()
    print('Enter the text fast with accuracy')
    print()

#main Calculation

while  1:
    t0 = time.time()
    createbox()
    print(string,'\n')
    inputText = str(input())
    t1 = time.time()
    lengthOfInput = len(inputText.split())
    accuracy = len(set(inputText.split()) & set(string.split()))
    accuracy = (accuracy/word_count)
    timeTaken = (t1 - t0)
    wordsperminute = (lengthOfInput/timeTaken)*60 


#result

    print('Total words \t :' ,lengthOfInput)
    print('Time used \t :',round(timeTaken,2),'seconds')
    print('Your accuracy \t :',round(accuracy,3)*100,'%')
    print('Speed is \t :' , round(wordsperminute,2),'words per minute')
    print("Do you want to retry? (Y / N)",end='')
    if input() == str("Y"):
        continue
    else:
        print('Thank you , bye bye .')
        time.sleep(1.5)
        break