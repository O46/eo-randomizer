import os

class iteite:
    def __init__(self, container_directory):
        self.container_directory = container_directory
        
    def item_iterator(self, user_dir, rand_seed=0):
        full_list = os.listdir(user_dir)

        number_list = []
        name_list = []

        for file in full_list:
        	print(file)
        	print(file.split("-"))


if __name__ == "__main__":
    cur_dir = os.getcwd()
    ite = iteite(cur_dir)
    print(" Etrian Randomizer\n", "-"*20, "\n")
    while True:
        user_dir = input("Input the folder you would like to modify: ").strip()
        rand_seed = input("Enter a seed for randomization or leave empty: ").strip()
        if len(rand_seed) < 0:
            rand_seed = random.getrandbits(64)
        ite.item_iterator(user_dir, rand_seed)
