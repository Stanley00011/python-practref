# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. 
# Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.


namess = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
rus = namess[-1]
ess = namess[-2]
nordic_countriess = namess[0:5]
print(rus, ess, nordic_countriess)

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, ru, es  = names
print(nordic_countries, ru, es)




