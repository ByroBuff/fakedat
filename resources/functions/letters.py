def main(count):
    import random
    return ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=int(count)))