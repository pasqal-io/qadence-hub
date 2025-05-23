
from perceptrain.train_utils import Accelerator

def simple_print(acc):
    print(f"""Hello--------
           This is process {acc.rank}
            Total world size {acc.world_size}
            """)



if __name__ == "__main__":
    accelerator = Accelerator(
        nprocs=10,                # Two processes
    )

    distributed_print = accelerator.distribute(simple_print)
    distributed_print(acc=accelerator) 