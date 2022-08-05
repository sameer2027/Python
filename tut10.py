d1= {}
print(type(d1))
d2= {"harry":"burger","rohan":"fish","shubham":{"b":"maggie","l":"roti","d":"chicken"}}
print(d2)
d2["ankit"]= "junk food"
d2[420]= "kebab"
print(d2)
del d2[420]
print(d2)
d2.update({"leena":"cofee","sameer":"chai"})
print(d2)
print(d2.keys())
print(d2.items())
d3=d2.copy()
del d3["sameer"]
print(d3)
print(d2)
print(len(d2))