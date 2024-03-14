def solve_method(line):
    result = ""
    # 使用临时字符串存储单词
    words = ""
    for char in line:
        # 检查一个字符是否为字母（即英文字母）
        if char.isalpha():
            words += char
        else:
            # 将单词逆序
            result += words[::-1]
            words = ""
            result += char

    return result

if __name__ == '__main__':
    s = "yM eman si boB."
    assert solve_method(s) == "My name is Bob."

    s = "woh era uoy ? I ma enif."
    assert solve_method(s) == "how are you ? I am fine."
