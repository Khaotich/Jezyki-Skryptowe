lista = ['Kasia', 'Basia', 'Marek', 'Darek']
lista.append('Józek')
lista.extend(['Ania','Basia'])
lista.sort()
print(lista[3])
print(lista[0],lista[1])
print(lista[-2],lista[-1])
lista.remove('Basia')
print(len(lista))
lista = tuple(lista)