import requests
from os import environ

def get_input(year: int, day: int) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session_cookie = environ.get("AOC_COOKIE")
    if session_cookie is None:
        raise Exception("AOC_COOKIE environment variable not set")
    response = requests.get(url, cookies={"session": session_cookie})
    return response.text.strip()