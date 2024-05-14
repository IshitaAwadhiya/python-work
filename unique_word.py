def count_unique_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Count the unique words using a set
    unique_words = set(words)
    
    # Return the count of unique words
    return len(unique_words)

# Example usage:
sentence = "😁Twinkle, twinkle little star. How I wonder what you are?” Lulu the Owl and Juno the Star become fast friends in this Super Simple version of one of the world’s most popular nursery rhymes."
print("Number of unique words:", count_unique_words(sentence))