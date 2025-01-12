import re
import os
import string
from next_word import wordle_guess, refine_first_word_list, generate_first_word
from submit import submit_word
from last_resort import process_result, generate_word_from_pools
import requests

# Main function to play the Wordle game
def main(game_type="daily", seed=None, length=5):
    # Load the list of possible words from a text file
    def load_word_list(url, length):
        response = requests.get(url)
        if response.status_code == 200:
            words = response.text.splitlines()
            # Filter words to include only those of the correct length with lowercase alphabetic characters
            filtered_words = [word for word in words if len(word) == length and word.islower() and re.match("^[a-z]+$", word)]
            print(f"Successfully loaded {len(filtered_words)} words of length {length}.")
            return filtered_words
        else:
            raise Exception(f"Failed to fetch words. HTTP Status Code: {response.status_code}")

    # Load the word list from the GitHub URL
    word_list_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    length = 5  # Change this to the desired word length
    word_list = load_word_list(word_list_url, length)

    # Generate the first word
    refined_list = refine_first_word_list(word_list)

    if refined_list:
        i=0
        while i<len(refined_list): 
            first_word = refined_list[i] 
            if len(first_word) == len(set(first_word)):
                break
            else:
                i+=1
    else:
        first_word=generate_first_word(length)
    print("First word:", first_word)

    # Submit the first word and get results
    results = submit_word(first_word, length, seed, game_type)

    # Initialize pools for each letter position
    pools = [set(string.ascii_lowercase) for _ in range(length)]

    # Main guessing loop
    while True:
        # Generate the next word based on results
        next_word, word_list = wordle_guess(results, word_list)

        if next_word is None:
            # If no valid word is found, generate a random word from pools
            next_word = generate_word_from_pools(pools)
            print("Generated random word from pools:", next_word)
        else:
            print("Next word:", next_word)

        # Submit the guess and get the results
        results = submit_word(next_word, length, seed, game_type)

        # Update pools based on feedback
        pools = process_result(pools, results)

        # Check if all guesses are correct
        if all(result['result'] == 'correct' for result in results):
            print(f"The answer is: {next_word}")
            break

# Run the main function with specified parameters
main(game_type="random", seed=34, length=28)
