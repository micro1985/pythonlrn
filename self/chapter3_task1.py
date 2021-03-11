import random

print("Пирожок с сюрпризом")

choice = random.randint(1, 5)

if choice == 1:
    print("З малинай")
elif choice == 2:
    print("З варэннем")
elif choice == 3:
    print("Са згушчонкай")
elif choice == 4:
    print("З мёдам")
elif choice == 5:
    print("Са смятанай")
else:
    print("Ня правильна")

print("А пааахне як...")
input("Нажми Enter")
