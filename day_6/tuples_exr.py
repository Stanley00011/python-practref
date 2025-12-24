# Create an empty tuple
new_tpl = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Rafla', 'Willa', 'Jayla', 'Tedla')
brothers = ('Baf', 'Will', 'Jay', 'Ted')

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(f"Here are the siblings: {siblings}")

#How many siblings do you have?
print(len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.append("Jen")
family_members.insert(9,"Neja")
print(f"here is the fam{family_members}")

family_members = tuple(family_members)
print(f"here is the fam{family_members}")
print(type(family_members))

#Unpack siblings and parents from family_members

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("watermellon", "apple", "orange")
vegetables = ("spinach", "carrot", "cabbage")
animal_products = ("milk", "beef", "lamb")

food_stuff_tp = fruits + vegetables + animal_products 
print(food_stuff_tp)

# for fun
fruits , vegetables, animal_products = ("watermellon", "apple", "orange"), ("spinach", "carrot", "cabbage"), ("milk", "beef", "lamb")
print (fruits , vegetables, animal_products)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(f"the list{food_stuff_lt}")

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_lt_slimid = food_stuff_lt[3:5]
print(food_stuff_lt_slimid)

# Slice out the first three items and the last three items from food_staff_lt list
food_stuff_lt_sli3 = food_stuff_lt[0:3]
print(food_stuff_lt_sli3)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print ('Estonia' in nordic_countries)
print ('Iceland' in nordic_countries)