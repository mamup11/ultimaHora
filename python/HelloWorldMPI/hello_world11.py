#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Scatter on MPI
# Taken from UTSA: https://youtu.be/Udn9wmmb9YY?list=PLNHwXvqzpO-EylKkU_yVRXwasq8Fbj9d-
from mpi4py import MPI
import numpy

sendbuf = []
root = 0
comm = MPI.COMM_WORLD

if comm.rank == 0:
    m = numpy.random.randn(comm.size, comm.size)
    print(m)
    sendbuf = m

v = comm.scatter(sendbuf,root)
print ('I got this array', v)

