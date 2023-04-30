# 4개가 같은지 확인하는 함수
def board_check(a, b, board):
    board_element = board[a][b]
    if board_element == "0":
        return False
    elif board_element != board[a+1][b]:
        return False
    elif board_element != board[a][b+1]:
        return False
    elif board_element != board[a+1][b+1]:
        return False
    else:
        return True


# 지울 위치를 찾는 함수
def loop_check(m, n, board):
    count_list = [[0 for w in range(n)] for h in range(m)]
    for a in list(range(0, m-1)):
        for b in list(range(0, n-1)):
            if board_check(a, b, board):
                count_list[a][b] = 1
                count_list[a+1][b] = 1
                count_list[a][b+1] = 1
                count_list[a+1][b+1] = 1
    # result = sum(sum(row) for row in count_list)
    return count_list


# 지우는 요소의 개수를 세는 함수
def sum_count(count_list):
    result = sum(sum(row) for row in count_list)
    return result


# 지우면서 아래로 내리는 함수
def let_down(count_list, m, n, board):
    for j in range(n):
        temp_list = ["0" for h in range(m)]
        count = m-1
        for i in reversed(range(m)):
            if count_list[i][j] == 0:
                temp_list[count] = board[i][j]
                count -= 1
        for i in range(m):
            temp_board = list(board[i])
            temp_board[j] = temp_list[i]
            board[i] = ('').join(temp_board)
    return board


def solution(m, n, board):
    answer = 0
    while True:
        count_list = loop_check(m, n, board)
        if sum_count(count_list) == 0:
            break
        answer += sum_count(count_list)
        board = let_down(count_list, m, n, board)
    return answer
