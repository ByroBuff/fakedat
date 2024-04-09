import random
import json

def main():
    with open("resources/dicts/adjectives.json", "r") as adjectivies:
        with open("resources/dicts/nouns.json", "r") as nouns:
            adjectives = json.load(adjectivies)
            nouns = json.load(nouns)

            formats = ["%adjective%%noun%%number%", "%adjective%%noun%", "%noun%%number%"]

            format = random.choice(formats)
            format = format.replace("%adjective%", random.choice(adjectives).title())
            format = format.replace("%noun%", random.choice(nouns).title())
            format = format.replace("%number%", str(random.randint(1, 100)))
            
            return format                