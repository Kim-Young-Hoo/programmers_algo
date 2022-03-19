def solution(record):
    answer = []
    id_dict = {}

    for r in record:
        r = r.split(' ')

        if r[0] == "Enter":
            answer.append([r[1], "님이 들어왔습니다."])
            id_dict[r[1]] = r[2]

        elif r[0] == "Leave":
            answer.append([r[1], "님이 나갔습니다."])

        else:
            id_dict[r[1]] = r[2]

    answer = [''.join([id_dict[sub_lst[0]], sub_lst[1]]) for sub_lst in answer]

    return answer