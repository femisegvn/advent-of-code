import operator

def part1(input):
    with open(input, 'r') as f:
        lines = []
        for line in f.readlines():
            line = line.strip("\n").split()
            if len(line) != 0:
                lines.append(line)

    answers = []
    for problem in zip(*lines):
        op = problem[-1]

        match op:
            case "+":
                op = operator.add
            case "*":
                op = operator.mul

        problem = problem[:-1]
        
        answer = None

        for var in problem:
            answer = op(answer, int(var)) if answer is not None else int(var)
        
        answers.append(answer)

    output = sum(answers)

    return output

def part2(input):
    with open(input, 'r') as f:
        lines = []
        for line in f.readlines():
            line = line.strip("\n")
            if len(line) != 0:
                lines.append(line)

    columns = []
    for column in zip(*lines):
        columns.append(column)
    
    problems = []
    problem = []

    for i, column in enumerate(reversed(columns)):
        if ''.join(column).isspace():
            problems.append(problem)
            problem = []
        else:
            col = ''

            for c in column:
                col += c
            problem.append(col)

            if i == len(columns) -1:
                problems.append(problem)

    answers = []
    
    for problem in problems:
        op = problem[-1][-1]
        problem[-1] = problem[-1].rstrip(op)

        match op:
            case "+":
                op = operator.add
            case "*":
                op = operator.mul
        
        answer = None
        for var in problem:
            answer = op(answer, int(var)) if answer is not None else int(var)
        
        answers.append(answer)

    output = sum(answers)

    return output