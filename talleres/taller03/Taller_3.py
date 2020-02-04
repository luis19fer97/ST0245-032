def hanoi(n, a = "Tower 1", b = "Tower 2", c = "Tower 3"):
    if n == 1:
        print ("From " + a + " to " + c)
    else:
        hanoi(n - 1, a, c , b )
        print ("From " + a + " to " + c)
        hanoi(n - 1, b, a, c )
