#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Sending and Receiving data tutorial - Supercomputing and Parallel Programming in Python and MPI 5
# Taken from: https://youtu.be/XdIwXDmxHLM?list=PLQVvvaa0QuDf9IW-fe6No8SCw-aVnCfRi
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
name = MPI.Get_processor_name()

shared = (rank+1) * 5

if rank == 0:
    data = shared
    time.sleep(5)
    comm.send(data,dest=1)
    comm.send(data,dest=2)
    print 'From rank', rank, 'we sent', data, 'and shared is:', shared
    print 'I am finishing at rank', rank
elif rank == 1:
    print "Waiting from rank", rank
    data = comm.recv(source=0)
    print 'on node', name, 'in rank:', rank ,'we received', data, 'and shared is:', shared
elif rank == 2:
    print "Waiting from rank", rank
    data = comm.recv(source=0)
    print 'on node', name, 'in rank:', rank, 'we received', data, 'and shared is:', shared

# que pasa si intercambiamos los destinos y las fuentes?
# cambie de lugar el time.sleep




