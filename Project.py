# Define the number of dimensions for the multidimensional array
num_dimensions = int(input("Enter the number of dimensions for the multidimensional array: "))

# Initialize an empty list to store the dimensions
dimensions = []

# Loop through each dimension and ask the user to enter its size
for i in range(num_dimensions):
    size = int(input(f"Enter the size of dimension {i+1}: "))
    dimensions.append(size)

# Create the multidimensional array using the given dimensions
multi_dim_array = [0]*dimensions[0]
for i in range(dimensions[0]):
    multi_dim_array[i] = [0]*dimensions[1] if num_dimensions > 1 else 0
    for j in range(dimensions[1]):
        multi_dim_array[i][j] = [0]*dimensions[2] if num_dimensions > 2 else 0
        for k in range(dimensions[2]):
            multi_dim_array[i][j][k] = [0]*dimensions[3] if num_dimensions > 3 else 0
            for l in range(dimensions[3]):
                multi_dim_array[i][j][k][l] = [0]*dimensions[4] if num_dimensions > 4 else 0
                for m in range(dimensions[4]):
                    multi_dim_array[i][j][k][l][m] = [0]*dimensions[5] if num_dimensions > 5 else 0
                    for n in range(dimensions[5]):
                        multi_dim_array[i][j][k][l][m][n] = [0]*dimensions[6] if num_dimensions > 6 else 0
                        for o in range(dimensions[6]):
                            multi_dim_array[i][j][k][l][m][n][o] = [0]*dimensions[7] if num_dimensions > 7 else 0
                            for p in range(dim):