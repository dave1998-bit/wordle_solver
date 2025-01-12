
import random


# Processes feedback from the previous guess to refine the letter pools
def process_result(pools, result):
    for feedback in result:
        slot = feedback['slot']
        letter = feedback['guess']
        outcome = feedback['result']

        if outcome == 'absent':  # Letter not in the word
            for pool in pools:
                pool.discard(letter)
        elif outcome == 'correct':  # Letter in the correct position
            pools[slot] = {letter}
        elif outcome == 'present':  # Letter in the word but wrong position
            pools[slot].discard(letter)

    return pools

# Generates a word by randomly picking a letter from each pool
def generate_word_from_pools(pools):
    return "".join(random.choice(list(pool)) for pool in pools if pool)