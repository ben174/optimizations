import random
from collections import OrderedDict, Counter
import timeit


card_faces = [ 'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King' ]

def sort_with_val_dict():
    """ Uses python's builtin sort, matching card faces to their corresponding
    sort orders in a dictionary.

    Should be fast, because the values are stored in a hash table for
    O(1) lookup. """
    card_values = {}
    for value, face in enumerate(card_faces):
        card_values[face] = value
    return sorted(deck, key=lambda i: card_values[i])

def sort_with_val_index():
    """ Uses python's builtin sort, matching card faces to their index in
    an ordered list.

    A bit slower, because the value has to be determined each time.
    """
    return sorted(deck, key=lambda i: card_faces.index(i))

def sort_with_dict_counts():
    """ Creates a dictionary of card faces and their counts, then constructs
    a ordered list of each card - repeated for its count.

    Should be very fast because and memory efficient, since we are simply
    storing counts for each unique value.
    """
    ret = []
    counts = {}
    for face in card_faces:
        counts[face] = 0
    for card in deck:
        counts[card] += 1
    for face in card_faces:
        ret.extend([face] * counts[face])
    return ret

def sort_ordered_dict():
    """ Uses Python's OrderedDict to hold a series of ordered buckets for each
    card. Then merges all the buckets into an ordered list.

    Not very fast or efficient.
    """
    ret = []
    ordered_cards = OrderedDict()
    for face in card_faces:
        ordered_cards[face] = []
    for card in deck:
        ordered_cards[card].append(card)
    for card_set in ordered_cards.values():
        ret.extend(card_set)
    return ret

def sort_counter():
    """ Uses Python's Counter to tally card counts into individual buckets for
    each card, then constructs a ordered list of each card - repeated for its
    count.

    Easiest to read, but has some overhead due to use of Counter.
    """
    ret = []
    counter = Counter()
    for card in deck:
        counter[card] += 1
    for face in card_faces:
        ret.extend([face] * counter[face])
    return ret

def sort_replace():
    """ Replaces each card face in the deck with its value, sorts the list,
    then switches them back to their card faces.

    Has to update the list in place twice, but leverages native sorting.
    """
    ret = deck[:]
    card_values = {}
    for value, face in enumerate(card_faces):
        card_values[face] = value
    for index, face in enumerate(ret):
        ret[index] = card_values[face]
    ret = sorted(ret)
    for index, value in enumerate(ret):
        ret[index] = card_faces[value]
    return ret

def bubble_sort():
    ret = deck[:]
    card_values = {}
    for value, face in enumerate(card_faces):
        card_values[face] = value
    for index, face in enumerate(ret):
        ret[index] = card_values[face]
    # manual bubble sort

    for index, value in enumerate(ret):
        ret[index] = card_faces[value]
    return ret



# constructs a very large deck of random, unsorted cards
deck = [random.choice(card_faces) for i in xrange(1000000)]

# take a baseline to assert against
baseline = sorted(deck, key=lambda i: card_faces.index(i))

start_time = timeit.default_timer()
assert sort_with_val_dict() == baseline
print('Sort Builtin (Dict vals): {}'.format(timeit.default_timer() - start_time))

start_time = timeit.default_timer()
assert sort_with_val_index() == baseline
print('Sort Builtin (Card index): {}'.format(timeit.default_timer() - start_time))

start_time = timeit.default_timer()
assert sort_with_dict_counts() == baseline
print('Sort Dict Counter: {}'.format(timeit.default_timer() - start_time))

start_time = timeit.default_timer()
assert sort_ordered_dict() == baseline
print('Sort Ordered Dict: {}'.format(timeit.default_timer() - start_time))

start_time = timeit.default_timer()
assert sort_counter() == baseline
print('Sort Counter: {}'.format(timeit.default_timer() - start_time))

start_time = timeit.default_timer()
assert sort_replace() == baseline
print('Sort Replace: {}'.format(timeit.default_timer() - start_time))

start_time = timeit.default_timer()
assert bubble_sort() == baseline
print('Bubble Sort: {}'.format(timeit.default_timer() - start_time))
