import hashlib
import random


def random_hash():
    """Generate a random SHA-256 hash"""
    random_value = str(random.random())
    return hashlib.sha256(random_value.encode()).hexdigest()


def add(x, y):
    """This is an add function"""
    return x + y


if __name__ == "__main__":
    print(add(1, 1))
    print(random_hash())
