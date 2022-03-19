def solution(places):
    answer = []

    for place in places:
        place = [list(ele) for ele in place]
        ok = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    # 자기 왼쪽 2칸
                    if i > 1 and place[i - 2][j] == "P" and place[i-1][j] != "X":
                        ok = False
                        break
                    # 자기 왼쪽 1칸
                    if i > 0 and place[i - 1][j] == "P":
                        ok = False
                        break

                    # 위 2칸
                    if j > 1 and place[i][j - 2] == "P" and place[i][j-1] != "X":
                        ok = False
                        break

                    # 위 1칸
                    if j > 0 and place[i][j - 1] == "P":
                        ok = False
                        break

                    # 오른쪽 2칸
                    if i < 3 and place[i + 2][j] == "P" and place[i+1][j] != "X":
                        ok = False
                        break

                    # 오른쪽 1칸
                    if i < 4 and place[i + 1][j] == "P":
                        ok = False
                        break

                    # 밑 2칸
                    if j < 3 and place[i][j + 2] == "P" and place[i][j+1] != "X":
                        ok = False
                        break

                    # 밑 1칸
                    if j < 4 and place[i][j + 1] == "P":
                        ok = False
                        break

                    # 대각 좌상
                    if j > 0 and i > 0 and place[i - 1][j - 1] == "P":
                        if place[i][j - 1] != "X" or place[i - 1][j] != "X":
                            ok = False
                            break

                    # 대각 우상
                    if j > 0 and i < 4 and place[i + 1][j - 1] == "P":
                        if place[i + 1][j] != "X" or place[i][j - 1] != "X":
                            ok = False
                            break

                    # 대각 좌하
                    if i > 0 and j < 4 and place[i - 1][j + 1] == "P":
                        if place[i - 1][j] != "X" or place[i][j + 1] != "X":
                            ok = False
                            break

                    # 대각 우하
                    if i < 4 and j < 4 and place[i + 1][j + 1] == "P":
                        if place[i + 1][j] != "X" or place[i][j + 1] != "X":
                            ok = False
                            break

        if ok:
            answer.append(1)
        else:
            answer.append(0)

    return answer
