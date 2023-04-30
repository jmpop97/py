# https://school.programmers.co.kr/learn/courses/30/lessons/172928#

park = ["SOO", "OOO", "OOO"]
routes = ["E 2", "S 2", "W 1"]


class DogP:
    def __init__(self, pl):
        self.place = pl

    def movedog(self, direction, park):
        # 방향설정
        match(direction[0]):
            case("E"):
                dir = [0, 1]
            case("W"):
                dir = [0, -1]
            case("S"):
                dir = [1, 0]
            case("N"):
                dir = [-1, 0]
            case __:
                dir = [0, 0]
        # 움직임 검사

        try:
            check_place_0 = self.place[0]
            check_place_1 = self.place[1]
            if check_place_0+dir[0]*int(direction[2]) >= 0 and len(park) > check_place_0+dir[0]*int(direction[2]):
                # print("1번")
                for i in list(range(int(direction[2]))):
                    if park[check_place_0+dir[0]*(i+1)][check_place_1] == "X":
                        # print("bug")
                        raise

            else:
                # print("2번")
                raise
            if check_place_1+dir[1]*int(direction[2]) >= 0 and len(park[0]) > check_place_1+dir[1]*int(direction[2]):
                # print("3번")
                for i in list(range(int(direction[2]))):
                    if park[check_place_0][check_place_1+dir[1]*(i+1)] == "X":
                        # print("bug")
                        raise
            else:
                # print("4번")
                raise
            # 블록이동
            # print("5번")
            self.place = [check_place_0 + dir[0] *
                          int(direction[2]), check_place_1+dir[1]*int(direction[2])]

        except:
            pass


def solution(park, routes):
    # 시작 좌표
    for i in park:
        if (i.find("S") >= 0):
            dogp = DogP([park.index(i), i.index("S")])
            print(type(dogp))
            for route_dir in routes:
                dogp.movedog(route_dir, park)
            break

    return dogp.place


print(solution(park, routes))
