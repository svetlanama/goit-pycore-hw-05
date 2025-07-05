from caching_fibonacci import caching_fibonacci
from generator_numbers import generator_numbers, sum_profit

if __name__ == "__main__":
    # Завдання 1
    fib = caching_fibonacci()
    print(f"fib(10) = {fib(10)}")
    print(f"fib(15) = {fib(15)}")
    print(f"fib(0) = {fib(0)}")
    print(f"fib(1) = {fib(1)}")
    print(f"fib(20) = {fib(20)}")

    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

