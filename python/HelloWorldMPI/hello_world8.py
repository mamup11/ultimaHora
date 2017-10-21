#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Scatter tutorial - Supercomputing and Parallel Programming in Python and MPI 9
# Taken from: https://youtu.be/XdIwXDmxHLM?list=PLQVvvaa0QuDf9IW-fe6No8SCw-aVnCfRi
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = [(x+1)**x for x in range(size)]
    print 'we will be scattering:', data
else:
    data = None

data = comm.scatter(data, root=0)
print 'rank', rank, 'has data:', data


