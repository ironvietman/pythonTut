# Commandline input
# getting input from commandline

def reverse(text):
    """Reverses a string."""
    return text[::-1]

def remove_punc(text):
    """Removes all puncutation, spaces, and case."""
    forbidden = (",","//","?","!","-","_","(",")","."," ")
    new_text = ""
    for char in text:
        if (char not in forbidden):
            new_text = new_text + char
    return new_text

def is_palindrome(text):
    """Checks if the string is a palindrome."""
    text = remove_punc(text)
    return text.upper() == reverse(text).upper()

something = raw_input("Enter text: ")
if is_palindrome(something):
    print "Yes, it is a palindrome"
else:
    print "No, it is not a palindrome"