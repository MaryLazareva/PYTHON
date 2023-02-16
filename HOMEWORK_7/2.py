def print_operation_table(operation, num_rows, num_columns):
    for i in range(1 , num_rows + 1):
        list = []
        for j in range(1, num_columns + 1):
            list.append(i * j)
        print(*list)    

print_operation_table(lambda x, y: x * y, int(input('row: ')), int(input('column: '))) 