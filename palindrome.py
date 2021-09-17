word = input("Please type word here: ")
palindrome_checker = None

# Test words
# palindrome_word = "bob"
# not_palindrome_word = "frank"

# Original idea, reversed gives an iterator and data location, not a string. You need to use .join with "" before to say join the words from reversed into a new string wherever there is a space
def isPalindromeJoin(word):
    reverse_word = "".join(reversed(word))
    if word == reverse_word:
        palindrome_checker = True
        print("According to the function using .join() and reversed(), this is a palindrome")
        print("Palindrome checker set to: " + str(palindrome_checker))
    else:
        palindrome_checker = False
        print("According to the function using .join(), and reversed(), this is not a palindrome")
        print("Palindrome checker set to: " + str(palindrome_checker))

isPalindromeJoin(word)

# Alternative, uses splice to say go from start (first value) to end (middle value) in reverse order (last value, -1)
def isPalindromeSplice(word):
    reverse_word = word[::-1]
    if word == reverse_word:
        palindrome_checker = True
        print("According to the function using splicing, this is a palindrome")
        print("Palindrome checker set to: " + str(palindrome_checker))
    else:
        palindrome_checker = False
        print("According to the function using splicing, this is not a palindrome")
        print("Palindrome checker set to: " + str(palindrome_checker))

isPalindromeSplice(word)