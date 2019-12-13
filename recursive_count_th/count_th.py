'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # initialize total_count of "th" in word
    total_count = 0

    # base case
    # if word is less than 1 letter
    if len(word) <= 1:
        return 0

    # go through string 'word'
    # check for "t" in the first pos and "h" in the second pos 
    # if word[0] and word[1] is "th" respectively, add 1 to total_count
    # and call recursive function to start at word[1:] 
    # else if "th" is not found, start at word[1:] until length <= 1
    if word[0] == "t" and word[1] == "h":
        total_count += 1
        return total_count + count_th(word[1:])
    else:
        return count_th(word[1:])
