#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Broadcasting with bcast tutorial - Supercomputing and Parallel Programming in Python and MPI 8
# Taken from: https://youtu.be/XdIwXDmxHLM?list=PLQVvvaa0QuDf9IW-fe6No8SCw-aVnCfRi
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    data = {'a': 1, 'b': 2, 'c': 3}
else:
    data = None

data = comm.bcast(data, root=0)
print 'rank', rank, data
