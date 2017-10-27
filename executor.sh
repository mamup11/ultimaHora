#!/home/mmurillo/anaconda2 bash

if ! [ -x /usr/bin/nproc ]; then
    echo "nproc is not installed. Please install it."
    exit 1
fi
CORES=$(nproc)
#mpiexec -np ${CORES} python ./hello_world${EXAMPLE}.py
mpiexec  -np 4 python ./Controller.py
#mpiexec -np 16 python ./hello_world${EXAMPLE}.py
