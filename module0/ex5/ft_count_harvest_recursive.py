def ft_count_harvest_recursive():
    limit = int(input("Days until harvest: "))

    def count_days(current):
        if current > limit:
            return
        print(f"Day {current}")
        count_days(current + 1)
    count_days(1)
    print("Harvest time!")
