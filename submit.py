import requests

def submit_word(guess: str, size: int = 5, seed: int = 34, game_type: str = "random"):
    """
    Guess a random word using the /random endpoint.

    :param guess: The word guess (string).
    :param size: The size of the word to guess (default: 5).
    :param seed: Optional seed for randomness (integer).
    :return: The API response (JSON) or None if an error occurs.
    """
    url = str("https://wordle.votee.dev:8000/"+game_type)
    params = {
        
        "guess": guess,
        "size": size
    }
    if seed is not None:
        params["seed"] = seed

    try:
        # Send GET request with query parameters
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()  # Parse and return the JSON response
        else:
            print(f"Error: Received status code {response.status_code}")
            print("Response:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
