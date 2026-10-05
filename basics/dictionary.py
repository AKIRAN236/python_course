data={1:55,2:66,3:77}
print(data)
print(type(data))
data={'kiran':55,'ravi':66,'siva':77}
print(data['ravi'])
print(data.get('siva'))
print(data.get('kiran','not found'))
data={'kiran':55,'ravi':66,'siva':77,'kiran':88}
print(data)
nums=[33,55,47]
keys={'kiran','ravi','siva'}
data=dict(zip(keys,nums))
print(data)
print(data.pop('ravi'))
del data['siva']
print(data)
