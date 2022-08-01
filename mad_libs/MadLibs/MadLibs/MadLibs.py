youtuber = "TheVR"

#one way to concatenate strings in Python is to use '+'
print("Subscribe to " + youtuber)

#an other method is using curly braces, then the .fromat() method
print("Subscirbe to {}".format(youtuber))

#the third version of this is much like the so called string interpolation from C#, but instead of using '$' at the start of the string,
#we use 'f'. The name of this is and "F" string.
print(f"Subscirbe to {youtuber}")

#From here we will take a look at getting user inputs from the console.

adj = input('Adjective: ')
verb1 = input('Verb: ')
verb2 = input('Verb: ')
famous_person = input('Famous person: ')

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}."

print(madlib)
