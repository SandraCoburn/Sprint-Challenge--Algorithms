'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #find base case. lower or easiest case.
    #find the point to get closer to base case
    #recursive condition
    count = 0

    if len(word) < 2:
        return count
    #if "th" in word[0:2]:
    if word[0:2] == "th":
        count = count +1
        print("count:", count, word)
    word = word[1:]
    print("word: ", word)
    return count + count_th(word)
    
print("This many th's: ",count_th("monthlythlth"))
