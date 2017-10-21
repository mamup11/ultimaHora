#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Gather on MPI
# Taken from UTSA: https://youtu.be/Udn9wmmb9YY?list=PLNHwXvqzpO-EylKkU_yVRXwasq8Fbj9d-
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
sendbuf = []
root = 0

if comm.rank == 0:
    m = numpy.array(range(comm.size), dtype=float)
    m.shape#(comm.size,comm.size)
    print(m)
    sendbuf = m

v = comm.scatter(sendbuf,root)
print 'I got this array', v
v = v * v
recvbuf = comm.gather(v, root)

if comm.rank == 0:
    print numpy.array(recvbuf)

