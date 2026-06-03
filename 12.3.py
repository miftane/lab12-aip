# 12.3.py
import re

ru_en = {}
with open('en-ru.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if not line or '-' not in line:
            continue
        
        parts = line.split('-', 1)
        eng = parts[0].strip()
        rus_parts = [p.strip() for p in parts[1].split(',')]
        
        for rus in rus_parts:
            if rus in ru_en:
                if eng not in ru_en[rus]:
                    ru_en[rus].append(eng)
            else:
                ru_en[rus] = [eng]

sorted_ru_en = dict(sorted(ru_en.items()))

with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for rus, eng_list in sorted_ru_en.items():
        eng_list = sorted(set(eng_list))  # Убираем дубликаты и сортируем
        file.write(f"{rus} – {', '.join(eng_list)}\n")

print("Русско-английский словарь создан в файле ru-en.txt")
