#My implementation of the Binary search algorithm
def binary_search(input_array, element):
    for i in range(len(input_array)):
        if input_array[i] < element:
            input_array[i] = input_array[(i + 1)]
        elif input_array[i] == element:
            return i + 1
        else:
            return -1
