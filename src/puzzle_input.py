"""Common functions related to fetching and storing the puzzle input."""

import json
import os

import requests

INPUT_URL_TEMPLATE = "https://adventofcode.com/2024/day/{day}/input"
COOKIES_FILENAME = "cookies.json"
PUZZLE_FILEPATH = "src/puzzles/day_{day}/"
INPUT_FILENAME = "input.txt"


cookies: dict[str, str] = {}


def save_cookies():
    """Saves the cookies to cookies.json."""
    with open(COOKIES_FILENAME, "w", encoding="utf-8") as cookies_file:
        json.dump(cookies, cookies_file)


def read_cookies():
    """Reads the saved cookies from cookies.json."""
    cookies.clear()
    try:
        with open(COOKIES_FILENAME, "r", encoding="utf-8") as cookies_file:
            cookies.update(json.load(cookies_file))
    except FileNotFoundError:
        save_cookies()


def fetch_puzzle_input(day: int) -> str:
    """Fetches the input for the puzzle of the given day."""
    read_cookies()
    while not cookies.get("session"):
        session = input("Enter your session id (type 'help' for explanation):\n> ")
        if session.lower() == "help":
            print(
                "Assuming you are logged in, visit <https://adventofcode.com/2024/>, "
                "open your developer tools (F12), go to the 'Storage' (or 'Application') tab, "
                "choose 'Cookies', select 'session' and copy the value."
            )
            continue
        cookies["session"] = session.strip('"')
        save_cookies()
    print("Fetching the puzzle input...")
    url = INPUT_URL_TEMPLATE.format(day=day)
    response = requests.get(url, cookies=cookies, timeout=10)
    data = response.text
    if not response.ok:
        raise RuntimeError(f"HTTP {response.status_code}: {data}")
    directory = PUZZLE_FILEPATH.format(day=day)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    with open(directory + INPUT_FILENAME, "w", encoding="utf-8") as input_file:
        input_file.write(data)
    return data


def get_puzzle_input(day: int) -> str:
    """Reads the input for the puzzle of the given day from the input.txt file."""
    try:
        with open(
            PUZZLE_FILEPATH.format(day=day) + INPUT_FILENAME, "r", encoding="utf-8"
        ) as input_file:
            return input_file.read()
    except FileNotFoundError:
        return fetch_puzzle_input(day)
