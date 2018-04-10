"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    # open the file (read mode)
    # turn content content of file in one line string
    # split string by whitespace
    # convert back one line string - for loop - concatanate list into string
    # return string

    with open(file_path) as new_file:
        lines = new_file.read()
        split_lines = lines.split()

    return split_lines


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    # for loop through the range of text_string(from previous function)
    # put the i, i + 1 for key as tuple
    # value connects i + 2 for value as list (append to list)
    # when i = len(text_string - 2), value = None
    # return completed dictionary

    chains = {}

    for i in range(len(text_string)-2):

        key = (text_string[i], text_string[i + 1])

        if key in chains:
            chains[key].append(text_string[i + 2])
        else:
            chains[key] = [text_string[i + 2]]

    return chains


def make_text(chains):
    """Return text from chains."""
    # choose random first key from chains
    # add both items in key to words list
    # check if key is in chains, while key is in chains
        # assign random value from chains[key] to chosen_word
        # add chosen_word to words list
        # generate new key using key[1] and chosen_word
    # when key not in chain [words].join and return string

    words = []

    key = choice(chains.keys())
    for item in key:
            words.append(item)

    while key in chains:
        # print "key: ", key
        chosen_word = choice(chains[key])
        # print "chosen word: ", chosen_word
        words.append(chosen_word)
        # print words
        key = (key[1], chosen_word)

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)

print random_text

