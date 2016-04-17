"""Advanced skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    # Creating empty dict
    counted_letters = {}

    # If character is a letter,
    # add character to dict as key with count as value
    for character in phrase:
        if character.isalpha() == True:
            counted_letters[character] = counted_letters.get(character, 0) + 1

    # Creating a highest count to keep track of
    highest_count = 0

    # Creating empty list to add letter(s) to return to
    highest_count_letter = []

    # Iterating through dict of letters
    for letter in counted_letters:

        # In the case the count of the letter is higher than highest_count
        # Replace highest_count with the number value
        # Replace highest_count_letter with the letter key
        if counted_letters[letter] > highest_count:
            highest_count_letter = [letter]
            highest_count = counted_letters[letter]

        # In the case that the count of the letter equals highest_count
        # Append letter key to highest_count_letter
        elif counted_letters[letter] == highest_count:
            highest_count_letter.append(letter)

    return highest_count_letter


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    # Creating an empty set
    word_lengths = set()

    # Creating empty dictionary
    dict_word_lengths_and_words = {}

    # Adding all word lengths to set
    for word in words:
        word_lengths.add(len(word))

    # Adding word lengths as keys in dict
    for word_length in word_lengths:
        dict_word_lengths_and_words[word_length] = []

    # Adding words to list values in dict by their word lengths
    for word in words:
        if len(word) in dict_word_lengths_and_words:
            dict_word_lengths_and_words[len(word)].append(word)

    # Sort values in dict by alphabet
    for word_length in dict_word_lengths_and_words:
        dict_word_lengths_and_words[word_length].sort()

    # Creating empty list to add tuples to
    word_lengths_and_words = []

    # For each pair item in dict, add two item tuple to list
    for word_length in dict_word_lengths_and_words:
        word_lengths_and_words.append(
            (word_length,
            dict_word_lengths_and_words[word_length])
            )

    return word_lengths_and_words


#####################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
