from divide_and_mul import mul, divide

 main() -> None:
    a = float(input())
    b = float(input())
    print(sub(a, b))
    print(summ(a, b))
    print(divide(a, b))
    print(mul(a, b))


def summ(a: float, b: float) -> float:
    return a + b


def sub(a: float, b: float) -> float:
    return a - b

main()