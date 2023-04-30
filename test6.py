arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]  # 3
# arrows = [5, 2, 7, 1, 6, 3]  # 3
# arrows = [6, 0, 3, 0, 5, 2, 6, 0, 3, 0, 5]  # 3


now = [0, 0]  # 현재좌표
dic_arrows = {
    0: [0, 1],
    1: [1, 1],
    2: [1, 0],
    3: [1, -1],
    4: [0, -1],
    5: [-1, -1],
    6: [-1, 0],
    7: [-1, 1]
}
path = {}


def check_dia(path, now, arrow):
    # print("-----------------------")
    c_now = now[:]
    c_arrow = arrow
    if c_arrow > 6:
        c_arrow -= 7
    else:
        c_arrow += 1
    c_now[0] += dic_arrows[c_arrow][0]
    c_now[1] += dic_arrows[c_arrow][1]

    if c_arrow > 2:
        c_arrow -= 3
    else:
        c_arrow += 5
    # print(c_now)
    # print(c_arrow)
    # print("-----------------------")
    try:

        c_check_list = path[str(c_now)]
        if c_arrow in c_check_list:
            return True
    except:
        pass
    # print("-----------------------")
    return False


def solution(arrows):
    result = 0
    for arrow in arrows:
        # 이동전
        inline = True
        dic_p = str(now)
        try:
            if arrow not in path[dic_p]:
                path[dic_p] = path[dic_p]+[arrow]
        except:
            path[dic_p] = [arrow]
        # 이동후
        now[0] += dic_arrows[arrow][0]
        now[1] += dic_arrows[arrow][1]
        if arrow > 3:
            arrow = arrow-4
        else:
            arrow = arrow+4

        dic_p = str(now)
        try:
            if arrow not in path[dic_p]:
                path[dic_p] = path[dic_p]+[arrow]
                result += 1
                inline = False
            else:
                inline = True

        except:
            path[dic_p] = [arrow]
            inline = False

        if (arrow % 2 == 1) and (not inline):
            result += check_dia(path, now, arrow)
    return result


print(solution(arrows))
