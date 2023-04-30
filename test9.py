#input 값
s1=["meosseugi", "1234"]
s2=[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]
# result= "login"
# s1=["programmer01", "15789"]
# s2=[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]
# result= "wrong pw"
# s1=["rabbit04", "98761"]
# s2=	[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]
# result= "fail"

# 1. s2의값이 s1에 있으면 login
i=True
if s1 in s2:
    print("login")
    i = False
# 2. 아이디만 같으면 wrong pw
for se_el in s2:
    if s1[0] == se_el[0] and s1[1] != se_el[1]:
        print("아이디만")
        i = False

       
# 3. 아이디가 존재 하지 않으면 fail
if i : 
    print("fail") 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
########################################################
#1. 아이디 비교
#2. 비밀번호 비교
i=False
for se_el in s2:
    if s1[0] == se_el[0]:
        #비번
        if s1[1] == se_el[1]:
            print("login")
        else:
            print("wrong pw")
    else:
        i = True
if i : 
    print("fail") 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
