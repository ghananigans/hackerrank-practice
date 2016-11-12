#!/bin/python3

n, k = [int(temp) for temp in input().split(' ')]
questions = [int(temp) for temp in input().split(' ')]
assert(len(questions) == n)

count = 0
page = 1
chapter = 0
first_question = 1

while chapter < n:
    last_question = min(questions[chapter], first_question + k - 1)

    if first_question <= page and page <= last_question:
        # page num is within first and last question num on a page
        count += 1

    first_question += k
    page += 1

    if first_question > questions[chapter]:
        # question is now beyond the question limit for this chapter
        chapter += 1
        first_question = 1

print(count)
