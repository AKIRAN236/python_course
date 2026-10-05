a=5
b=8
print(id(a))  # Prints the memory address of the variable 'a'
print(id(b))  # Prints the memory address of the variable 'b'
k=8
b=9
print(id(k))  # Prints the memory address of the variable 'k'
print(id(b))  # Prints the memory address of the variable 'b'
name='kiran'
name1='kiran'
print(id(name))  # Prints the memory address of the variable 'name'
print(id(name1))  # Prints the memory address of the variable 'name1'
#for a sentence the memory address will be different for each variable
sentence='kiran is a good boy'
sentence1='kiran is a good boy'
print(id(sentence))  # Prints the memory address of the variable 'sentence'
print(id(sentence1))  # Prints the memory address of the variable 'sentence1'