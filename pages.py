def create_string(pages):
    if len(pages) == 1:
        return str(pages[0])
    sorted_pages = sorted(set(pages))
    start = sorted_pages[0]
    end = sorted_pages[0]
    ranges = []
    for i in range(1, len(sorted_pages)):
        if sorted_pages[i] == end + 1:
            end = sorted_pages[i]
        else:
            ranges.append((start, end))
            start = sorted_pages[i]
            end = sorted_pages[i]
    ranges.append((start, end))
    
    result_parts = []
    for start, end in ranges:
        if start == end:
            result_parts.append(str(start))
        else:
            result_parts.append(f"{start}-{end}")
    
    result = ','.join(result_parts)
    return result

if __name__ == "__main__":
    print(create_string([1])) # 1
    print(create_string([1, 2, 3])) # 1-3
    print(create_string([1, 1, 1])) # 1
    print(create_string([1, 2, 1, 2])) # 1-2
    print(create_string([1, 6, 2, 5])) # 1-2,5-6
    print(create_string([1, 3, 5, 7])) # 1,3,5,7
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9

    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages)) # 1-3
    print(pages) # [3, 2, 1, 3, 2, 1]