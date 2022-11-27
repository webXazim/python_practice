txt_1 = "Do you even know what numbers are? Stay focused!"
txt_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
txt_3 = "Yeah... division by zero. Smart move..."
txt_4 = "Do you want to store the result? (y / n):"
txt_5 = "Do you want to continue calculations? (y / n):"

memory = 0


def is_one_digit(number):
    return -10 < number < 10 and number.is_integer()


def check(operand_1, operator, operand_2):
    txt = ''
    txt += " ... lazy" if is_one_digit(operand_1) and is_one_digit(operand_2) else ''
    txt += " ... very lazy" if (operand_1 == 1 or operand_2 == 1) and operator == '*' else ''
    txt += " ... very, very lazy" if (operand_1 == 0 or operand_2 == 0) and (operator in '*+-') else ''
    txt = "You are" + txt if txt != '' else ''
    print(txt)


while True:
    print("Enter an equation")
    x, oper, y = input().split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory

    try:
        num_1 = float(x)
        num_2 = float(y)
    except ValueError:
        print(txt_1)
    else:
        if oper in '+-*/':
            check(num_1, oper, num_2)
            if oper == '/' and num_2 == 0:
                print(txt_3)
            else:
                if oper == '+':
                    result = num_1 + num_2
                elif oper == '-':
                    result = num_1 - num_2
                elif oper == '*':
                    result = num_1 * num_2
                elif oper == '/':
                    result = num_1 / num_2
                print(result)
                print(txt_4)
                save_answer = input()
                if save_answer == 'y':
                    if is_one_digit(result):
                        txt_10 = "Are you sure? It is only one digit! (y / n)"
                        txt_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
                        txt_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

                        print(txt_10)
                        one_digit_not = input()
                        if one_digit_not == 'y':
                            print(txt_11)
                            add_in_memory = input()
                            if add_in_memory == 'y':
                                print(txt_12)
                                sure = input()
                                if sure == 'y':
                                    memory = result
                                    print(txt_5)
                                    calc_again = input()
                                    if calc_again == 'y':
                                        continue
                                    elif calc_again == 'n':
                                        break
                            elif add_in_memory == 'n':
                                print(txt_5)
                                calc_again = input()
                                if calc_again == 'y':
                                    continue
                                elif calc_again == 'n':
                                    break
                    else:
                        print(txt_5)
                        memory = result
                elif save_answer == 'n':
                    print(txt_5)
                calc_again = input()
                if calc_again == 'y':
                    pass
                elif calc_again == 'n':
                    break
        else:
            print(txt_2)

