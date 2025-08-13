#bitwise operator are used to perform bitwise calculation.these are applicable only for integer and boolean type only
#if we try to use any  other type then pvm (python virtual machine) gives you error. boolean is like T=1/F=0
'''
types of bitwise
and(&)-agar dono bits 1 hai tabhi result 1 hoga otherwise 0
a=3 #011    011
b=2 #010    010
c=a&b #010  010
print(c)
output : 2 
or(|)-agar koi ek bhi bit 1 hai to result 1 hoga otherwise 0
a=3 #011
b=2 #010
c=a|b #011
print(c)
output: 3
xor(^)- agar ek 1 aur dusra 0 tabhi ye result 1 dega agar dono 1 ya dono 0 to result 0
a=3 #011
b=2 #010
c=a^b #001
print(c)
output: 1
not(~)- ye binary bits ko ulta kar deta hai formula= -(a+1) jaha 1 hoga vaha 0 ho jayega jaha 0 hoga vaha 1
print(~3) #00000011 (8 bits hone chahiye na)
output: -4 #11111100 (ye 252 ka bhi binary hai aur -4 ka bhi kyuki 0-255 tak 8 bit binary hota hai ab isme hota kya hai
ki jo -1 ka binary hoga vhi 255 ka hoga aur jo -2 ka hoga vhi -254 ka hoga and so oon jise -5 ka janna hai toh 255-5=250
toh jo 250 ka hoga vhi -5 ka hoga)
'''