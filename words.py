def print_upper_words(words, startingwords):
    """   Print each word in the given array of strings on a seperate line uppercased if it starts with one of the words in startingwords."""

    for word in words:
         upperWord = word.upper()
         for letter in startingwords:
               if upperWord.startswith(startingwords.upper(letter)):
                      print(upperWord)
            
    
