# -*- coding: utf-8 -*-
import os, sys, time, collections
from Jaccard import *
from kmeans import *
from Dictionary import *


def read():
    timeIni = time.time()
    words = {}
    index = 0
    words_map = []
    otroWords = []
    arr = []
    mapa = dict()
    # comm = MPI.COMM_WORLD
    size = 3#comm.Get_size()
    rank = 0

    if len(sys.argv) != 2:
        print "Error!"
        print "Usage: " + sys.argv[0] + " PATH"
        exit(-1)

    documents = str(sys.argv[1])
    if rank == 0:
        core = 0
        for filename in os.listdir(documents):
            if str(filename).endswith(".txt"):
                core += 1
                print core
                if core == size:
                    core = 0

                    for i in range(size):
                        # print i
                        # Esperar resultados de cada nodo
                        data = []#comm.recv(source=i)
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
                    1
                    # enviar a cada nodo un libro
                    # comm.send(documents + filename, dest=core)


    else:
        #Wait datos para
        stopWords = getstopwords()
        path = 1#comm.recv(source=0)
        while path != -1:

            content = open(path, 'r')
            txt = content.read().lower()
            text = txt.split()
            unique_words = []

            for i in range(len(text)):
                if text[i] not in stopWords and text[i] not in unique_words:
                    unique_words.append(arr[i])
            # comm.send(unique_words, dest=0)
            # path = comm.recv(source=0)



    mat = np.empty((len(fdt), len(fdt)))
    for i in range(len(fdt)):
        for j in range(len(fdt)):
            mat[i][j] = 1 - jaccard_similarity(fdt[i], fdt[j])

    # jaccard(result)
    print mat
    cents, C = kMeans(mat, 2)
    print C
    print "-" * 50
    print cents
    print(time.time() - timeIni)


read()