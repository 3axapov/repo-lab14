#!/bin/bash

#функция для получения размера
get_size() {
    local path="$1"
    local size=$(du -sh "$path" 2>/dev/null | awk '{print $1}')
    echo "$size"
}

#функция анализа директории
analyze_dir() {
    local dir="$1"
    local results=()
    
    
    #перебор элементов  директории
    for item in "$dir"/*; do
	#проверка наличия элемента
	if [ -e "$item" ]; then
	    #получение размера и сохранить в масив
	    local size=$(get_size "$item")
	    results+=("$size $item")
	fi
    done
    
    #сортировка по первому столбцу
    printf "%s\n" "${results[@]}" | sort -rh
}
echo "Анализ размеров каждой директории и файла в текущей директории:"
analyze_dir "."
