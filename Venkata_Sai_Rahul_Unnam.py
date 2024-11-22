def function(n):
    if n < 0:
        return "Factorial is not defined."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

  print(function(5))
