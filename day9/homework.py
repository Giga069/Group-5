                              #dav N1

x = [2, 4, 6, 2, 4, 7, 2, 9]
for i in range (3):  #ramdeni washalos
    x.remove(2)  #ra washalos
print(x) 
                              #dav N2

family = ["Sofo", "Zuka", "Giga"]
age = [33, 37, 15]
added_age =[10, 10, 10]

sentence_1 = "my mom's name is {}, she is {} yo.".format(family[0],age[0] + added_age[0])
print(sentence_1)

sentence_2 = "my name is {} and i am {} yo.".format(family[2],age[2] + added_age[2])
print(sentence_2)

sentence_3 = "my father's name is {}, he is {} years old.".format(family[1],age[1] + added_age[1])
print(sentence_3)



