import itertools
######## input##################

expression = "100-200*300-500+20"
# expression = "50*6-3*2"

#############################
# 1. expression 숫자 리스트와 연산 리스트 뽑기
# import re
# b =re.split('[^0-9]',expression)

# print("야롱",b)

# a = expression.replace('*','-').replace('+','-')
# print(a)
# a = a.split('-')
# print(a)

def_n_list = []
def_a_list = []
lists = ''
# for num in expression:
#   if num.isdigit():
#     n_list.append(num)

# print(n_list)
for i in expression:
    if i.isdigit():
        lists += i
    else:
        def_a_list.append(i)
        def_n_list.append(int(lists))
        lists = ''
def_n_list.append(int(lists))
print("1.n_list", def_n_list, def_a_list)

# 함수


# def d_minus(a_list, n_list):
#     c_list = []
#     first_c = True
#     c = 0
#     c_place = 0
#     for n in range(len(a_list)):
#         if a_list[n] == '-':
#             print(c)
#             if (first_c):
#                 c = c+n_list[n]
#             c = c-n_list[n+1]
#             first_c = False
#             print(c)
#         else:
#             c = n_list[n]
#             c_place += 1

#         if len(c_list) == c_place+1:
#             c_list[c_place] = c
#         else:
#             c_list.append(c)
#             c = 0
#     for i in a_list[::]:
#         if '-' in a_list:
#             a_list.remove('-')

#     return c_list, a_list


# def d_plus(a_list, n_list):
#     c_list = []
#     first_c = True
#     c = 0
#     c_place = 0
#     for n in range(len(a_list)):
#         if a_list[n] == '+':
#             if (first_c):
#                 c = c+n_list[n]
#             c = c+n_list[n+1]
#             first_c = False

#         else:
#             c = n_list[n]
#             c_place += 1

#         if len(c_list) == c_place+1:
#             c_list[c_place] = c
#         else:
#             c_list.append(c)
#             c = 0
#     for i in a_list[::]:
#         if '+' in a_list:
#             a_list.remove('+')
#     return c_list, a_list

def d_minus(a_list, n_list):
    del_list = []
    for i in range(len(a_list)):
        if a_list[i] == "-":
            n_list[i+1] = n_list[i]-n_list[i+1]
            del_list.append(i)
    for del_el in reversed(del_list):
        del a_list[del_el]
        del n_list[del_el]
    return a_list, n_list


def d_plus(a_list, n_list):
    del_list = []
    for i in range(len(a_list)):
        if a_list[i] == "+":
            n_list[i+1] = n_list[i]+n_list[i+1]
            del_list.append(i)
    for del_el in reversed(del_list):
        del a_list[del_el]
        del n_list[del_el]
    return a_list, n_list


def d_mul(a_list, n_list):
    del_list = []
    for i in range(len(a_list)):
        if a_list[i] == "*":
            n_list[i+1] = n_list[i]*n_list[i+1]
            del_list.append(i)
    for del_el in reversed(del_list):
        del a_list[del_el]
        del n_list[del_el]
    return a_list, n_list


# n_list = [100, 200, 300, 500, 20]
# a_list = ['-', '-', '-', '+']

# print(d_minus(a_list, n_list))
# 1. * > - > _+
# 계산 우선순위
cal_list = ['*', '-', '+']
cal_lists = list(itertools.permutations(cal_list))
cal_dict = {
    '*': d_mul,
    '-': d_minus,
    '+': d_plus
}

# 계산
answer = 0
for cal_list in cal_lists:
    n_list = def_n_list[:]
    a_list = def_a_list[:]
    print("~~~~~~~~~~~~~~~")
    print(cal_list)
    for i in cal_list:
        if i in a_list:
            print("n_list_f", n_list)
            result = cal_dict[i](a_list, n_list)
            a_list = result[0]
            n_list = result[1]
            print("n_list", n_list)
            print("a_list", a_list)
    if (answer < abs(n_list[0])):
        answer = abs(n_list[0])
print(answer)
