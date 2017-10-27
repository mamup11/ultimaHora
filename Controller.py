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
#print size
#print rank

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
        #print "core: " + str(core)
        if core == size:
            core = 1
            for i in range(size):
                #print "i: " +str(i)
                if i != 0:
                    # print i
                    # Esperar resultados de cada nodo
                    #print "Wait for results from node: " +str(i)
                    data = comm.recv(source=i)
                    #print "Received from node " + str(i) +", "+ str(len(data)) +" words"
                    uniques = []
                    for word in data:
                        if word in words:
                            uniques.append(words.get(word))
                        else:
                            words.update({word: index})
                            uniques.append(index)
                            index += 1
                    #print "Finish dicctionary update from node: " + str(i)
                    words_map.append(uniques)

        # enviar a cada nodo un libro
        #print "data send to node: " + str(core)
        comm.send(documents + filename, dest=core)
        #print filename

    # print "Ending core: " + str(core)
    if core > 0:
        for i in range(core+1):
            if i != 0:
                # print i
                # Esperar resultados de cada nodo
                # print "Wait for results from node: " +str(i)
                data = comm.recv(source=i)
                # print "Received from node " + str(i) +", "+ str(len(data)) +" words"
                uniques = []
                for word in data:

                    if word in words:
                        uniques.append(words.get(word))
                    else:
                        words.update({word: index})
                        uniques.append(index)
                        index += 1
                words_map.append(uniques)
    for i in range(size):
        if i != 0:
            comm.send(-1, dest=i)
    #print "sale 0"
    print len(words)
    print "*" * 20
    read_time = time.time()
    print "Tiempo de lectura: " + str(read_time - timeIni)
    print "Tiempo de ejecucion finalizando lectura: " + str(read_time - timeIni)
    print "*" * 20

else:

    # Wait data para
    stopWords = getstopwords()
    path = comm.recv(source=0)
    #print ("Slave node number: " + str(rank)+ " received: " + path)
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
        #print
        #print "Sended from " + str(rank) + ": "
        #print unique_words
        path = comm.recv(source=0)
        #print "New entry in node: " +str(rank) + path


if rank == 0:
    #print len(words_map)
    amount = len(words_map)
    jaccard_matrix = np.empty((amount, amount), dtype=float)
    for i in range(amount):
        for j in range(amount):
            if j < i:
                jaccard_matrix[i][j] = jaccard_matrix[j][i]
            else:
                if j == i:
                    jaccard_matrix[i][j] = 0
                else:
                    jaccard_matrix[i][j] = 1 - jaccard_similarity(words_map[i], words_map[j])

    print "*" * 20
    jaccard_time = time.time()
    print "Tiempo de jaccard: " + str(jaccard_time - read_time)
    print "Tiempo de ejecucion finalizando jaccard: " + str(jaccard_time - timeIni)
    print "*" * 20

    cents, c = kMeans(jaccard_matrix, int(clusters))
    books = os.listdir(str(sys.argv[1]))
    centroides = []
    for i in range(int(clusters)):
        cluster = []
        centroides.append(cluster)
    for i in range(len(c)):
        centroides[c[i]].append(books[i])

    print centroides
    print

    print "*" * 20
    kMeans_time = time.time()
    print "Tiempo de kMeans: " + str(kMeans_time - jaccard_time)
    print "Tiempo de ejecucion total: " + str(kMeans_time - timeIni)
    print "*" * 20
