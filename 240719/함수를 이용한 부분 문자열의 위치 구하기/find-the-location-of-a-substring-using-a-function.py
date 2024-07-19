input_string = input()
target_string = input()

def compareString(str_):
    return input_string.find(target_string) 
    # string.find(subString, [start], [end]): string에서 subString 찾아보고, 있으면 첫 번째 인덱스 반환, 없으면 -1 반환
    
print(compareString(target_string))