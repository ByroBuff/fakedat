import random
import json

def main(first, second):
    formats = ["%firstL%%second%", "%first%%secondL%", "%first%%second%", "%firstL%%second%%number%", "%first%%secondL%%number%", "%first%%second%%number%"]
    providers = ["@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com", "@icloud.com", "@aol.com", "@zoho.com", "@protonmail.com", "@gmx.com", "@yandex.com"]
    format = random.choice(formats)
    format = format.replace("%first%", first)
    format = format.replace("%second%", second)
    format = format.replace("%firstL%", first[0])
    format = format.replace("%secondL%", second[0])
    format = format.replace("%number%", str(random.randint(1, 1000)))

    return format + random.choice(providers)