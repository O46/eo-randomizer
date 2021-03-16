import os
import random
import shutil
import math

class iteite:
    def __init__(self, container_directory):
        self.container_directory = container_directory
        
    def item_iterator(self, user_dir, boss_skip, num_seed, mon_seed):
        full_list = os.listdir(user_dir)
        clean_list = []
        number_list = []
        name_list = []
        comb_list = []

        with open("files to ignore", "r") as ignore_list:
            ignored_numbers = ignore_list.readlines()

        if boss_skip:
            with open("bosses", "r") as boss_list:
                ignored_numbers.extend(boss_list.readlines())

        for item in full_list:
            if not any(bad_number.strip() in item for bad_number in ignored_numbers):
                clean_list.append(item)

        for file in clean_list:
            number_list.append(file.split("-")[0])
            name_list.append(file.split("-", 1)[1])

        random.Random(num_seed).shuffle(number_list)

        i = 0
        for item in clean_list:
                comb_list.append(number_list[i] + "-" + name_list[i])
                i+=1

        i = 0
        for item in clean_list:
            shutil.move(os.path.join(user_dir, item), os.path.join(user_dir, comb_list[i]))
            i += 1

        post_list = os.listdir(user_dir)
        print("Seed used: ", num_seed, "\n\n\n")


if __name__ == "__main__":
    cur_dir = os.getcwd()
    ite = iteite(cur_dir)
    print(" Etrian Randomizer\n", "-"*20, "\n")
    while True:
        try:
            user_dir = input("Input the folder you would like to modify: ").strip()
            num_seed = input("Enter a seed for randomization or leave empty: ").strip()
            boss_skip = input("Randomize bosses? (y/n): ").strip().lower()[0]
            if boss_skip == "y":
                boss_skip = True
            if len(num_seed) < 1:
                num_seed = random.getrandbits(64)
            mon_seed = math.floor(float(num_seed) * .46) + 46
            ite.item_iterator(user_dir, boss_skip, num_seed, mon_seed)
        except Exception as e:
            print("Error: {0}\nPlease try again.".format(e))
