import os
print ("Enjoy this fun quiz!")
a = input("What is your name?\n")
b = input("what is your favourite colour?\n")
c = input("What is your favourite sport? \n")
d = input("What is your favourite subject? \n")
print ("Thank you,", a)
x = "hi"

for root, dirs, files in os.walk(os.getcwd()): #for every file in the current working directory
    for file in files: #for each file
        if file.endswith(".txt"): #if it ends with txt
             new = file.split("."); #split it by the dots e.g. answers.2.txt goes to a list [answers, 2, txt]
             fileno = int(new[1]) + 1 #get the file no and add one on to it
             fileno = str(fileno) #print the fileno as a string
             
f = open("answers."+fileno+".txt", "w")
f.write("Persons name: \n")
f.write(a)
f.write("\n")
f.write("colour: \n")
f.write(b)
f.write("\n")
f.write("sport:\n")
f.write(c)
f.write("\n")
f.write("subject:\n")
f.write(d)
f.write("\n")
f.close()
#I spent quite a while trying to work out how to get it to write to a certan line so that the old results are not wiped out if annoher person takes the test. I couldnt do it. It would be good if you did.
#This took me about 15 mins to make.
