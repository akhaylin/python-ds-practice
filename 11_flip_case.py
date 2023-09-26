def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

#FIXME: use swapcase
    swapped = ""

    for ltr in phrase:
        if ltr.lower() == to_swap.lower():
            if(ltr.isupper()):
                swapped += ltr.lower()
            else:
                swapped += ltr.upper()
        else:
            swapped += ltr

    return swapped

