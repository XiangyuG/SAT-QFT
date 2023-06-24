import sys
def main(argv):
    if len(argv) != 3:
        print("Usage: python3", argv[0], "<# step> <# qubits>")
        exit(1)
    N=int(argv[1])
    n = int(argv[2])

    option_num = 5
    #{{C000, C001, C002, C003, C004, C005, C006, C007},{C010, C011, C012, C013, C014, C015, C016, C017},{C020, C021, C022, C023, C024, C025, C026, C027},{C030, C031, C032, C033, C034, C035, C036, C037}},

    # int[2] arr = {0,1};
    tmp_str = "int[" + str(n) + "] arr = {"
    for i in range(n):
        tmp_str += str(i)
        if i != n - 1:
            tmp_str += ","
        else:
            tmp_str += "};"
    print(tmp_str)
    # int[2] pos = {0,1};
    tmp_str = "int[" + str(n) + "] pos = {"
    for i in range(n):
        tmp_str += str(i)
        if i != n - 1:
            tmp_str += ","
        else:
            tmp_str += "};"
    print(tmp_str)
    # int[2][2] I = {{0, 0}, {0, 0}};
    tmp_str = "int[" + str(n) + "]" + "[" + str(n) + "]" + " I = {"
    for i in range(n):
        new_str = "{"
        for j in range(n):
            new_str += "0"
            if j != n - 1:
                new_str += ","
            else:
                new_str += "}"
        if i != n - 1:
            new_str += ","
        tmp_str += new_str
    tmp_str += "};"
    print(tmp_str)

    # int[5][2][1]
    beg_str = "int[" + str(option_num) + "][" + str(n) + "][" + str(N) + "] gate_swap ="
    for i in range(N):    
        tmp_str =  "{"
        for j in range(n):
            tmp_str += "{"
            for k in range(option_num):
                tmp_str += "C_"+str(i)+"_"+str(j)+"_"+str(k)
                if k != option_num - 1:
                    tmp_str += ","
            tmp_str += "}"
            if j != (n - 1):
                tmp_str += ","
        tmp_str += "}"
        if i != N - 1:
            tmp_str += ","
        if i == 0:
            if i == N - 1:
                print(beg_str + "{" + tmp_str + "};")
            else:
                print(beg_str + "{" + tmp_str)
        elif i == N - 1:
            print(tmp_str + "};")
        else:
            print(tmp_str)
    print("-----------------------")
    for i in range(N):
        for j in range(n):
            tmp_str = ""
            for k in range(option_num - 1):
                tmp_str += "C_"+str(i)+"_"+str(j)+"_"+str(k)
                if k != option_num - 2:
                    tmp_str += "+"
                else:
                    tmp_str += "<=1"
            print("assert (" + tmp_str + ");")
    print("-----------------------")
    for i in range(N):
        for j in range(n):
            for k in range(option_num - 1):
                tmp_str = "int "+"C_"+str(i)+"_"+str(j)+"_"+str(k) + "= ??(1);"
                print(tmp_str)
            tmp_str = "int "+"C_"+str(i)+"_"+str(j)+"_"+str(option_num - 1) + "= ??;"
            print(tmp_str)
if __name__ == '__main__':
    main(sys.argv)