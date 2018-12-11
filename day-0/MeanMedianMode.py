from collections import Counter

def take_input():
    n = int(input())
    data_set = list(map(int, input().strip().split(' ')))
    return data_set

def process_and_output(data_set):
    n = len(data_set)
    total =  sum(data_set)

    print(total / n)

    data_set.sort()
    mid = n // 2;
    if n & 1:
        print(data_set[mid])
    else:
        print((data_set[mid] + data_set[mid - 1])/2.0);
    
    mode = Counter(data_set).most_common(1)[0][0]
    print(mode)

if __name__ == '__main__':
    data_set = take_input()

    process_and_output(data_set);
