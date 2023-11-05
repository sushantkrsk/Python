# for loop in list
# sppend means add in last
marks= [95,98,97]
for score in marks:
    print(score)

#
marks=[95,97,98]
marks.append(99)
print(marks)

# if we want to add something in starting or middle
marks=[95,97,98]
marks.insert(0,99)
print(marks)

# check whether 99 is present in marks or not
print(99 in marks)

# for finding length of strings

print(len(marks))