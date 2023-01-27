import random


# generates the problems and return the useful values
def addends():
    denominator = random.randint(3, 12)
    numerator1 = random.randint(1, denominator)
    numerator2 = random.randint(1, denominator)
    fraction1 = str(numerator1) + "/" + str(denominator)
    fraction2 = str(numerator2) + "/" + str(denominator)
    question = fraction1 + " + " + fraction2 + "="
    return question, numerator1, numerator2, denominator


# solves the problem as proper fraction or mixed number solution
def answer(numerator1, numerator2, denominator):
    solution_numerator = numerator1 + numerator2
    if solution_numerator <= denominator:
        solution_correct = (str(solution_numerator) + "/" + str(denominator))
    else:
        whole_number = solution_numerator // denominator
        mixed_numerator = solution_numerator % denominator
        solution_correct = (str(whole_number) + " and " + str(mixed_numerator) + "/" + str(denominator))

    return solution_correct

for i in range(100):
    question, numerator1, numerator2, denominator = addends()
    solution_correct = answer(numerator1, numerator2, denominator)
    print(question)
    print(solution_correct)
    print()
