## Practice Sheet - 1 ####

## Q-2 ####

print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6 == 6)
a = 20; a+= 30; a%=3; print(a)
print(True * False)
print(True & False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
##False in ‘False’##
print(((True == False) or (False > True)) and (False <= True))

s = 5**9
print(s)

# Q-3 ####

s1 = 'Nice to have it'
s2 = 'here'
j = ' '.join([s1,s2])
print(j)

s1 = 'Nice to have it'
s2 = 'here'
k = s1 + ' ' + s2
print(k)

# Q-4 ####

a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

q = a[3][1][2][0]
print(q)

# Q-5 ####

a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a = a[:0] + [s1] + a[0:]; 
a = a[:7] + [s2] + a[7:]
print(a)

# Q-6 ###

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])


color_list_1.discard("Red")
print(color_list_1)

### OR ###
print(color_list_1-color_list_2)

# Q-7 ###

p = set(input())
j = set('abcdefghijklmnopqrstuvwxyz')
if j == p:
    print("It is a Pangram Sentence")
else:
    print("Not a Pangram Sentence")


#  Q-8 ###

z = eval('{0}+{0}{0}+{0}{0}{0}'.format(input("Enter the Number n:")))
print(z)

### Q-9 ###

g = input("Enter The Strings:")
list_value = g.split(",")
tuple_value = tuple(list_value)
print(g)
sorted_list = sorted(tuple_value)
print(sorted_list)

# Q-10 ###

d = {'Student':['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 
'Marks':[57,87,67,79]}
d['Marks']
m = max(d['Marks'])
h = d['Marks'].index(m)
print(d['Student'][a])



#################################


