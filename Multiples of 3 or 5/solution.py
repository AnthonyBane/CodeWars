def solution(number):
    if number < 0:
        return 0
    return sum(num for num in range(0,number) if not num % 3 or not num % 5)