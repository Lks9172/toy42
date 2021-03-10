def solution(name):
    answer = 0
    start = ['A'] * len(name)
    index = 0
    name = list(name)
    while True:
        if name == start:
            break

        if name[index] != 'A':
            answer = answer + min(ord(name[index]) - ord('A'), -ord(name[index]) + ord('Z'))
            name[index] = 'A'

        left = 1
        right = 1

        for i in range(1, len(name)):
            if name[index + i] == 'A':
                right += 1
            else:
                break
        for i in range(1, len(name)):
            if name[index - i] == 'A':
                left += 1
            else:
                break
        if left < right:
            answer += left
            index -= left
        else:
            answer += right
            index += right

    return answer

priorities = [93, 30, 55]
location = [1, 30, 5]
print(solution("JEROEN"),'\n')


priorities = [95, 90, 99, 99, 80, 99]
location = [1, 1, 1, 1, 1, 1]
print(solution("JAN"))
