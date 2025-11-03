from caching_fibonacci import caching_fibonacci
from generator_numbers import generator_numbers, sum_profit
import sys
from log_analyzer import load_logs, count_logs_by_level, display_log_counts, filter_logs_by_level

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].endswith('.log'):
        file_path = sys.argv[1]
        level = sys.argv[2] if len(sys.argv) > 2 else None
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        if level:
            filtered = filter_logs_by_level(logs, level)
            print(f"\nLog details for level '{level.upper()}':")
            for log in filtered:
                print(f"{log['date']} {log['time']} - {log['message']}")
        sys.exit(0)

    # Завдання 1
    # fib = caching_fibonacci()
    # print(f"fib(10) = {fib(10)}")
    # print(f"fib(15) = {fib(15)}")
    # print(f"fib(0) = {fib(0)}")
    # print(f"fib(1) = {fib(1)}")
    # print(f"fib(20) = {fib(20)}")

    # Завдання 2
    # text = (
    #     "Загальний дохід працівника складається з декількох частин: "
    #     "1000.01 як основний дохід, доповнений додатковими надходженнями "
    #     "27.45 і 324.00 доларів."
    # )
    # total_income = sum_profit(text, generator_numbers)
    # print(f"Загальний дохід: {total_income}")

