def solution(s):
    answer = len(s)

    comp_len = 0
    while comp_len <= len(s) // 2:
        comp_len += 1
        pointer = 0
        current_string = ""

        repeated = 1

        while pointer < len(s):

            if s[pointer:pointer + comp_len] == s[pointer + comp_len:pointer + comp_len + comp_len]:
                repeated += 1

            else:
                if repeated > 1:
                    current_string += str(repeated) + s[pointer:pointer + comp_len]
                    repeated = 1

                else:
                    current_string += s[pointer:pointer + comp_len]
                    repeated = 1

            pointer += comp_len

        answer = min(answer, len(current_string))

    return answer

s = "aabbaccc"

print(solution(s))