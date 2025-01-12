
# Wordle Solver Algorithm

## Overview
This repository contains a Wordle solver algorithm implemented in Python. The program uses heuristic analysis, feedback processing, and API interaction to iteratively guess the correct Wordle word. The solver supports custom word lengths, seed values, and different game modes.

---

## Features
- **Dynamic Word List**: Fetches an extensive English word list directly from the [dwyl/english-words](https://github.com/dwyl/english-words) repository.
- **Dynamic Guessing**: Generates subsequent guesses based on feedback from previous attempts.
- **API Integration**: Interacts with a Wordle-like API to retrieve game results.
- **Fallback Mechanism**: Generates random guesses when no valid words remain.
- **Customizability**: Allows users to specify word length, seed, and game type.

---

## File Descriptions

### 1. `main.py`
The entry point of the program. It orchestrates the game loop:
- Dynamically fetches the word list from the `dwyl/english-words` GitHub repository.
- Loads and filters the word list based on the specified word length.
- Generates and submits guesses.
- Processes feedback and refines the pool of potential guesses.
- Ends when the correct word is found.

### 2. `last_resort.py`
Contains functions for handling edge cases:
- `process_result`: Updates the letter pools based on feedback (e.g., correct, present, or absent letters).
- `generate_word_from_pools`: Generates a random word by selecting letters from the refined pools.

### 3. `next_word.py`
Handles word refinement and guess generation:
- `refine_word_list`: Filters and reorders the word list based on feedback.
- `wordle_guess`: Generates the next guess from the refined word list.
- `refine_first_word_list`: Optimizes the initial word list for the first guess.
- `generate_first_word`: Creates a fallback word based on letter frequency.

### 4. `submit.py`
Interacts with the Wordle API:
- `submit_word`: Submits a guess to the API and retrieves the feedback.

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dave1998-bit/wordle_solver/edit/main/README.md
   cd wordle_solver
   ```

2. **Install Required Packages**:
   Ensure Python is installed, then install the `requests` package:
   ```bash
   pip install requests
   ```

3. **Run the Program**:
   ```bash
   python main.py
   ```

---

## Word List Source
The word list used in this project is dynamically fetched from the [dwyl/english-words](https://github.com/dwyl/english-words) repository. Full credit goes to the contributors of this repository for maintaining a comprehensive collection of English words.

---

## Usage

Run the main script:
```bash
python main.py
```

### Optional Parameters
- `game_type`: Specifies the game mode (`daily`, `random`).
- `seed`: Sets the seed for reproducibility.
- `length`: Specifies the length of the Wordle word.

Example:
```bash
python main.py --game_type random --seed 34 --length 5
```

---

## How It Works

1. **Word List Fetching**:
   - If the word list is not found locally, it is downloaded automatically from the GitHub repository.

2. **First Word Selection**:
   - The initial word is chosen based on letter frequency and uniqueness.

3. **Feedback Processing**:
   - The feedback (correct, present, absent) refines the pool of potential words and updates positional letter pools.

4. **Subsequent Guesses**:
   - The program iteratively guesses until the correct word is found.

