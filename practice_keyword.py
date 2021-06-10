#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Trevor Fournier & Kyle VanWinter
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Can take 3 arguments  for generated summarization (1, 2, 3) 1. the string in question  2. bool "split" of whether to generate or not  3. the "ratio" of how much to summarize
#Summarize can take 2 arguments for extractive summarization (1, 2)  1. the string in question  2. the "ratio" of how much to summarize
from gensim.summarization.summarizer import summarize 

#Keywords can take 2 arguments (1, 2) 1. string in question  2. "words" an int of how many keywords looking for
from gensim.summarization import keywords #Keywords can take 2 arguments (1, 2) 1. string in question  2. "words" an int of how many keywords looking for

#for getting the html from website
import urllib.request, urllib.error, urllib.parse
from urllib.request import urlopen, Request

import csv


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Summarization and Keywords Practice
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#text1 = "Hello, people from the future! Welcome to Normalized Nerd! I love to create educational videos on Machine Learning and Creative Coding. Machine learning and Data Science have changed our world dramatically and will continue to do so. But how they exactly work?... Find out with me. If you like my videos please subscribe to my channel."

#print(summarize(text1, split = True, ratio = .5)) #For example .5 summarizes it by half, the smaller the more summarrized it becomes.
#print(summarize(text1, split = True, word_count = 10)) #can also call a wordcount ish thing
#print("---")
#print(keywords(text1, words = 5, lemmatize = True))



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Reading website for all html
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#getting the html from the website
print("Input URL if enabled")
#url = input()
#url = 'https://www.nomadicmatt.com/travel-blogs/my-current-list-of-favorite-blogs/'
#url = 'https://www.farandwide.com/s/us-travel-bloggers-b735420bc9804272'
url = 'https://ofwhiskeyandwords.com/the-best-travel-blogs-of-2021/'

req = Request(url, headers = {"User-Agent": "Mozilla/5.0"})

#response = urllib.request.urlopen(url)
response = urllib.request.urlopen(req)
webContent = response.read()

print(type(webContent))
tmp = webContent.decode()

#print(webContent[0:300])



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Parsing
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def parse(theString):
    copy = 0
    htmlString = ''
    inMain = False
    count = 0
    for i in range(len(theString)):
        if(i < len(theString) - 7):
            count += 1
            if(theString[i] == "<" and theString[i+1] == "m" and theString[i+2] == "a" and theString[i+3] == "i" and theString[i+4] == "n" and theString[i+5] == ">"):
                inMain = True
            elif(theString[i] == "<" and theString[i+1] == "/" and theString[i+2] == "m" and theString[i+3] == "a" and theString[i+4] == "i" and theString[i+5] == "n" and theString[i+6] == ">"):
                inMain = False
            elif(theString[i] == "<" and theString[i+1] == "b" and theString[i+2] == "o" and theString[i+3] == "d" and theString[i+4] == "y"):
                inMain = True
            elif(theString[i] == "<" and theString[i+1] == "/" and theString[i+2] == "b" and theString[i+3] == "o" and theString[i+4] == "d" and theString[i+5] == "y" and theString[i+6] == ">"):
                inMain = False
        if(inMain == True):    
            if(theString[i] == "<"):
                if(i > 0 and i < len(theString) - 1):
                    if(theString[i+1]  != " " or theString[i-1] != " "):
                        copy += 1
                else:
                    copy += 1
            elif(theString[i] == ">"):
                if(i > 0 and i < len(theString) - 1):
                    if(theString[i+1] != " " or theString[i-1] != " "):
                        copy -= 1
                else:
                    copy -= 1
            elif(copy == 0):
                if(theString[i] == "\n"):
                    htmlString = htmlString + " "
                else:
                    htmlString = htmlString + str(theString[i])
    #print(keywords(htmlString, words = 14, lemmatize = True))
    pp = keywords(htmlString, words = 15, lemmatize = True)

    keyList = [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."] 
    tmp = 0
    keyCount = 0
    tmpstr = ""
    while(tmp < len(pp)):
        if(pp[tmp] != '\n'):
            tmpstr = tmpstr + pp[tmp]
        else:
            keyList[keyCount] = tmpstr
            tmpstr = ""
            keyCount += 1
        tmp += 1

    with open('keyword_list.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow({"Keywords"})
        writer.writerow({keyList[0]})
        writer.writerow({keyList[1]})
        writer.writerow({keyList[2]})
        writer.writerow({keyList[3]})
        writer.writerow({keyList[4]})
        writer.writerow({keyList[5]})
        writer.writerow({keyList[6]})
        writer.writerow({keyList[7]})
        writer.writerow({keyList[8]})
        writer.writerow({keyList[9]})
        writer.writerow({keyList[10]})
        writer.writerow({keyList[11]})
        writer.writerow({keyList[12]})
        writer.writerow({keyList[13]})
        #writer.writerow(data)


parse(tmp)
