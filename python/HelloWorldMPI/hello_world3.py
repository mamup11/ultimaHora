#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Network Size tutorial- Supercomputing and Parallel Programming in Python and MPI 4
# Taken from: https://youtu.be/XdIwXDmxHLM?list=PLQVvvaa0QuDf9IW-fe6No8SCw-aVnCfRi
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

print 'rank:', rank
print 'node count:', size
print 9**(rank+3)
