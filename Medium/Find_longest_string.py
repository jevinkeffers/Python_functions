def longest(lst):
    word_len = []
    for i in lst:
        word_len.append((len(i), i))
    word_len.sort()
    return word_len[-1][1]


print(longest(["You", "are", "soooo", "beautiful", "to", "meeee"]))

#Solved, helped by https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-8.php