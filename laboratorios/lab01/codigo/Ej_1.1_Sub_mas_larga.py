
def lcs(X, Y):
    if len(X) == 0 or len(Y) == 0:
        return []
    if X[-1] == Y[-1]:
        return lcs(X[:-1], Y[:-1]) + [X[-1]]
    else:
        return Mas_larga(lcs(X, Y[:-1]), lcs(X[:-1], Y))


def Mas_larga(X, Y):
	return X if len(X) > len(Y) else Y

print("".join(lcs("ABCDGH","AEDFHR")))
