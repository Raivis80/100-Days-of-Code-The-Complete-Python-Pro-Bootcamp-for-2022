import time


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} runs {end_time - start_time} seconds")
        return end_time - start_time
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for _ in range(10000000):
        pass


@speed_calc_decorator
def slow_function():
    for _ in range(100000000):
        pass


def main():
    first_run = fast_function()
    second_run = slow_function()
    print(f"First run: {first_run}, Second run: {second_run}")
    return second_run - first_run


if __name__ == "__main__":
    main()