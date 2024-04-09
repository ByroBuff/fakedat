import random
import json

def main():
    with open("resources/dicts/last_names.json", "r") as f:
        lastnames = json.load(f)
        return random.choice(lastnames)