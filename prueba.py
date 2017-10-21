words_map = []
words = {}
index = 0

for i in range(2):
    # print i
    # Esperar resultados de cada nodo
    data = []
    if i == 0:
        data = ["Esto","es","la","prueba","del","millon","de","dolares","xD"]  # comm.recv(source=i)
    else:
        data = ["Ala","cuack!","bar!!","jajajaj","mera","gueva","los","dolares","no","pasaron","la","prueba"]
    uniques = []
    for word in data:
        if word in words:
            uniques.append(words.get(word))
        else:
            words.update({word: index})
            uniques.append(index)
            index += 1
    words_map.append(uniques)

print words_map
print "----"
print words