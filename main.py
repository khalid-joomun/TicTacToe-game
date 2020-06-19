cells = [A1, A2, A3, B1, B2, B3, C1, C2, C3]
A1 = ""
A2 = ""
A3 = ""
B1 = ""
B2 = ""
B3 = ""
C1 = ""
C2 = ""
C3 = ""


def play(box):
    if (box == "A1"):
        A1 = "X"
    elif (box == "A2"):
        A2 = "X"
    elif (box == "A3"):
        A3 = "X"
    elif (box == "B1"):
        B1 = "X"
    elif (box == "B2"):
        B2 = "X"
    elif (box == "B3"):
        B3 = "X"
    elif (box == "C1"):
        C1 = "X"
    elif (box == "C2"):
        C2 = "X"
    else:
        C3 = "X"


def grid():
    print("   A\tB\tC")
    print("1  ", A1, "\t", B1, "\t", C1)
    print("2  ", A2, "\t", B2, "\t", C3)
    print("3  ", A3, "\t", B3, "\t", C3)


grid()
