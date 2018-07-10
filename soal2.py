def pascal(n,r=[]):
    for x in range(n):
        l = len(r)
        r = [1 if i == 0 or i == l else r[i-1]+r[i] for i in range(l+1)]
        yield r

def create_triangle(n):
    ps = list(pascal(n))
    max = len(' '.join(map(str,ps[-1])))
    for p in ps:
        print(' '.join(map(str,p)).center(max)+'\n')


if __name__ == '__main__':
    create_triangle(5)