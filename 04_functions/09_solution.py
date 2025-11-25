def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i   # Yielding even numbers one by one




for num in even_generator(10):
    print(num)
            