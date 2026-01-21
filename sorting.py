def shake(data, key_func):
    if len(data) <= 1:
        return data.copy()
    
    arr = data.copy()
    left = 0
    right = len(arr) - 1
    swap = True
    
    while left < right and swap:
        swap = False
        
        for i in range(left, right):
            if key_func(arr[i]) > key_func(arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
        
        if not swap:
            break
        
        right -= 1
        
        for i in range(right, left, -1):
            if key_func(arr[i - 1]) > key_func(arr[i]):
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swap = True
        
        left += 1
    
    return arr

def sort1(people):
    def key(p):
        return (p.job, p.surname)
    return shake(people, key)

def sort2(people):
    def key(p):
        gender_val = 0 if p.gender == "Мужской" else 1
        return (-p.exp, gender_val, p.surname)
    return shake(people, key)

def sort3(people):
    def key(p):
        return (-p.pay, p.surname)
    return shake(people, key)