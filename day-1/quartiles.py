
def getMedian(data_set):
    n = len(data_set)
    mid = n // 2

    if n & 1:
        return data_set[mid]
    else:
        return (data_set[mid] + data_set[mid - 1])/2.0


def take_input_and_process():
    n = int(input())
    data_set = list(map(int, input().strip().split(' ')))

    data_set.sort()
    
    q2 = getMedian(data_set)

    mid = n // 2

    if n & 1:
        q1 = getMedian(data_set[: mid])
        q3 = getMedian(data_set[mid + 1 :])
    else:
        q1 = getMedian(data_set[: mid])
        q3 = getMedian(data_set[mid :])

    print(int(q1))
    print(int(q2))
    print(int(q3))

if __name__ == '__main__':
    take_input_and_process()
