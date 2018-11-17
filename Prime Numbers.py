order = 1000
for i in range(1, order + 1):
    remaining_list = []
    for i_koochika in range(1, i+1):
        remaining = i % i_koochika
        if remaining == 0:
            remaining_list.append(i_koochika)
    if len(remaining_list) == 2:
        print(i)
