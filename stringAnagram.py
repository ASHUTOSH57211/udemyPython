s1 = input("Enter a astring ")
s2 = input("Enter second string ")
count = 0
for s in s1:
    if s in s2:
        count += 1
if len(s1)==len(s2) and count == len(s1):
    print("Strings are anagram")
else:
    print("Strings are not anagram")