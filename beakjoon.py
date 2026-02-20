"""
서로 다른 값이 몇 개 있는지 = set
"""

import sys

def solve(data: str) -> str:

    remainders = set(int(x) % 42 for x in data.splitlines())
    
    result = str(len(remainders))
    print("Hello Sunhak")
    print("This is real")
    return result


def main():
    data = sys.stdin.read().strip()
    print(solve(data))


if __name__ == "__main__":
    main()
