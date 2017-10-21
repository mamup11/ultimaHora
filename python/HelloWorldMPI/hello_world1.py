#!/usr/bin/env python
# -*- coding: utf-8 -*-
# hello.py
# Taken from Python Parallel Programming Cookbook. Giancarlo Zaccone
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print "hello world from process", rank
