# -*- coding: utf-8 -*-
import os, sys, time
import numpy as np
from mpi4py import MPI
from Jaccard import *
from kmeans import *
from Dictionary import *


timeIni = time.time()
words = {}
index = 0
words_map = []
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.rank

if len(sys.argv) != 3:
    print "Error!"
    print "Usage: " + sys.argv[0] + " PATH " + "NumberOfClusters"
    exit(-1)

documents = str(sys.argv[1])
clusters = str(sys.argv[2])

if rank == 0:
    core = 0
    for filename in os.listdir(documents):
        core += 1
        # print core
        if core == size:
            core = 0
            for i in range(size-1):
                if i != 0:
                    # print i
                    # Esperar resultados de cada nodo
                    data = comm.recv(source=i)
                    uniques = []
                    for word in data:
                        if word in words:
                            uniques.append(words.get(word))
                        else:
                            words.update({word: index})
                            uniques.append(index)
                            index += 1
                    words_map.append(uniques)
        else:
            # enviar a cada nodo un libro
            comm.send(documents + filename, dest=core)
    if core > 0:
        for i in range(core):
            if i != 0:
                # print i
                # Esperar resultados de cada nodo
                data = comm.recv(source=i)
                uniques = []
                for word in data:
                    if word in words:
                        uniques.append(words.get(word))
                    else:
                        words.update({word: index})
                        uniques.append(index)
                        index += 1
                words_map.append(uniques)
    for i in range(size - 1):
        comm.send(-1, dest=i)
else:
    # Wait data para
    stopWords = getstopwords()
    path = comm.recv(source=0)
    while path != -1:
        content = open(path, 'r')
        txt = content.read().lower()
        text = txt.split()
        unique_words = []
        for i in range(len(text)):
            subword = text[i]
            if subword not in stopWords and subword not in unique_words:
                unique_words.append(subword)
        comm.send(unique_words, dest=0)
        path = comm.recv(source=0)

if rank == 0:
    amount = len(words_map)
    jaccard_matrix = np.empty(amount, amount)
    for i in range(amount):
        for j in range(amount):
            if j < i:
                jaccard_matrix[i][j] = jaccard_matrix[j][i]
            else:
                if j == i:
                    jaccard_matrix[i][j] = 1
                else:
                    jaccard_matrix[i][j] = jaccard_similarity(words_map[i], words_map[j])

    cents, c = kMeans(jaccard_matrix, clusters)
    books = os.listdir(str(sys.argv[1]))
    centroides = np.empty(clusters)
    for i in range(len(c)):
        centroides[c[i]].append(books[i])

    print centroides
    print "Time taken" + (time.time() - timeIni)
