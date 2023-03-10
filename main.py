# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def load_input_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        #print(lines)
    split_lines = lines[0].split(" ")
    dim_x = int(split_lines[0])
    dim_y = int(split_lines[1])
    snake_num = int(split_lines[2])
    # print(dim_y)
    # print(dim_x)
    # print(snake_num)
    snake_lens = [int(l) for l in lines[1].split(" ")]
    # print(snake_lens)
    field_mat = [l.rstrip().split(" ") for l in lines[2:]]
    # print(field_mat)
    return dim_x, dim_y, snake_num, snake_lens, field_mat

def create_output_file(filename,output):
    f = open(filename,"w")
    for mat_line in output:
        mat_strs = [str(n) for n in mat_line]
        f.write(" ".join(mat_strs) + "\n")

def calculate_result(dim_x, dim_y, snake_num, snake_lens, field_mat):
    snake_lens.sort(reverse=True)
    print(snake_lens)
    vertix_num = dim_x*dim_y
    longest_paths = [[-5 for _ in range(vertix_num)] for _ in range(vertix_num)]

    print(field_mat)

    for i in range(dim_y):
        for j in range(dim_x):
            if field_mat[i][j] == '*':
                field_mat[i][j] = -float("inf")
            else:
                field_mat[i][j] = int(field_mat[i][j])

    for i in range(dim_y):
        for j in range(dim_x):
            longest_paths[i * dim_x + j][i * dim_x + j] = field_mat[i][j]
            longest_paths[i * dim_x + j][(i - 1) % dim_y * dim_x + j] = field_mat[(i - 1) % dim_y][j]
            longest_paths[i * dim_x + j][(i + 1) % dim_y * dim_x + j] = field_mat[(i + 1) % dim_y][j]
            longest_paths[i * dim_x + j][i * dim_x + (j - 1) % dim_x] = field_mat[i][(j - 1) % dim_x]
            longest_paths[i * dim_x + j][i * dim_x + (j + 1) % dim_x] = field_mat[i][(j + 1) % dim_x]

    print(longest_paths)

    return [[0,0],[0,0]]




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filenames = ["00-example.txt"]
    for filename in filenames:
        dim_x, dim_y, snake_num, snake_lens, field_mat = load_input_file(filename)

        output_mat = calculate_result(dim_x, dim_y, snake_num, snake_lens, field_mat)

        output_file_name = filename.split(".")[0] + "_result.txt"
        # create_output_file(output_file_name,[[0,0],[0,0]])
        create_output_file(output_file_name,output_mat)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
