#!/usr/bin/python3
"""
2-main
"""
import sys

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse

    result = recurse(input("Target subreddit\n"))
    if result is not None:
        print(len(result))
    else:
        print("None")
