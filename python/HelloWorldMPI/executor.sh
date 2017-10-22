#!/usr/bin/env bash
# This code circumvents the problem on PyCharm IDE
# for MPI execution from the IDE
# EXAMPLE is the number of the example. Between 1 and 12.
# CORES is the number of cores. This parameter is taken from system
# Examples:
# 1. Print Hello World from each core
# 2. Executing different tasks from each core
# 3. Executing same code from each core and node. Counting cores.
# 4. Sending and Receiving data
# 5. Dynamically sending and receiving
# 6. Data tagging
# 7. Broadcasting with bcast
# 8. Scatter
# 9. Gather
# 10. Point to Point Communication
# 11. Scatter 2
# 12. Gather 2
if ! [ -x /usr/bin/nproc ]; then
    echo "nproc is not installed. Please install it."
    exit 1
fi
CORES=$(nproc)
EXAMPLE=1
#mpiexec -np ${CORES} python ./hello_world${EXAMPLE}.py
mpiexec  -np 3 python ./hello_world${EXAMPLE}.py
#mpiexec -np 16 python ./hello_world${EXAMPLE}.py
