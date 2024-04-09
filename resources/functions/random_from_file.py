import random

def main(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        return random.choice(lines).strip()