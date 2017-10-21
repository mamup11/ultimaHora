#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Data tagging tutorial - Supercomputing and Parallel Programming in Python and MPI 7
# Taken from: https://youtu.be/XdIwXDmxHLM?list=PLQVvvaa0QuDf9IW-fe6No8SCw-aVnCfRi
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
name = MPI.Get_processor_name()

if rank == 0:
    shared = {'d1': 22, 'd2': 33}
    comm.send(shared, dest=1, tag=1)

    shared2 = {'d1': 44, 'd2': 55}
    comm.send(shared2, dest=1, tag=2)

if rank == 1:
    receive = comm.recv(source=0, tag=2)
    print receive, receive['d1']
    receive2 = comm.recv(source=0, tag=1)
    print receive2, receive2['d1']

# que pasaría si el orden importa y quiero recibir primero el shared2?

