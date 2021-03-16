import os
import random
import shutil


class iteite:
    def __init__(self, container_directory):
        self.container_directory = container_directory
        
    def item_iterator(self, user_dir, boss_skip, rand_seed=0):
        full_list = os.listdir(user_dir)
        clean_list = []
        number_list = []
        name_list = []
        comb_list = []

        with open("files to ignore", "r") as ignore_list:
            ignored_numbers = ignore_list.readlines()

        if boss_skip == True:
            with open("bosses", "r") as boss_list:
                ignored_numbers.extend(boss_list.readlines())

        for item in full_list:
            if not any(bad_number.strip() in item for bad_number in ignored_numbers):
                clean_list.append(item)

        for file in clean_list:
            number_list.append(file.split("-")[0])
            name_list.append(file.split("-")[1])

        random.Random(rand_seed).shuffle(name_list)

        for item in number_list:
            comb_list.append(item + "-" + name_list[number_list.index(item)])

        i = 0	
        for item in clean_list:
        	shutil.move(os.path.join(user_dir, item), os.path.join(user_dir, comb_list[i]))
        	i += 1

        print("Seed used: ", rand_seed, "\n\n\n")


if __name__ == "__main__":
    cur_dir = os.getcwd()
    ite = iteite(cur_dir)
    print(" Etrian Randomizer\n", "-"*20, "\n")
    while True:
        try:
            user_dir = input("Input the folder you would like to modify: ").strip()
            rand_seed = input("Enter a seed for randomization or leave empty: ").strip()
            boss_skip = input("Randomize bosses? (y/n): ").strip().lower()[0]
            if boss_skip == "y":
                boss_skip = True
            if len(rand_seed) < 1:
                rand_seed = random.getrandbits(64)
            ite.item_iterator(user_dir, boss_skip, rand_seed)
        except Exception as e:
            print("Error: {0}\nPlease try again.".format(e))