"""Skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different::

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    # Returns set of items in words
    return set(words)


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    # Returns intersection of set of items1 and set of items2
    return set(items1) & set(items2)


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    # Creates empty dict
    count_words = {}

    # Split phrase by space which returns a list
    # Iterates through the list
    # Use .get method to add key of word and 
    # value of + 1 for each instance of word
    for word in phrase.split():
        count_words[word] = count_words.get(word, 0) + 1

    #returns dictionary of words : counts
    return count_words


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    # Dictionary of English to pirate
    # Not sure if the table in the doctest can be auto added to a dict?
    # I ended up manually adding the pairs
    english_pirate_dict = {
        "sir" : "matey",
        "hotel" : "fleabag inn",
        "student" : "swabbie",
        "man" : "matey",
        "professor" : "foul blaggart",
        "restaurant" : "galley",
        "your" : "yer",
        "excuse" : "arr",
        "students" : "swabbies",
        "are" : "be",
        "restroom" : "head",
        "my" : "me",
        "is" : "be",
        }

    # Initiate empty string
    pirate_phrase = ""

    # For word in phrase, if word exists as key in dict, add value
    # Else add word
    for word in phrase.split():
        if word in english_pirate_dict:
            pirate_phrase = "%s %s" %(
                pirate_phrase, 
                english_pirate_dict[word]
                )
        else:
            pirate_phrase = "%s %s" %(
                pirate_phrase, 
                word
                )

    # Return pirate phrase without initial space
    return pirate_phrase.strip()


def sort_by_word_length(words):
    """Given list of words, return list of ascending (len, [words]).

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- the length
    of the words for that word-length, and the list of words of
    that word length.

    For example::

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]
    """

    # Create empty dictionary
    dict_by_word_length = {}

    # For each word in words
    # Either add length of word as key into dict with word as value
    # Or append word to value if key already in dict
    for word in words:
        if len(word) not in dict_by_word_length:
            dict_by_word_length[len(word)] = [word]
        else:
            dict_by_word_length[len(word)].append(word)

    # Create empty list
    list_by_word_length = []

    # For each key value pair in dict, turn into tuple in list
    for key in dict_by_word_length:
        list_by_word_length.append((key, dict_by_word_length[key]))

    # Return list of tuples
    return list_by_word_length


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    # Removing duplicate number in numbers
    numbers = set(numbers)

    # Creating empty list
    number_with_pair = []
 
    # Appending numbers to list if numbers have a -number also in the list
    for number in numbers:
        if ((0 - number) in numbers):
            number_with_pair.append(number)

    # Sorting list of numbers
    number_with_pair = sorted(number_with_pair)

    # Creating a pairs list to add final pairs to
    sum_zero_pairs = []

    # For sorted list of numbers, add number and -number to pairs list
    for index in range(0 , (len(number_with_pair) / 2)):
        sum_zero_pairs.append([number_with_pair[index], -number_with_pair[index]])

    # For the case where there's a zero
    for number in number_with_pair:
        if number == 0:
            sum_zero_pairs.append([0 , 0])

    # Returns list of pairs
    return sum_zero_pairs


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # Creating chained names
    chained_names = [names.pop(0)]

    # Creating an empty set
    set_first_letters = set()

    # Adding all first letters to set
    for name in names:
        set_first_letters.add(name[0])

    # Creating an empty dict
    dict_by_first_letter = {}

    # Creating a dict with key of first letter with empty lists as values
    for letter in set_first_letters:
        dict_by_first_letter[letter] = []

    # Adding each name to value lists based on first letter
    for name in names:
        dict_by_first_letter[name[0]].append(name)

    # While last letter of last word in chain is in first letter dict
    while chained_names[-1][-1] in dict_by_first_letter:

        # Creating a variale to represent that letter to make code more readable
        letter = chained_names[-1][-1]

        # Putting in a way to break when no words can be found
        if dict_by_first_letter[letter] != []:

            # Adding first word at index 0 of value of letter key
            # Then removing that word from dictionary
            chained_names.append(dict_by_first_letter[letter][0])
            dict_by_first_letter[letter].pop(0)

        else:
            break

    return chained_names


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
