#!/bin/python3

REPEATING_LETTER = 'a'

s = input().strip()
n = int(input().strip())
len_s = len(s)

full_repeats = n // len_s
partial_repeat_letters = n % len_s
count = 0

for i in range(min(len_s, n)):
    if s[i] == REPEATING_LETTER:
        count += full_repeats
        
        if i < partial_repeat_letters:
            count += 1

print(count)

