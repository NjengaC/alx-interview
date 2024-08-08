#!/usr/bin/python3
"""
Prime game
"""


def isWinner(x, num):
    """
    Fucnction resolves the winner of a prime game session in `x` rounds
    """

    if x < 1 or not num:
        return None
    player1, player2 = 0, 0
    n = max(num)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    for _, n in zip(range(x), num):
        count = len(list(filter(lambda x: x, primes[0: n])))
        player2 += count % 2 == 0
        player1 += count % 2 == 1
    if player1 == player2:
        return None
    return 'Maria' if player1 > player2 else 'Ben'
