def string_validation(p):
    if len(p) == 0:
        return True

    pair = "()"

    stack = [p[0]]


    idx = 1
    while idx < len(p):
        if not stack and p[idx] == ")":
            return False

        if p[idx] == stack[-1]:
            stack.append(p[idx])
            idx += 1
        else:
            while stack:
                temp = stack.pop() + p[idx]
                if temp == pair:
                    idx += 1
                else:
                    return False

    return True


def solution(p):
    if string_validation(p):
        return p

    u = ""
    v = ""

    left_cnt = 0
    right_cnt = 0

    for idx, char in enumerate(p):
        u += char

        if char == "(":
            left_cnt += 1
        else:
            right_cnt += 1

        if left_cnt == right_cnt:
            v = p[idx+1:]
            break

    if string_validation(u):
        return u + solution(v)

    else:
        temp = list(u[1:-1])
        for i in range(len(temp)):
            temp[i] = ")" if temp[i] == "(" else "("
        temp = ''.join(temp)
        return '(' + solution(v) + ')' + temp



p = "(()())"
# p = ")("
# print(solution(p))

print(string_validation(p))
