import sys


def main() -> int:
    nums = range(6)
    for i in nums:
        if i < 5:
            print(f'{i} is less than 5')
        else:
            print(f'{i} is not less than 5')

    return 0


if __name__ == "__main__":
    sys.exit(main())