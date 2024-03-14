def solve_method(string):
    str_list = string.split(",")
    taskA = int(str_list[0])
    taskB = int(str_list[1])
    num = int(str_list[2])

    result = []
    for i in range(num + 1):
        total_time = i * taskA + (num - i) * taskB
        result.append(total_time)

    return sorted(list(set(result)))


if __name__ == '__main__':
    # assert solve_method("1,2,3") == [3, 4, 5, 6]
    print(solve_method("1,2,3"))


