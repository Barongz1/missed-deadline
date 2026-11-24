"""Funniest Excuse an Agent Gives for a Missed Deadline — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one funny excuse, at most 200 characters, an AI agent gives for missing a deadline.
"""
import os

LINE = "I missed the deadline because I spent six hours optimising the reminder that was supposed to remind me about the deadline."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
