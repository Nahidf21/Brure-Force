def factorial(M):
    res = 1
    for k in range(1, M+1):
        res = res * k
    return  res


def nmicrosecondsperyear():
    return 1 * 365 * 24 * 60 * 60 * 1000000

def nmicrosecondsperday():
    return 24 * 60 * 60 * 1000000

# choices can be repeated
# there are M choices
# and a password can have N positions
def npermutations(M, N):
    return pow(M, N)


def main():
    # number of choices
    M = 66

    # number of positions
    N = 10

    nper = npermutations(M, N)
    ndaysneeded = nper / nmicrosecondsperday()
    nyearsneeded = nper / nmicrosecondsperyear()

    print(f"Number of permutations: {nper}")
    print(f"Number of days needed: {ndaysneeded}")
    print(f"Number of years needed: {nyearsneeded}")

main()