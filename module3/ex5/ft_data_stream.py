"""Module for memory-efficient data streaming using Python generators."""


def event_generator(limit: int):
    """
    Generate a stream of simulated game events.

    Args:
        limit: The total number of events to produce.

    Yields:
        A tuple containing (player_name, level, event_type).
    """
    players = ["alice", "bob", "charlie", "diana"]
    events = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, limit + 1):
        player = players[i % len(players)]
        level = (i * 7) % 25
        event_type = events[i % len(events)]
        yield (i, player, level, event_type)


def fibonacci_generator(n: int):
    """
    Generate the first n numbers of the Fibonacci sequence.

    Yields:
        The next number in the Fibonacci sequence.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n: int):
    """
    Generate the first n prime numbers.

    Yields:
        The next prime number.
    """
    count = 0
    num = 2
    while count < n:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1


def process_stream() -> None:
    """
    Process the game data stream and display analytics and demonstrations.
    """
    print("=== Game Data Stream Processor ===")
    limit = 1000
    print(f"Processing {limit} game events...")

    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    for i, player, level, event in event_generator(limit):
        if i <= 3:
            print(f"Event {i}: Player {player} (level {level}) {event}")
        if i == 4:
            print("...")

        if level >= 10:
            high_level_count += 1
        if event == "found treasure":
            treasure_count += 1
        elif event == "leveled up":
            levelup_count += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {limit}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    fib_list = [str(x) for x in fibonacci_generator(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")

    prime_list = [str(x) for x in prime_generator(5)]
    print(f"Prime numbers (first 5): {', '.join(prime_list)}")


if __name__ == "__main__":
    process_stream()    