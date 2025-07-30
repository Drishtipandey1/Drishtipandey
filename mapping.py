# python me mapping mtlab ki koi ek opertion ko kisi iterable jaise (list,tuple) ke sabhi element pe ek hi operation apply kar dena 

number = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x**2, number))
print(squared_numbers)

#mapping ek data structure hai jo key-value pairs ko store karta hai yah dictionaries ki tarah kaam karta hai yaha
#aap key ka istemaal karke value ko access kar sakte hai jaise
my_dict = {"apple": 1, "banana": 2, "cherry": 3}
print(my_dict["banana"]) 
