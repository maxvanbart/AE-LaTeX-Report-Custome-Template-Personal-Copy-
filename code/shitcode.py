
def isEven(n):
    txt = "def isEven(n):\n    if (n == 0):\n        out = True \n"
    for i in range(1, 2*n+1):
        txt += f"    if (n == {i}):\n        out = {bool(i%2)} \n"
    txt += "    return out"
    # print(txt)
    with open("ifstate.py", 'w') as file:
        file.write(txt)

    from ifstate import isEven
    return isEven(n)


print(isEven(1000))
