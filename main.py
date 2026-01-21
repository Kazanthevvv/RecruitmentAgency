from database import load
from reports import show_all, show_job, show_pay

def main():
    print("\nКАДРОВОЕ АГЕНСТВО")
    print()
    people = load()
    
    if not people:
        return
    
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Все соискатели (работа ↑, фамилия ↑)")
        print("2. По специальности (стаж ↓, пол ↓, фамилия ↑)")
        print("3. По окладу (зарплата ↓, фамилия ↑)")
        print("0. Выход")
        
        choice = input("Выбор: ")
        
        if choice == "0":
            print("Пока!")
            break
        
        elif choice == "1":
            show_all(people)
        
        elif choice == "2":
            jobs = sorted(set(p.job for p in people))
            print("\nСпециальности:")
            for i, j in enumerate(jobs, 1):
                print(f"{i}. {j}")
            
            try:
                num = int(input("Номер работы: "))
                if 1 <= num <= len(jobs):
                    show_job(people, jobs[num - 1])
                else:
                    print("Неверно")
            except:
                print("Ошибка")
        
        elif choice == "3":
            try:
                min_p = int(input("Мин зарплата: "))
                max_p = int(input("Макс зарплата: "))
                show_pay(people, min_p, max_p)
            except:
                print("Ошибка")
        
        else:
            print("Неверно")
        
        if choice in ["1", "2", "3"]:
            input("\nНажмите Enter для продолжения")

if __name__ == "__main__":
    main()