#Write a Python program that accepts a word from the user and reverse it.
a = input("Enter input a word: ")
i = len(a)
k = i+1
w = "*"
for j in range(1,k):
    l = i-j
    w = w + a[l]
print(w)