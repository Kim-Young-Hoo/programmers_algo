def solution(new_id):
    answer = ''

    dictionary = 'abcdefghijklmnopqrstuvwxyz-_.'

    new_id = new_id.lower()

    for i in range(len(new_id)):
        if new_id[i] == '.' and len(answer) == 0:
            continue

        if new_id[i] in dictionary:
            if new_id[i] == '.' and answer[-1] == '.':
                continue
            answer += new_id[i]
        elif new_id[i].isdigit():
            answer += str(new_id[i])


    if len(answer) == 0:
        answer = "a"

    while True:
        if answer[-1] == '.':
            answer = answer[:-1]
        else:
            break


    if len(answer) >= 16:
        return solution(answer[:15])

    elif len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer



new_id = "=.="

print(solution(new_id=new_id))