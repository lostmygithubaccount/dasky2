import time 

from mpi4py import MPI 

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print("\n\n")
print("rank: ")
print(rank)
print("\n\n")

from dask_mpi import initialize
initialize()

from dask.distributed import Client 

counter = 0
while True:

    print(counter)
    counter += 1
    time.sleep(10)

    if rank == 1:
        print("rank1")
        try:
            client = Client()
            print(client)
        except:
            pass