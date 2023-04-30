
'''
TIL 적립 완료
'''


def pas(list, line_num):
    if len(list) == line_num:
        return list
    result = list[:]
    for i in range(len(list)-1):
        result[i+1] = list[i]+list[i+1]
    result.append(1)
    return pas(result, line_num)


a = pas([1], 9)
print(a)


##소은####

def pascal(list,n):
    if n > 1:
        answer = []
        answer.append(1)
        for i in range(len(list)-1):
            answer.append(list[i]+list[i+1])
        answer.append(1)
        n -= 1
        return pascal(answer,n)
    if n == 1:
        return list

start_list=[1]
a=pascal(start_list, 8)
print("real_result",a)
