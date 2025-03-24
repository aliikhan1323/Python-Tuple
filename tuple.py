#Define a Tuple(ordered, unchangeable, Allow Duplicate)
string=("Audi","Changan","Daihatsu","Honda","Nissan","Toyota", "Suzuki")
integer=(1,5,3,4,9)
float=(12.5, 3.5, 12.4, 99.66, 123.321)
bool=(True,False)
mix=("Audi",3,3.9,True)
print("This is tuple:")
print(string,integer,float,bool,mix)
#To display the data type using type() function
print("Display data type of tuple:")
print(type(mix))
#Display length of list using len() function.
print("This is length of tuple:")
print(len(bool))

#Access
print("Access Tuple Items:")
fruits=("apple","banana","mango","orange")
print(fruits[1]) #index
print(fruits[1:]) #
print(fruits[:3])
print(fruits[1:3]) #Positive range
print(fruits[-3:-1]) #Negative range
print(fruits[-1]) #Negative Index


#Check if "apple" exists in the tuple
fruits=("apple","banana","mango","orange") #Check if Item is exist.
if "apple" in fruits:
  print("Yes, 'apple' is in the fruits tuple")

#Change Tuple values:
print("Cahnge Tuple values:") #Convert the tuple into a list.
x = ("Face Book", "Instagram", "Whatsapp")
y = list(x)
y[1] = "Twitter"
x = tuple(y)
print(x)

#Add Items in Tuple.
print("Addition in Tuple:")
fruits=("apple","banana","mango") #Convert the tuple into a list, 
y = list(fruits)
y.append("orange") #using.append() function
fruits = tuple(y)
print(fruits)

#Add Tuple to a Tuple
print("Add Tuple into a Tuple:")
fruits = ("apple", "banana", "cherry") #Tuple+=Tuple1
fruit1 = ("orange",)
fruits+= fruit1 #using + function
print(fruits)

#Remove Items.
fruits = ("apple", "banana", "cherry") ##Convert the tuple into a list
fruit1 = list(fruits)
fruit1.remove("apple") #using.remove() function
fruits = tuple(y)


#Join two tuples
print("Join two Tuples:")
alphabets = ("a", "b" , "c")
numbers = (1, 2, 3)
print(alphabets)
print(numbers)
new = alphabets + numbers  #using + operator
print("Addition of two Tuples:",new)

#Multiply Tuples
print("Multiply the Tuples by 2:")
fruits = ("apple", "banana", "cherry")
fruits = fruits * 2
print(fruits)

#Find the maximum and minimum numbers in the tuple
print("Find the Maximum and Minimum Number:")
num = (10, 25, 5, 78, 90, 3, 55)
print("Maximum Number in list:", max(num)) #using max() function
print("Minimum Number in list:", min(num)) #using min() function