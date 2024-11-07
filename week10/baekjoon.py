
x_array, y_array = map(int, input().split())
input_list = [0 for i in range(x_array)]
cnt = 0
r_place = []
b_place = []
o_place = []
default_around = [[0, 1], [0, -1], [-1, 0], [1, 0]] # -> <- ^ V
check_around_r = [[0, 0], [0, 0], [0, 0], [0, 0]]
check_around_b = [[0, 0], [0, 0], [0, 0], [0, 0]]

def update_around_r(obj_place):
    for i in range(len(check_around_r)):
        check_around_r[i][0] = default_around[i][0] + obj_place[0]
        check_around_r[i][1] = default_around[i][1] + obj_place[1]

def update_around_b(obj_place):
    for i in range(len(check_around_b)):
        check_around_b[i][0] = default_around[i][0] + obj_place[0]
        check_around_b[i][1] = default_around[i][1] + obj_place[1]

for k in range(y_array):
    input_list[k] = list(input())

for i in range(x_array):
    for j in range(y_array):
        if input_list[i][j] == 'R':
            r_place.append(i)
            r_place.append(j)
        if input_list[i][j] == 'B':
            b_place.append(i)
            b_place.append(j)
        if input_list[i][j] == 'O':
            o_place.append(i)
            o_place.append(j)

for i in range(len(check_around_r)):
    if input_list[check_around_r[i][0]][check_around_r[i][0]] == '.' and r_place[0] > check_around_r[i][0]:
        r_place[0] -= 1
    
    if input_list[check_around_r[i][0]][check_around_r[i][1]] == '.' and r_place[1] > check_around_r[i][1]:
        r_place[1] -= 1

print(r_place)
update_around_r(r_place)
update_around_b(b_place)
print(check_around_r)
print(check_around_b)

