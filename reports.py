from sorting import sort1, sort2, sort3

def show_all(people):
    print("\n  ВСЕ СОИСКАТЕЛИ   ")
    print()
    sorted_people = sort1(people)
    
    for i, p in enumerate(sorted_people, 1):
        print(f"{i:2}. {p.surname:15} {p.name:10} {p.mid:15} | "
              f"{p.gender:8} | {p.d:02}.{p.m:02}.{p.y} | "
              f"{p.job:20} | {p.exp:2}. | {p.lang:20} | {p.pay:8} руб.")
    
    print(f"\nВсего: {len(sorted_people)}")
    return sorted_people

def show_job(people, job):
    filtered = [p for p in people if p.job == job]
    
    if not filtered:
        print(f"Нет таких: {job}")
        return []
    
    sorted_people = sort2(filtered)
    
    print(f"\n--- {job} ---")
    for i, p in enumerate(sorted_people, 1):
        print(f"{i:2}. {p.surname:15} {p.name:10} {p.mid:15} | "
              f"{p.gender:8} | {p.d:02}.{p.m:02}.{p.y} | "
              f"{p.exp:2}. | {p.lang:20} | {p.pay:8} руб.")
    
    print(f"\nНайдено: {len(sorted_people)}")
    return sorted_people

def show_pay(people, min_p, max_p):
    filtered = [p for p in people if min_p <= p.pay <= max_p]
    
    if not filtered:
        print(f"Нет с зарплатой {min_p}-{max_p}")
        return []
    
    sorted_people = sort3(filtered)
    
    print(f"\n--- ЗАРПЛАТА {min_p}-{max_p} ---")
    for i, p in enumerate(sorted_people, 1):
        print(f"{i:2}. {p.surname:15} {p.name:10} {p.mid:15} | "
              f"{p.gender:8} | {p.d:02}.{p.m:02}.{p.y} | "
              f"{p.job:20} | {p.exp:2}. | {p.lang:20} | {p.pay:8} руб.")
    
    print(f"\nНайдено: {len(sorted_people)}")
    return sorted_people