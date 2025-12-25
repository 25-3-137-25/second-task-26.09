from functions import *
from visual import *

FUNCTIONS = {
    '1': ('sin', sin),
    '2': ('cos', cos),
    '3': ('exp', exp),
    '4': ('quadratic', quadratic),
    '5': ('obr_proporc', obr_proporc)
}


def main():
    print("Введите а, б и шаг h")

    a = float(input("a: "))
    b = float(input("b: "))
    h = float(input("шаг h: "))

    print("\nФункции:")
    for key, (name, _) in FUNCTIONS.items():
        print(f"{key}. {name}")

    choice = input("\nВыберите функцию: ")

    func_name, func = FUNCTIONS[choice]

    x = []
    y = []
    current = a
    while current <= b + h / 100:
        x.append(current)
        y.append(func(current))
        current += h

    print_table(x, y)
    plot_graph(x, y, func_name)
    print(f"\n{func_name} на [{a}, {b}] шаг {h}")


if __name__ == "__main__":
    main()
