from pandas import pandas as pd

print("로그인하세요!")
id = input("아이디 : ")
password = input("패스워드 : ")
File = pd.read_excel('pass.xlsx', header=None)
j = 0

for i in range(1, len(File)):
    if id == File[0][i]:
        j = j + 1
    if password == File[1][i]:
        j = j + 1
    else:
        j = 0

if j == 2:
    print("통과하셨습니다")
elif j == 1:
    print("id나 패스워드가 틀렸습니다")
else:
    print("어떻게 다 틀리냐고요 ㅋㅋ")