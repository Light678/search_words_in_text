import re


def search_words(text, words_to_find):
    # Compile the list of search words into a regular expression
    pattern = re.compile("|".join(words_to_find))

    # Search for matches in the text and print them out
    matches = pattern.findall(text)
    if matches:
        print("The following words were found:")
        for word in matches:
            print(word)
    else:
        print("No matches found.")


text = "insert Text"  # insert the Text
words_to_find = ["insert"]  # Insert words you want to find

search_words(text, words_to_find)

