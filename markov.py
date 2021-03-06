"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_open = open(file_path)
    read_file = file_open.read()

    return read_file



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

    chains = {}
    words = text_string.split()

    for i in range(len(words)-2):
        
        key = words[i], words[i + 1]
        value = words[i+2]

        if value is None:
            
            value.append(words)
            chains[key] = value


        chains.setdefault(key, []).append(value)

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    key_list = list(chains)
       
    for i in range(len(key_list)):
       
        first_word = key_list[i][0]
        second_word = key_list[i][1]
        chosen_word = choice(chains[(first_word, second_word)])

        while chosen_word is not None:
            key_word = (second_word, chosen_word)
            words.append(chosen_word)
            final_word = choice(chains[key_word])

    words.append(final_word)

               
        # if second_word in key_list[0] and chosen_word in key_list[1]:
        #     last_word = choice(chains[(second_word, chosen_word)])

        # words.append(second_word) 
    # words.append(first_word)
    # words.append(last_word)
    # import pdb; pdb.set_trace()

    return " ".join(words)




input_path = "green-eggs.txt"


# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
