# This is the start of my youtube analyzer website
# This is how to write python comments
# lets say that student_name= "Chandrala"
# these are variables and they have datatypes (string, int. booleans, etc)
# true and false statements are booleans
# characters are strings
# numbers are ints.
# functions are print(student_name) like f(x)
import string
from collections import Counter 

user_text=input("Enter the text:")
# This text will remove the punctuation and make everything lowercase using the char for char
cleaned_chars = [char if char not in string.punctuation else " " for char in user_text.lower()]
cleaned_text ="".join(cleaned_chars)

print("Cleaned text:",cleaned_text)
words= cleaned_text.split()
count=len(words)
print("This is your word count:", count)
#NEW WORD FREQUENCY ADDITION
word_frequencies= Counter(words)
print("\nWord Frequencies:")
for word,frequency in word_frequencies.items():
    print(f"-{word}:{frequency}")
print("Thank you for using! Have a great day!")