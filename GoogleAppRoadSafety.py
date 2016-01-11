__author__ = 'sunny_anand'
#import packages for the program
import csv
import operator
import nltk
from nltk.stem.porter import *
stemmer = PorterStemmer()
#open the file for reading : Corpus file after web crawling
file_content = open("Corpus.txt","r").read()
#Syntactic and Semantic Analysis of the raw data using NLTK
tagged = nltk.sent_tokenize(file_content.strip())
ab = nltk.pos_tag(tagged)
list_verbs = []
for sent in tagged:
    z = nltk.word_tokenize(sent)
    k = nltk.pos_tag(z)
    for i,j in k:
        if j == "VBG" or j =="VBN" or j == "VBD" or j == "VB" or j=="VBP" or j=="VBZ":
            list_verbs.append(i)
#list of Unique Verbs
uniqueWords = []
for i in list_verbs:
      if not i in uniqueWords:
          uniqueWords.append(i);

#Static Predictions
v1 = "Dangerous road ahead ! Remain alert !"
v2 = "Drive carefully as there is accident prone road ahead !"
v3 = "Caution ! Road ahead may be dangerous !"
v4 = "Alert ! Overpass ahead !"
v5 = "High risk accident area ahead ! Drive safe !"
v6 = "High risk accident area ahead ! Drive safe !"
#predicted value of the verbs
dict_pred = {'killed': 1,'kill':1, 'injured':2,'injure':2,'caused':3,'cause':3, 'left':4, 'struck':2,'strike':2, 'rolled':2,'roll':2, 'hurt':1,'hit':5, 'stolen':4,'stole':4 ,'driven':2,'drive':2,'involving':1,'involve':1, 'dead':3, 'hits':5,'hit':5 ,'sign':4, 'crashing':1,'crash':1,'Crash':1,'Strike':2,'accident':3,'die':3,
        'ejected':4,'eject':4, 'thrown':1,'throw':1,'crashed':2,'crash':2, 'fleeing':3,'flee':3, 'collide':1,'stalled':1,'stall':1, 'following':2, 'falling':3,'arrested':1,'Wreck':2,'wreck':2,'Killed': 1, 'Injured':2, 'Caused':3, 'Left':4, 'Struck':2, 'Rolled':2, 'Hurt':1,'Hit':5, 'Stolen':4, 'Driven':2, 'Involving':1,'involve':1, 'Dead':3, 'Hits':5, 'Sign':4, 'Crashing':1,
        'Ejected':4,'Eject':4, 'Thrown':1,'Throw':1,'Crashed':2, 'Fleeing':3, 'Collide':1,'collide':1,'Stalled':1,'stall':1, 'Following':2,'follow':2, 'Falling':3,'fall':3,'Arrested':1,'arrest':1}
##declaration of data
dict ={}
dict1 ={}
dict2={}
dict3={}
dict4={}
dict5={}
freq1={}
freq2={}
freq3={}
temp={}
cau_loc_counter = 0
list_cause_loc=[]
list_cause_loc_count = []
user_input = str()
remove = 0
count =0
flag = 0
#user input for the location
user_input =raw_input("Please enter a location name to find the the highest accident causing reasons and their safety measures")
#1.for the user input check if the corpus contains the location
f=open("Corpus.txt",'r')
for checked in f:
    if user_input in checked:
        flag=1
f.close()
#check for the SRL observation excel file
if flag ==1:
    with open('Book31.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                s = row['Sentences']#Put a check here that the sentence must have the same location
                k = row['Verb']
                m = row['SRL Cause']
                n= row['Nominal Cause']
                o= row['Location']
                p= row['Vehicle']
                q = row['Temporal']
                z= row["Nom"]
                count = count+1
                #check the cause of the accident from the role labeled sentences
                if m:
                    cause = m #if it is a srl cause
                    verb = k
                else:
                    cause = n #if it is a nominal cause
                    verb= z
                #print cause
                a=1
                dict5[s,verb,a]= cause,o,p
                if (p and o == user_input):
                #Type 1 category created where we find sentence ,verb,verb category,cause,location,vehicle
                    a=1#verb category is 1
                    dict2[s,verb,a]= cause,o,p
                #Finding the frequency of the cause location for type1 kind of accident information
                    new_string = cause + " "+o
                    list_cause_loc.append(new_string)
                    list_cause_loc_count.append(1)

                elif( not p and o==user_input) :
                #type2 category created where we find sentence,verb,verb category,cause location
                    b=2#verb category is 2
                    dict3[s,verb,b]=cause,o
                #Finding the frequency of the cause location for type1 kind of accident information
                    new_string = cause + " "+o
                    list_cause_loc.append(new_string)
                    list_cause_loc_count.append(1)
                else:
                    remove = remove+1
                s= str()
                k= str()
                l= str()
else:
    print "The location will be survyed and updated soon for accident prediction!!Thank you for your patience!!"
#2.then for all those SRL tagged sentences in the csv file do the processing and not for the entire corpus.(to be done)
# put the below code in if
if count == remove:
    print"No records of accident at this location."
else:
    seen = {}
    unseen = {}

    for x in list_cause_loc:
        if x in seen:
            seen[x] +=1
        else:
            seen[x] = 1
    #find the cause location from
    string1=  (max(seen.iteritems(), key=operator.itemgetter(1))[0])
    zzz= string1.split()
    causing_agent =  zzz[0]
    zzzz= dict_pred.keys()
    value_pred = 0
    for z4 in dict_pred.keys():
        if z4 == causing_agent:
            value_pred = dict_pred[z4]
            if value_pred ==1:
                print v1
            elif value_pred ==2:
                print v2
            elif value_pred ==3:
                print v3
            elif value_pred ==4:
                 print v4
            elif value_pred ==5:
                 print v5
            else:
                 print v6
#End of program--Sunny/Rumela