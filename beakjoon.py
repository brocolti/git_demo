"""
서로 다른 값이 몇 개 있는지 = set
"""

import sys

def solve(data: str) -> str:

    remainders = set(int(x) % 42 for x in data.splitlines())
    
    result = str(len(remainders))
    print("Hello Will")
    print("이게 메인이야")
    return result


def main():
    data = sys.stdin.read().strip()
    print(solve(data))


if __name__ == "__main__":
    main()
