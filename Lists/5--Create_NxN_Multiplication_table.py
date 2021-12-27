# Your task, is to create NxN multiplication table, of size provided in parameter.

# for example, when given size is 3:

# 1 2 3
# 2 4 6
# 3 6 9
# for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]

def multiplication_table(size):
    dummy_list = []
    table = []

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            dummy_list.append(i*j)
            if len(dummy_list) % size == 0:
                table.append(list(dummy_list))
                dummy_list.clear()
                
    return table

print(multiplication_table(4))