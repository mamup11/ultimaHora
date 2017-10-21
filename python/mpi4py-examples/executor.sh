#!/usr/bin/env bash
EXAMPLE=09
CORES=4
mpiexec -np ${CORES} python ./${EXAMPLE}*.py
