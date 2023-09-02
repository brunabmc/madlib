"""
Practicing: string concatenation (how to put strings together)
suppose we want to create a string that says "Computer programming is so ______"
adj = "usefull" # some string variable 

print ("Computer programming is so " + adj)
print ("Computer programming is so {}".format(adj) )
print (f"Computer programming is so {adj}")
"""

adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
verb2 = input("Verb: ")
famous = input("Famous person: ")


madlib = f"Computer programming is so {adj1}! It makes me feel so {adj2},\
    that I can {verb2} like you are {famous}!"

print(madlib)
