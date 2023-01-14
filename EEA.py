


def EEA(a, b):
    r_1 = a
    r_2 = b
    t_1 = 0
    t_2 = 1

    while(r_2 != 0):
        q = r_1 // r_2
        r = r_1 % r_2
        t = t_1 - t_2 * q
        #Shift
        r_1 = r_2
        r_2 = r
        t_1 = t_2
        t_2 = t
    if r_1 != 1:
        return "Not Coprime, no solution"
    if(t_1 < 0):
        answer = a + t_1
        return answer
    return t_1        



def main():
    inv = EEA(40, 3)
    print(inv)


if __name__ == "__main__":
   main()    
# RESULT = 34807