symbol='s'
text='sims'
print(text.find(symbol))
print(text.find(symbol) + 1)
a= text.find(symbol, text.find(symbol) + 1) 

print(a)
 
#  if  text.count(symbol) >= 2 else None