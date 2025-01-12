import re

def refine_word_list(response, word_list):
    """
    Refines the list of potential words based on the Wordle feedback.

    Args:
    - response: List of dictionaries with feedback for a guess.
    - word_list: List of possible words.

    Returns:
    - A refined list of words.
    """
    letter_points = {
        'A': 26, 'E': 25, 'S': 24, 'O': 23, 'R': 22, 'I': 21, 'L': 20, 'T': 19, 'N': 18, 'U': 17, 'D': 16, 'C': 15,
        'M': 13, 'P': 12, 'H': 11, 'B': 10, 'G': 9, 'K': 8, 'F': 7, 'W': 6, 'V': 5, 'Z': 4, 'J': 3, 'X': 2, 'Q': 1
    }

    # Step 1: Eliminate words containing letters marked as 'absent'
    for feedback in response:
        if feedback['result'] == 'absent':
            word_list = [word for word in word_list if feedback['guess'] not in word]

    # Step 2: Keep words with 'present' and 'correct' feedback
    for feedback in response:
        slot, guess, result = feedback['slot'], feedback['guess'], feedback['result']
        if result == 'present':
            # Keep words containing the letter but not in the specific position
            word_list = [word for word in word_list if guess in word and word[slot] != guess]
        elif result == 'correct':
            # Keep words with the letter in the specific position
            word_list = [word for word in word_list if word[slot] == guess]

    # Step 3: Reorder the word list based on points
    def calculate_points(word):
        return sum(letter_points.get(letter.upper(), 0) for letter in word)

    word_list.sort(key=calculate_points, reverse=True)
    return word_list


def wordle_guess(response, word_list):
    """
    Makes a new guess based on the Wordle response.

    Args:
    - response: List of dictionaries with feedback for a guess.
    - word_list: List of possible words.

    Returns:
    - A tuple containing the next guess (string) and the refined word list.
    """
    # Refine the word list based on the response
    refined_words = refine_word_list(response, word_list)

    # Return the first word from the refined list as the next guess
    return (refined_words[0] if refined_words else None, refined_words)


def refine_first_word_list(word_list):
    """
    Reorders the list of potential first words based on letter frequency points.

    Args:
    - word_list: List of possible words.

    Returns:
    - A reordered list of words based on points.
    """
    letter_points = {
        'A': 26, 'E': 25, 'S': 24, 'O': 23, 'R': 22, 'I': 21, 'L': 20, 'T': 19, 'N': 18, 'U': 17, 'D': 16, 'C': 15,
        'M': 13, 'P': 12, 'H': 11, 'B': 10, 'G': 9, 'K': 8, 'F': 7, 'W': 6, 'V': 5, 'Z': 4, 'J': 3, 'X': 2, 'Q': 1
    }

    # Reorder the word list based on points
    def calculate_points(word):
        return sum(letter_points.get(letter.upper(), 0) for letter in word)

    word_list.sort(key=calculate_points, reverse=True)
    
    return word_list


def generate_first_word(word_length):
    """
    Generates a word using a predefined sequence of common letters. If the desired word length
    is greater than the sequence length, the sequence is repeated.

    Args:
    - word_length: Length of the desired word.

    Returns:
    - A generated word of the specified length.
    """
    base_sequence = "aesoriltnudcymphbgkfwvzjxq"  # Predefined sequence of letters ranked by frequency
    repeat_count = (word_length // len(base_sequence)) + 1  # Determine how many times to repeat the sequence
    generated_word = (base_sequence * repeat_count)[:word_length]  # Repeat and slice to the desired length
    return generated_word
