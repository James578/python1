print ("Enjoy this fun quiz!")
a = input("What is your name?\n")
b = input("what is your favorite colour?\n")
c = input("What is your favorite sport? \n")
d = input("What is your subject? \n")
print ("Thank you,", a)
x = "hi"

f = open("answers.txt", "w")
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
