import streamlit as st
st.write("""
# 5. The zip() function
The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.
_Example_
```mixed
colour = [“red”, “yellow”, “green”]
fruits = [‘apple’, ‘banana’, ‘mango’]
for colour, fruits in zip(colour, fruits):
print(colour, fruits)
```
_Output_
```mixed
red apple
yellow banana
green mango
```
The zip() function can also be used for combining two lists into a dictionary. This method can be really helpful while grouping data from the list.
_Example_
```mixed
students = [“Rajesh”, “kumar”, “Kriti”]
marks = [87, 90, 88]
dictionary = dict(zip(students, marks))
print(dictionary)
```
_Output_
```mixed
{‘Rajesh’: 87, ‘kumar’: 90, ‘Kriti’: 88}
```
""")