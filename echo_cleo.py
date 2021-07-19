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

from pytrends.request import TrendReq
import pandas as pd
import time



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Reading website for all html
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#getting the html from the website
url = ['https://www.nomadicmatt.com/travel-blogs/my-current-list-of-favorite-blogs/', 'https://www.farandwide.com/s/us-travel-bloggers-b735420bc9804272', 'https://ofwhiskeyandwords.com/the-best-travel-blogs-of-2021/']
outputs = ['Nomadic_Matt.txt', 'Far_and_Wide.txt', 'Of_Words_and_Whiskey.txt']

#this function will run for as many websites as we have in the url list. It does everything
#could probably be faster
def just_do_it(the_url, outputFile):
    key_words = 0
    req = Request(the_url, headers = {"User-Agent": "Mozilla/5.0"})
    response = urllib.request.urlopen(req)
    webContent = response.read()
    tmp = webContent.decode()



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
        pp = keywords(htmlString, words = 20, lemmatize = True)

        keyList = []
        tmp = 0
        keyCount = 0
        tmpstr = ""
        while(tmp < len(pp)):
            if(pp[tmp] != '\n'):
                tmpstr = tmpstr + pp[tmp]
            else:
                keyList.append(tmpstr)
                tmpstr = ""
                keyCount += 1
            tmp += 1


    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #checks for shite words that we decided upon
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        set1 = {'amp', '.', 'http', 'nbsp'}
        i = 0
        while(i < len(keyList)):
            set2 = {keyList[i]}
            if(set2.issubset(set1)):
                keyList.remove(keyList[i])
            else:
                i += 1
        key_wordZ = len(keyList) + 2



    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #Prints to the Excel keyword_list.csv     Must already have keyword_list.csv made
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        with open('keyword_list.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow({"Keywords"})
            i = 0
            while(i < len(keyList)):
                writer.writerow({keyList[i]})
                i +=1
            #for fun lol
            writer.writerow({"corona"})
            writer.writerow({"virus"})
        return key_wordZ

    key_words = parse(tmp)





    time.sleep(3)





    startTime = time.time()
    pytrend = TrendReq(hl='en-GB', tz=360)

    colnames = ["keywords"]
    df = pd.read_csv("keyword_list.csv", names=colnames)
    df1 = df["keywords"].values.tolist()
    df1.remove("Keywords")

    dataset = []
    dataset1 = []

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #Goes through and creates/stores data gotten from pytrend
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    for x in range(0,len(df1)):
        keys = [df1[x]]
        pytrend.build_payload(
        kw_list=keys,
        cat=0,
        #timeframe='2021-04-01 2021-06-01',
        timeframe='today 12-m', #'all' outputs monthly so it would be possible
        geo='GB')
        data = pytrend.interest_over_time()
        if not data.empty:
            data = data.drop(labels=['isPartial'],axis='columns')
            dataset.append(data)
        
        pytrend.build_payload(
        kw_list=keys,
        cat=0,
        #timeframe='2021-04-01 2021-06-01',
        timeframe='all', #'all' outputs monthly so it would be possible
        geo='GB')
        data1 = pytrend.interest_over_time()
        if not data1.empty:
            data1 = data1.drop(labels=['isPartial'],axis='columns')
            dataset1.append(data1)



    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #Prints the gotten values to the csv files
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    result = pd.concat(dataset, axis=1)
    extraResult = pd.concat(dataset1, axis = 1)
    result.to_csv('output.csv')
    extraResult.to_csv('outputAll.csv')



    executionTime = (time.time() - startTime)
    print('Execution time in sec.: ' + str(executionTime))





    time.sleep(3)





    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #reads data from the output.csv file and stores it in lists
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    bisty = ["."]*key_words
    busty = [0]*key_words
    with open('output.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        lineCount = 0
        for row in csv_reader:
            if(lineCount == 0):
                i = 0
                while i < len(bisty):
                    bisty[i] = row[i+1]
                    i += 1
            else:
                t = 0
                while t < len(busty):
                    busty[t] += int(row[t+1])
                    t += 1

            lineCount += 1

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #reads data from outputAll.csv file and stores it in lists
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    listy = ["."]*key_words
    lusty = [0]*key_words
    with open('outputAll.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        lineCountAll = 0
        for row in csv_reader:
            if(lineCountAll == 0):
                i = 0
                while i < len(listy):
                    listy[i] = row[i+1]
                    i += 1
            else:
                t = 0
                while t < len(lusty):
                    lusty[t] += int(row[t+1])
                    t += 1

            lineCountAll += 1
            


    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #outputs averages for last year and last 10 years
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    z = open(outputFile,"w+")
    mostIncrease = [{'name': '.', ':': 0}]*key_words
    mostPop = [{'name': '.', ':': 0}]*key_words


    z.write("Averages for Last Year: \n")
    pp = 0
    while pp < len(busty):
        busty[pp] = busty[pp] / (lineCount-1)
        z.write(f'{bisty[pp]}: \t\t{busty[pp]} \n')
        pp += 1


    z.write("\nAverages for Last 10 Year: \n")
    pp = 0
    while pp < len(lusty):
        lusty[pp] = lusty[pp] / (lineCountAll-1)
        mostPop[pp] = {'name': listy[pp], ':': busty[pp]}
        mostIncrease[pp] = {'name': listy[pp], ':': busty[pp]-lusty[pp]}
        z.write(f'{listy[pp]}: \t\t{lusty[pp]} \n')
        pp += 1

    def myFunc(e):
        return e[':']

    mostPop.sort(reverse = True, key=myFunc)
    mostIncrease.sort(reverse = True, key=myFunc)



    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #output sorted averages
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    z.write("\nSorted Avgs: \n")
    pp = 0
    while pp < len(mostPop):
        z.write(f'{mostPop[pp]}\n')
        pp += 1


    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #output sorted increases
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    z.write("\nSorted Increases in Pop: \n")
    pp = 0
    while pp < len(mostPop):
        z.write(f'{mostIncrease[pp]}\n')
        pp += 1


#this is what calls the whole function until no websites are left
ii = 0
while(ii < len(url)):
    just_do_it(url[ii], outputs[ii])
    ii += 1
    print('Finished: ' + str(ii) + '\n')