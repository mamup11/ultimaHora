#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Dynamically sending and receiving tutorial - Parallel Programming in Python and MPI 6
# Taken from: https://youtu.be/XdIwXDmxHLM?list=PLQVvvaa0QuDf9IW-fe6No8SCw-aVnCfRi
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
name = MPI.Get_processor_name()

shared = (rank+1)*7

comm.send(shared,dest=(rank+1) % size)
data = comm.recv(source=(rank-1) % size)

print 'Name:', name, 'Rank:', rank, 'Received:', data, 'which came from rank:', (rank-1) % size

