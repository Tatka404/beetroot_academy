fio = 'Ivchyk Tetiana Vasylivna'
print(len(fio))

data = fio.split()

fam = data[0]
name = data[1]
otch = data[2]

# =
fam2, name2, otch2 = fio.split()
print(fam2, name2, otch2)

print(f'your fam is {fam}, your name is {name}, your otch is {otch}')

print(fio.count('o'))
print(fio.count('e'))

fio_s = 'Ivchyk\nTetiana\tVasylivna'
print(fio_s)

# =
fio_s = f'{fam}\n{name}\t{otch}'
