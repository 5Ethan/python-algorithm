def solve_method(newspaper, anonymousLetter):
    newspaper_list = [sorted(l) for l in newspaper]
    anonymous_letter_list = [sorted(l) for l in anonymousLetter]

    for letter in anonymous_letter_list:
        if letter not in newspaper_list:
            return False

    return True


if __name__ == '__main__':
    newspaper = ["ab", "cd"]
    anonymousLetter = ["ab"]
    assert solve_method(newspaper, anonymousLetter) is True

    newspaper = ["ab", "ef"]
    anonymousLetter = ["aef"]
    assert solve_method(newspaper, anonymousLetter) is False

    newspaper = ["ab", "bcd", "ef"]
    anonymousLetter = ["cbd", "fe"]
    assert solve_method(newspaper, anonymousLetter) is True

    newspaper = ["ab", "bcd", "ef"]
    anonymousLetter = ["cb", "fe"]
    assert solve_method(newspaper, anonymousLetter) is False
