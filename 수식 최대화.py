from itertools import permutations

def solution(expression):
    answer = 0
    lst = []

    perm = list(permutations("+*-", 3))

    if expression[0] in "+*-":
        operand = expression
    else:
        operand = "+"
    num = ""
    for ele in expression:
        if ele.isdigit():
            num += ele
        else:
            lst.append(operand+num)
            num = ""
            operand = ele
    lst.append(operand+ num)
    print(lst)

    for p in perm:
        new_expression = lst.copy()
        for oper in p:
            idx = 0
            while len(new_expression) > 1:
                idx += 1

                if oper not in ''.join(new_expression[1:]):
                    break

                if new_expression[idx][0] == oper:
                    if new_expression[idx][0] == "+":
                        new_ele = new_expression[idx - 1][0] + str(eval((new_expression[idx - 1][1:])) + eval(new_expression.pop(idx)[1:]))
                    elif new_expression[idx][0] == "-":
                        new_ele = new_expression[idx - 1][0] + str(eval(new_expression[idx - 1][1:]) - eval(new_expression.pop(idx)[1:]))
                    else:
                        new_ele = new_expression[idx - 1][0] + str(eval(new_expression[idx - 1][1:]) * eval(new_expression.pop(idx)[1:]))

                    new_expression[idx - 1] = new_ele[0] + "(" + new_ele[1:] + ")"

                    idx = 0
        answer = max(abs(eval(new_expression[0])), answer)




    return answer


expression = "100-200*300-500+20"
solution(expression=expression)