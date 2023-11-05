# break and continue
# break- to break upto given name etc
students= ["ram", "shyam","kishan","vinit","akash"]

for student in students:
    if student =="kishan":
        break;
    print(student)   

# continue
# if we want to remove some name(etc) and then continue next one
for student in students:
    if student == "kishan":
        continue;
    print(student)    

