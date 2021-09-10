import sys
import random


def main() -> int:
    # a = 0
    # while a <= 500000:
    #     print(a)
    #     a += 50000
    # return 0
    # print()

    nums = []
    for cur, _ in enumerate(range(500000)):
        print(f'\rGen... {cur}/500000', end="")
        nums.append(random.randint(0, 2000000000000))

    odds, evens = [], []
    total = len(nums)
    while nums:
        print(f"\rProcessing... [{len(evens) + len(odds)}/{total}]"
              f" ({(len(evens) + len(odds)) / total * 100}%)", end="")
        num = nums.pop()
        evens.append(num) if num % 2 == 0 else odds.append(num)

    print(f" Odd numbers: {len(odds)}")
    print(f"Even numbers: {len(evens)}")
    print(f" All numbers: {len(odds) + len(evens)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
