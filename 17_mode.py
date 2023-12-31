def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """



    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    max_value = max(count.values())
    for key in count:
        if count[key] == max_value:
            return key


    #get max of count values
    #loop through count keys
    #check count[key] equal max

    # return max(nums, key=nums.count)

    # highest_count = 0
    # highest_num = None

    # for num in count:
    #     if count[num] > highest_count:
    #         highest_count = count[num]
