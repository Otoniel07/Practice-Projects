def error_handling(num1, num2, operator):
    if not (num1.isdecimal() and num2.isdecimal()):
        return "Error: Numbers must only contain digits."
    elif len(num1) > 4 or len(num2) > 4:
        return "Error: Numbers cannot be more than four digits."
    elif operator != '+' and operator != '-':
        return "Error: Operator must be '+' or '-'."
    else:
        return ""

def arithmetic_arranger(problems, mode = False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    line1 = line2 = line3 = line4 = ""
    first = True
    
    for problem in problems:
        parts = problem.split()
        num1 = parts[0]
        operator = parts[1]
        num2 = parts[2]
        
        check_errors = error_handling(num1, num2, operator)
        if check_errors != "":
            return check_errors
        
        int1 = int(num1)
        int2 = int(num2)
        spacing = max(len(num1), len(num2))
        
        if first == True:
            line1 += num1.rjust(spacing + 2)
            line2 += operator + ' ' + num2.rjust(spacing)
            line3 += '-' * (spacing + 2)
            
            if operator == '+':
                line4 += str(int1 + int2).rjust(spacing + 2)
            elif operator == '-':
                line4 += str(int1 - int2).rjust(spacing + 2)
            
            first = False
            
        else:
            line1 += num1.rjust(spacing + 6)
            line2 += operator.rjust(5) + ' ' + num2.rjust(spacing)
            line3 += '    ' + '-' * (spacing + 2)
            
            if operator == '+':
                line4 += '    ' + str(int1 + int2).rjust(spacing + 2)
            elif operator == '-':
                line4 += '    ' + str(int1 - int2).rjust(spacing + 2)
        
    if mode == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    else:
        return line1 + '\n' + line2 + '\n' + line3