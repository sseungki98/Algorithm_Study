from sys import stdin
start_event, end_event, end_stream = map(str, input().split())
start = int(start_event[:2] + start_event[3:])
end = int(end_event[:2] + end_event[3:])
stream = int(end_stream[:2] + end_stream[3:])

member_list = set()
cnt = 0

while True:
    try:
        line = stdin.readline().rstrip()
        time = int(line[:2] + line[3:5])
        member_name = line[6:]

        if time <= start:
            member_list.add(member_name)
        elif end <= time <= stream and member_name in member_list:
            cnt += 1
            member_list.remove(member_name)

    except:
        break


print(cnt)