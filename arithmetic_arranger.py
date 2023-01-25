def arithmetic_arranger(math,should_answer = False):

    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    output = ''

    arranged_problems = ''

    for equation in math:

        ans = ''
        element = equation.split(" ")
        num_eq = len(math)

        if num_eq > 5:
            return("Error: Too many problems.")
            break


        if element[1] != ("+") and element[1] != ("-"):
            return("Error: Operator must be '+' or '-'.")
            break

        if element[0].isdigit() == False or element[2].isdigit() == False:
            return("Error: Numbers must only contain digits.")
            break

        if len(element[0]) > 4 or len(element[2]) > 4:
            return("Error: Numbers cannot be more than four digits.")
            break

        space = 2+max(len(element[0]),len(element[2]))

        element[0] = element[0].rjust(space, " ")

        line1 += element[0]
        line2 += element[1] + element[2].rjust(space-1, " ")

        for i in range(space):
            line3 += "-"

        if equation != math[num_eq-1]:
            line1 += '    '
            line2 += '    '
            line3 += "    "

        arranged_problems = line1 + '\n' + line2 + '\n' + line3

        if should_answer == True:
            if element[1] == "+":
                ans += str(int(element[0]) + int(element[2]))
                ans = ans.rjust(space, " ")
                line4 += ans
                arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
            else:
                ans += str(int(element[0]) - int(element[2]))
                ans = ans.rjust(space, " ")
                line4 += ans
                arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
        if equation != math[num_eq-1]:
            line4 += "    "

    return arranged_problems