#1.Basic - Print all integers from 0 to 150.
for i in range(0,151):
    print(i)

#2.Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range  (5,1001):
    if x % 5 == 0:
        print(x)

#3.Counting, the Dojo Way
for j in range(0,101):
    if j % 5 == 0:
        print(j,"Coding")
for a in range(0,101):
    if a % 10 == 0:
        print(a,"Coding Dojo")

#4.Whoa. That Sucker's Huge
sum=0
count=0
for (num) in range(0,500001):
    if num % 2 != 0:
         sum=sum+num
         count=count+1
print (f" the entire sum of odd nubers between 0 and 500000 is {sum} and there is {count} values")

#5.Countdown by Fours
for x in range(2018,0,-4):
    if x>0:
        print(x)

#6.Flexible Counter
lowNum=3
highNum=15
mult=4

for x in range(lowNum,highNum):
    if x % mult==0:
        print(f" Mutiles of mult on the the range is {x}")




