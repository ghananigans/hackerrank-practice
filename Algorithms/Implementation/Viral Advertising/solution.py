n = int(input())
original_num_people = 5

today_saw = original_num_people
total_liked = 0
today_liked = 0

for i in range(n):
    today_liked = today_saw // 2
    total_liked += today_liked
    today_saw = today_liked * 3

print(total_liked)

