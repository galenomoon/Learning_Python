# json/object => dictionary type <class 'dict'>

brother = {}
brother['name'] = "Gusta"
brother['age'] = 19

moonfriend = {'name': 'Lua', 'age': 19}
sister = dict([('name', 'Isa'), ('age', 13)])
cat = dict(zip(['name', 'age'], ['Apollo', 11]))

print(f"Todos são iguais?: {brother == moonfriend == sister == cat}\n")
print(f"Type: {type(brother)} | Output: {brother}")
print(f"Type: {type(moonfriend)} | Output: {moonfriend}")
print(f"Type: {type(sister)} | Output: {sister}")
print(f"Type: {type(cat)} | Output: {cat}")
