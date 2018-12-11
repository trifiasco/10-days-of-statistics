
def getMedian(data_set):
    n = len(data_set)
    mid = n // 2

    if n & 1:
        return data_set[mid]
    else:
        return (data_set[mid] + data_set[mid - 1]) / 2.0

def getInterQuartileRange(data_set):
    n = len(data_set)
    mid = n // 2
    
    if n & 1:
        q1 = getMedian(data_set[:mid])
        q3 = getMedian(data_set[mid + 1 :])
        return q3 - q1
    else:
        q1 = getMedian(data_set[:mid])
        q3 = getMedian(data_set[mid :])
        return q3 - q1
    
def input_and_process():
    n = int(input())
    elements = list(map(int, input().strip().split(' ')))
    frequencies  = list(map(int, input().strip().split(' ')))

    data_set = []

    for element, frequency in zip(elements, frequencies):
        data_set.extend([element] * frequency)

    data_set.sort()
    print(round(float(getInterQuartileRange(data_set)), 1))


if __name__ == '__main__':
    input_and_process()
