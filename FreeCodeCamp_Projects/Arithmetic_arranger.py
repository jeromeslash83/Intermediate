def arithmetic_arranger(problems, second_arg=None):
    upper_all = []
    lower_all = []
    lines_all = []
    ans_all = []
    if len(problems) <6:
        for item in problems:
            divided = item.split()
            upper = divided[0]
            operator = divided [1]
            lower = divided[2]
            line_length= max(len(divided[0]), len(divided[2])) + 2
            lines = ''
            for n in range(line_length):
                lines += '-'
            try:
                if len(upper) < 5 and len(lower) < 5:
                    if operator == '+':
                        answer = str(int(upper) + int(lower))
                    elif operator == '-':
                        answer = str(int(upper) - int(lower))
                    else:
                        return "Error: Operator must be '+' or '-'."
                else:
                    return "Error: Numbers cannot be more than four digits."
            except:
                return "Error: Numbers must only contain digits."
            if second_arg == True:
                upper_all.append(upper.rjust(line_length))
                lower_all.append(operator + lower.rjust(line_length - 1))
                lines_all.append(lines)
                ans_all.append(answer.rjust(line_length))
            else:
                upper_all.append(upper.rjust(line_length))
                lower_all.append(operator + lower.rjust(line_length - 1))
                lines_all.append(lines)
    else:
        return 'Error: Too many problems.'
    if second_arg == True:
        return f"{'   '.join(upper_all)}{chr(10)}{'   '.join(lower_all)}{chr(10)}{'   '.join(lines_all)}{chr(10)}{'   '.join(ans_all)}"
    else:
        return f"{'   '.join(upper_all)}{chr(10)}{'   '.join(lower_all)}{chr(10)}{'   '.join(lines_all)}"
