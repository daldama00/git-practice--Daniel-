



def expensive_op(n):
    total = 0
    total = n * sum(range(1000))
    return total


def slow_func(lst):
    return [expensive_op(i) for i in range(len(lst))]


def main():
    numbers = list(range(1000))
    output = slow_func(numbers)
    print("Done")


if __name__ == "__main__":
    main()
