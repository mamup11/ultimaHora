#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Conditional Statements tutorial - Supercomputing and Parallel Programming in Python and MPI 3
# Taken from: https://youtu.be/XdIwXDmxHLM?list=PLQVvvaa0QuDf9IW-fe6No8SCw-aVnCfRi
from mpi4py import MPI

comm = MPI.COMM_WORLD

print 'My rank is', comm.rank
if comm.rank == 1:
    print 'Doing the task of rank 1'

if comm.rank == 2:
    print 'Haciendo la tarea del nodo 2'

if comm.rank == 3:
    print 'faisant noeud de devoirs 3'
