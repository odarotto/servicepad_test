
def answer_1(numbers: list=None) -> list:
    results = list()
    numbers = range(1, 101) if not numbers else numbers
    for n in numbers:
        if n % 3 == 0 and n % 5 == 0:
            results.append('fizz buzz')
        elif n % 3 == 0:
            results.append('fizz')
        elif n % 5 == 0:
            results.append('buzz')
        else:
            results.append(n)
    return results

def answer_2(number=None) -> int:
    if not number:
        if number != 0:
            number = int(input('Ingrese una posición Fibonacci: '))
    if number == 0 or number == 1:
        return number
    return answer_2(number=number-1) + answer_2(number=number-2)

def answer_3(text: str=None) -> dict:
    result = dict()
    if not text:
        text = input('Ingrese un texto: ')
    for word in text.replace('\n', ' ').lower().split(' '):
        if word != '':
            if word in result.keys():
                result[word] += 1
            else:
                result[word] = 1
    return result



if __name__ == '__main__':
    print('[!] Running answer 1...')
    print(answer_1())
    print('[!] Running answer 2...')
    print(answer_2())
    print('[!] Running answer 3...')
    print(answer_3())