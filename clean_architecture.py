"""Clean architecture in python
https://youtu.be/DJtef410XaM

Separate logic and I/O
"""

from urllib.parse import urlencode
import requests


def find_definition(word):
    """1 or 2 integration tests for this"""
    url = build_url(word)
    data = requests.get(url).json()  # I/O
    return pluck_definition(data)


def build_url(word):
    q = "define " + word
    url = "http://api.duckduckgo.com/?"
    url += urlencode({"q": q, "format": "json"})
    return url


def pluck_definition(data):
    definition = data[u"definition"]
    if definition == u"":
        raise ValueError("that is not a word")
    return definition


# Testing
# Functional core - Many fast unit tests
# Imperative shell - Few integration tests


# BAD
def uppercase_words(wordlist):
    """I/O as a side effect"""
    for word in wordlist:
        word = word.upper()
        print(word)


# GOOD
def process_words(wordlist):
    """Logic with zero side effects"""
    for word in wordlist:
        yield word.upper()


def procedural_glue(wordlist):
    """I/O goes outside of logic"""
    for word in process_words(wordlist):
        print(word)


words = ["Hello", "You"]

procedural_glue(words)
