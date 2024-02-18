import numpy as np
import math

def format_value(value):
    formated_value = "{:.2f}".format(value)
    return formated_value
def entered_function(x):
    return (2 * x * math.exp(x**2))-5

def funс_diff_1(x):
    return ((4*x**2)+2)*math.exp(x**2)

def funс_diff_2(x):
    return ((12*x)+8*(x**3))*math.exp(x**2)

def scanning(start, end, step):
    x = start
    while x <= end:
        if np.sign(entered_function(x)) != np.sign(entered_function(x + step)):
            return x, x + step
        x += step

def print_range(start, end):
    for i in range(start, end):
        print("|f(" + str(i) + ")\t|" + str(entered_function(i)), end="|\n")

def print_subrange(start, end, step):
    current_value = start
    x_steps = []
    current_y_string = []
    current_y_def_string = []
    current_y_2_def_string = []
    while current_value < end:
        current_y_string.append(format_value(entered_function(current_value)))
        current_y_def_string.append(format_value(funс_diff_1(current_value)))
        current_y_2_def_string.append(format_value(funс_diff_2(current_value)))
        x_steps.append(str(format_value(current_value)))
        current_value += step
    print(" ")
    print("| x | " + " |\t".join(x_steps) + "\t| ")
    print("| y | " + " |\t".join(current_y_string) + "\t| ")
    print("| y'| " + " |\t".join(current_y_def_string) + "\t| ")
    print("|y''| " + " |\t".join(current_y_2_def_string) + "\t| ")

def check_diff(x):
    return funс_diff_1(x) * funс_diff_2(x) > 0

def chorde_method(x1, x2, accuracy):
    print(" ")
    print("||| Метод Хорд |||")
    if check_diff(float(x1)):
        print(" ")
        print("y' * y'' > 0")
        print("Використовую формулу 'а'\n")
        return chorde_method_a(x1, x2, accuracy)
    else:
        print(" ")
        print("y' * y'' < 0")
        print("Використовую формулу 'b'\n")
        return chorde_method_b(x1, accuracy)
def chorde_method_a(x1, x2, accuracy):
    i = 1
    res = x1
    m = x2
    prev_res = 0
    while abs(res - prev_res) > accuracy:
        prev_res = res
        res = prev_res - (entered_function(prev_res) * (m - prev_res))/(entered_function(m) - entered_function(prev_res))
        print(f"a{i} = {res}")
        print(f"({res}) - ({prev_res}) = {res - prev_res} < {accuracy}")
        i += 1
    return print(f"\nАпроксимований корінь: {res} \nПохибка обрахування: {entered_function(res)}")

def chorde_method_b(x1, accuracy):
    i = 1
    res = x1
    m = x1
    prev_res = 0
    while abs(res - prev_res) > accuracy:
        prev_res = res
        res = prev_res - (entered_function(prev_res) * (prev_res - m))/(entered_function(prev_res) - entered_function(m))
        print(f"a{i} = {res}")
        print(f"({res}) - ({prev_res}) = {res - prev_res} < {accuracy}")
        i += 1
    return print(f"\nАпроксимований корінь: {res} \nПохибка обрахування: {entered_function(res)}")

def tangents_method(x1, x2, accuracy):
    print(" ")
    print("||| Метод Дотичних |||")
    if check_diff(float(x1)):
        print(" ")
        print("y' * y'' > 0")
        print("Використовую формулу 'b'\n")
        return tangents_method_b(x2, accuracy)
    else:
        print(" ")
        print("y' * y'' < 0")
        print("Використовую формулу 'a'\n")
        return tangents_method_a(x1, accuracy)

def tangents_method_a(x1, accuracy):
    i = 1
    res = x1
    prev_res = 0
    while abs(res - prev_res) > accuracy:
        prev_res = res
        res = prev_res - entered_function(prev_res) / funс_diff_1(prev_res)
        print(f"a{i} = {res}")
        print(f"({res}) - ({prev_res}) = {res - prev_res} < {accuracy}")
        i += 1
    return print(f"\nАпроксимований корінь: {res} \nПохибка обрахування: {entered_function(res)}")

def tangents_method_b(x2, accuracy):
    i = 1
    res = x2
    prev_res = 0
    while abs(res - prev_res) > accuracy:
        prev_res = res
        res = prev_res - entered_function(prev_res)/funс_diff_1(prev_res)
        print(f"a{i} = {res}")
        print(f"({res}) - ({prev_res}) = {res - prev_res} < {accuracy}")
        i += 1
    return print(f"\nАпроксимований корінь: {res} \nПохибка обрахування: {entered_function(res)}")

def iterations_method(x, accuracy):
    print(" ")
    print("||| Метод Простих ітерацій |||")
    diff = funс_diff_1(x)
    print(f"\n-2 < {diff} * m < 0")
    m = 2.0 / diff
    print(f"{m} < m < 0")
    m = m * -1
    print(f"0 < m < {m}\n" f"m = {m}")
    i = 1
    res = x
    prev_res = 0
    while abs(res - prev_res) > accuracy and i<=20:
        print(f"{res} + {m} * f({res}) =")
        prev_res = res
        res = res + m * entered_function(res)
        print(res)
        i += 1

    if i <= 20:
        print(f"\nАпроксимований корінь: {res}\nПохибка обрахування: {res - prev_res}")

    elif i > 20:
        print(f"Не вдалося відшукати корінь з необхідною точністю за 20 ітерацій.\n"
        f"Коренем рівняння буде x = {res}\n"
        f"Абсолютна похибка: {entered_function(res)}")
        return res

if __name__ == "__main__":
    print("Комп'ютерний практикум №1 \nВаріант №11 \nстудент групи ПБ-21 \nРозумняк Руслан")
    accuracy = 0.0001
    print("-------------------------")
    print("||| Метод Сканування |||")
    print(" ")
    print_range(-5, 6)
    x1, x2 = scanning(-5, 6, 1)
    print("")
    print(f"Частковий інтервал: {x1, x2}")
    print_subrange(x1, x2, 0.1)
    sub_x1, sub_x2 = scanning(x1, x2, 0.1)
    print(" ")
    print(f"Наближений інтервал: {float(format_value(sub_x1)), float(format_value(sub_x2))}")
    print("-------------------------")
    chorde_method(float(format_value(sub_x1)), float(format_value(sub_x2)), accuracy)
    print("-------------------------")
    tangents_method(sub_x1, sub_x2, accuracy)
    print("-------------------------")
    iterations_method(1, accuracy)
