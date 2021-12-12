# We want to generate a function that computes the series starting from 0 and ending until the given number.
# Example:
# Input:
# > 6

# Output:
# 0+1+2+3+4+5+6 = 21

# Input:
# > -15

# Output:
# -15<0

# Input:
# > 0

# Output:
# 0=0

def show_sequence(n):
    final_answer = ""
    sum = 0

    if n < 0:
        final_answer = f"{n}<0"
    
    elif n == 0:
        final_answer = f"{n}=0"
    else:
        for numbers in range(0, n+1):
            sum += numbers
            if numbers == n:
                final_answer += f"{numbers}"
                break

            final_answer += f"{numbers}+"

        final_answer += f" = {sum}"

    return final_answer

print(show_sequence(0))
