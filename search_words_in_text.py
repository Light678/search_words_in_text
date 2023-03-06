import re


def find_words(text, word_to_find):
    # compile the regular expression pattern for the word
    pattern = re.compile(word_to_find)

    # search the text for the word
    match = pattern.search(text)

    # return the match if found, or None otherwise
    if match:
        return match.group()
    else:
        return None


def find_syllables(text, syllable_to_find):
    # compile the regular expression pattern for the syllable
    pattern = re.compile(r"\b\w*" + syllable_to_find + r"\w*\b")

    # search the text for the syllable
    matches = pattern.findall(text)

    # return the matches if found, or None otherwise
    if matches:
        return matches
    else:
        return None


# sample text
text = "Insert Text"

# search for the word(s)
word = find_words(text, "Insert Word")
if word:
    print(f"Word found: {word}")
else:
    print("Word not found.")

# search for the syllable(s)
syllables = find_syllables(text, "Insert syllable/letters")
if syllables:
    print(f"Syllables found: {syllables}")
else:
    print("Syllables not found.")
