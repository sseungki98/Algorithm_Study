from collections import Counter
count_store = Counter(list(input()))
one_count = 0
answer_string = ""
single_string = ''
for item in count_store.values():
    if item % 2 != 0:
        one_count += 1

if one_count > 1:
    print("I'm Sorry Hansoo")
else:
    for item in sorted((count_store.items())):
        if item[1] % 2 == 0:
            answer_string += item[0] * (item[1] // 2)
        else:
            answer_string += item[0] * (item[1] // 2)
            single_string = item[0]
    reversed_list = list(answer_string)
    reversed_list.reverse()
    reversed_answer = ''.join(reversed_list)
    print(answer_string+single_string+reversed_answer)