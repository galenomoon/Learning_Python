names = ["Guilherme Galeno", "Luana Santiago",
         "Gustavo Nascimento", "Isabella Letícia", "Apollo 11º"]

# "map(lambda name: ..., [Array])" === [Array].map.((name) => ...)
user_names = map(lambda name: f"@{name.lower().replace(' ', '')}", names)

print(f"\nNew list: {user_names}")
print(f"\nOps, sorry, the real new list: {list(user_names)}")
