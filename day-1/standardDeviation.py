
def Mean(data_set):
    return sum(data_set) / len(data_set)

def variance(data_set):
    mean = Mean(data_set)

    return sum((x - mean)**2 for x in data_set)/ len(data_set)

def standard_deviation(data_set):
    return variance(data_set) ** .5

if __name__ == '__main__':
    n = int(input())
    data_set = list(map(int, input().strip().split(' ')))

    print(round(float(standard_deviation(data_set)), 1))
