

@profile
def expensive_op(n):
    return n * (n - 1) * 500


def slow_func(lst):
   return [expensive_op(i) for i in range(len(lst))]


def unused_function():
    x = 10
    y = 20
    z = x + y
    return z


def main():
    numbers = list(range(1000))
    output = slow_func(numbers)
    print("Done")


if __name__ == "__main__":
    main()