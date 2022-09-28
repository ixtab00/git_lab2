from divide_and_mul import mul, divide

def main() -> None:
    a = float(input())
    b = float(input())
    print(sub(a, b))
    print(summ(a, b))
<<<<<<< HEAD
=======
    print(divide(a, b))
>>>>>>> test-div-and-mul


def summ(a: float, b: float) -> float:
    return a + b


def sub(a: float, b: float) -> float:
    return a - b

main()