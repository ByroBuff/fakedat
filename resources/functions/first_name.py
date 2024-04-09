import random
import json

def main(gender = "r"):
    if gender == "m":
        with open("resources/dicts/first_names_m.json", "r") as f:
            firstnames = json.load(f)
            return random.choice(firstnames)
    elif gender == "f":
        with open("resources/dicts/first_names_f.json", "r") as f:
            firstnames = json.load(f)
            return random.choice(firstnames)
    else:
        # random pick gender
        return main(random.choice(["m", "f"]))