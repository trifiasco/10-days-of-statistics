

def take_input():
    n = int(input())
    x = list(map(int, input().strip().split(' ')))
     
    w = list(map(int, input().strip().split(' ')))

    res = 0
    for xi,wi in zip(x,w):
        res += xi * wi
    res = res / sum(w) 
    print(res)
    return

if __name__ == '__main__':
    take_input()
