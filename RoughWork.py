
safe_ones = 0
pawns = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}

for col, row in pawns:
    # print(col)
    # print(row)
    # print(str(int(row)-1))
    defender_row = str(int(row)-1)
    print(chr(ord(col)-1) + defender_row)
    print(chr(ord(col)+1) + defender_row)

    # if left_defender in pawns or right_defender in pawns:
    #     safe_ones += 1
