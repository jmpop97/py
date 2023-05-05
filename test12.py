# https://www.acmicpc.net/problem/2745
# num = 35*36**4 + 35*36**3 + 35*36**2 + 35*36**1 + number_base[len_num-1-n]*base**n / ZZZZZ 36

input_value = input('')
number_base, base = input_value.split()
# EDCBA -> ABCDE
len_num = len(number_base)
num = 0
for n in range(len_num):
    # 숫자
    try:
        num += int(number_base[len_num-1-n])*int(base)**n
    # 문자
    except:
        num += (ord(number_base[len_num-1-n])-55)*int(base)**n
print(num)
try:
    int('asdf')
    print('a')
except:
    print('b')

# https://www.acmicpc.net/problem/8958
# 인풋이 OX니까  .split("X")한 뒤,
# .count("O")로 O의 연속된 갯수만큼 뽑아 등차수열의 합
input_value = '''5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX'''
num, *input_list = input_value.split('\n')
for ox in input_list:
    ox_split_list = ox.split('X')
    sum_o = 0
    for ox_split in ox_split_list:
        len_o = len(ox_split)
        sum_o += len_o*(len_o+1)/2
    print(int(sum_o))
a = []
a.append(1)
