nums = [ 1, 5, 2, 2, 3, 4] 
print(len(nums))    #პრინტას რამდენი ელემენტია სიაში

surname = "yifiani"
print(len(surname)) #შვიდი სიმბოლოა გვარში
nums = [ 1, 5, 2, 2, 3, 4] 
set_of_nums = set(nums)
print(set(nums))        #აქრობს duplicatebs

letters =["a", "b", "c"]
letters += ["d"]
print(len(letters))       #4
print(letters)            #['a', 'b', 'c', 'd']


age = 10
age += 5
print(age) #15


str = "some text" #ცხრა სიმბოლოა რადგან space-იც ითვლება
x = len(str)
print(x)


nums = [1, 2, 3]
nums.append(4)       #append ამატებს ელმენტს ბოლოში
print(nums)

words =["giga",  "years old"]
words.insert(1,    "is 15")  #index=1 #რა ჩაჯდეს=is 15
print(words)


names = ["sofo", "zura"]
names.insert(1, "giga")
names.append("nika")
print(names)

x = 5 # integer
y = 2 # integer
z = x/y # float (implicit conversion)
 
x = input()
y = input()
print(x+y)

age = int(input())
print(type(age))

x = 15
print(type(x))

a = "ball"
b = "snow"
c = "foot"
print(b + a)

distance = 14 
units = "km"
print(distance + units)


distance = 14
units = "km"                         #<---დაიმახსოვრე.
print(str(distance) + units)


nums = [4, 5, 6]
msg = "numbers: {0} {1} {2}". format(nums[0], [1], [2])
print(msg)

family = ["ana", "deda", "tamari", "mama"]
fml = "{0}, {1}, {2}, {3}". format(family[0], family[1], family[2], family[3])
print(fml) 

names = ["Giga", "Nika", "Ana", "Tamara", "Zviada"]
nm = "my name is: {}".format(names[0])
print(nm)
nm =  "chemi dzmakaci saxelia: {}".format(names[1])
print(nm)
nm = "chemi zangi dis saxelia: {}".format(names[2])
print(nm)
nm = "chemi meore zangi dis saxelia: {}".format(names[3])
print(nm)
nm ="es vin chemi fexebia idk but his name is: {}".format(names[4])
print(nm)


a = "my name is: {}, my surname is: {}".format("Giga", "Yifiani")
print(a)


a = "my surname is {2}, my name is {0}, i love {1}".format("Giga","myself", "Yifiani")
print(a)


names = ["giga", "taso", "nika", "miyvars", "xinkali", "mwvadi", "shaurma", "sofo", "tbili", "zangi", "mkvleli", "mausi", "jacketi"]
name = "chemi saxelia {}".format(names[0])
print(name)
name = "chemi sauketeso megobaris saxxelia {}".format(names[2])
print(name)
name = "chemi sheyvarebulis saxelia {} <333".format(names[1])
print(name)
name = "me dzalian {} qartuli kerdzi {}, aseve dzan {} {}".format(names[3], names[4], names[3], names[6])
print(name)


words = ["miyvarxar", "shen"]
txt ="deda me {} dzalian dzalia {} <33".format(words[1], words[0])
print(txt)





















































