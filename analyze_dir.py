import os

def get_sizes(path):
    sizes = {}

    # перебор элементов
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        
        # получаем размер
        if os.path.isfile(item_path):
            sizes[item] = os.path.getsize(item_path)  # размер файла в байтах
        elif os.path.isdir(item_path):
            sizes[item] = get_directory_size(item_path)  # размер директории

    return sizes

def get_directory_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def main():
    current_path = os.getcwd() 
    sizes = get_sizes(current_path)  # получаем размеры 
    
    #сортировка
    sort_sizes = sorted(sizes.items(), key=lambda item: item[1], reverse=True)


    # выводим размеры
    for item, size in sort_sizes:
        print(f"{item}: {size} bytes")

if __name__ == "__main__":
    main()