import random
import ast

def main(l=[]):
    print(type(l))
    l = ast.literal_eval(l)
    return random.choice(l)