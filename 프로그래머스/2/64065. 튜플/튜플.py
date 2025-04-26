def solution(s):
    answer = []
    ans_stack = []
    s_len = len(s)
    sliced_s = s[1:s_len-1]
    start_flag = False
    temp_str = ""
    for i in range(len(sliced_s)):
        if sliced_s[i] == '{':
            start_flag = True
            continue
        if sliced_s[i] == '}':
            ans_stack.append(temp_str.split(','))
            temp_str = ""
            start_flag = False
            continue
        if start_flag:
            temp_str += sliced_s[i]
    
    new_answer_stack = sorted(ans_stack, key=lambda x:len(x))
    answer.append((int(new_answer_stack[0][0])))
    if len(new_answer_stack) == 1:
        return answer
    for item in new_answer_stack:
        if len(item) == 1:
            continue
        for el in item:
            if int(el) not in answer:
                answer.append(int(el))
                break
    return answer