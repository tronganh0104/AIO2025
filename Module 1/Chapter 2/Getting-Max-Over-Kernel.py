def max_kernel(num_list, k):
    if len(num_list) < k: 
        return
    start_index = 0
    end_index = k
    length = len(num_list)
    result = []
    while (end_index <= length):
        current_list = num_list[start_index:end_index]
        result.append(max(current_list))
        start_index += 1
        end_index += 1
    return result