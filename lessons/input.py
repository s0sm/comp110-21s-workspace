"""a program to demonstrate user input and variables."""

#name: str = input("Who are you? ")

#print("Wow, " + name + ", you rock!")
#print(name + " have a great day!")

i=0

def double_letters(word):
    while i < (len(word)-1):
        if word[i].equals(word[i+1]):
            return True;
        else:
            return False;