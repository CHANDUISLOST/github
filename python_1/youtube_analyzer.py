# This is the start of my youtube analyzer website
# This is how to write python comments
# lets say that student_name= "Chandrala"
# these are variables and they have datatypes (string, int. booleans, etc)
# true and false statements are booleans
# characters are strings
# numbers are ints.
# functions are print(student_name) like f(x)
# I like cookies
import string
from collections import Counter 


while True:
    user_choice= input("Anything else to process: (yes/no)").lower()
    if user_choice == "yes":
        user_text=input("Enter the text:")
        # This text will remove the punctuation and make everything lowercase using the char for char
        def cleaning_text(user_text): #ndhbfvm
            cleaned_chars = [char if char not in string.punctuation else " " for char in user_text.lower()]
            cleaned_text ="".join(cleaned_chars)
            return cleaned_text

        final_cleaned_text =cleaning_text(user_text) # Calling the function
        print("Cleaned text:",final_cleaned_text)
        words= final_cleaned_text.split()
        count=len(words)
        print("This is your word count:", count)
        #NEW WORD FREQUENCY ADDITION
        word_frequencies= Counter(words)
        print("\nWord Frequencies:")
        for word,frequency in word_frequencies.items():
            print(f"-{word}:{frequency}")
        

    
    elif user_choice == "no":
        print("Thank you for using! Have a great day!") 
        break