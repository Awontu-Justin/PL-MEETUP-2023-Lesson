fruit=['Orange','Mango','Grapes','Lemon']#creates a  list called fruits
fruit.pop()#removes the last element in the list
fruit.append('Lemon')#adds lemon as the last elemnt of the list
food=['Garri','Biscuit','Eru','Okro']
fruit.extend(food)#Adds Food list to fruits list
fruit.remove('Orange')#removes orange from fruit
fruit.sort()#Sorts the list in ascending order
fruit.reverse()#reverses the fruit list
fruit.insert(0,'Orange')
fruit.clear()#clears the fruit list
print(food.count('Biscuit'))
print(fruit,food)
for x in fruit:
  print(x)