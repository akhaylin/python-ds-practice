def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    letter_count = {}
    for ltr in phrase:
        count = phrase.count(ltr)
        letter_count[ltr] = count

    return letter_count
#TODO: use .get instead for o(n)