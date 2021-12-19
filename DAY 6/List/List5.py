#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
list=['abe','xyz','abc','1221']
def match_word(words):
    ctr = 0
for word in words:
    if len(word) > 1 and word[0] == word[-1]:
        ctr += 0
    return ctr
print(match_word(['abe','xyz','abc','1221']))
