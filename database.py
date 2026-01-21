import os

class Person:
    def __init__(self, surname, name, mid, gender, y, m, d, job, exp, lang, pay):
        self.surname = surname
        self.name = name
        self.mid = mid
        self.gender = gender
        self.y = y
        self.m = m
        self.d = d
        self.job = job
        self.exp = exp
        self.lang = lang
        self.pay = pay

def load():
    if not os.path.exists("info.txt"):
        print("Нет файла")
        return []
    
    all_people = []
    
    try:
        with open("info.txt", 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                parts = [p.strip() for p in line.split(',')]
                
                if len(parts) >= 11:
                    p = Person(
                        parts[0], parts[1], parts[2], parts[3],
                        int(parts[4]), int(parts[5]), int(parts[6]),
                        parts[7], int(parts[8]), parts[9], int(parts[10])
                    )
                    all_people.append(p)
        
        print(f"Загружено: {len(all_people)}")
        return all_people
        
    except:
        print("Ошибка")
        return []