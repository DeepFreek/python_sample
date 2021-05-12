name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())  # 1- делаем 1 буквы заглавные 2-верхний регистр 3-нижний регистр
first_name = "ada"
last_name = "lovelace"
full_name = "{} {}".format(first_name, last_name)  # вставляем переменные в текст
print(full_name)
lang = "  python"
print(lang.lstrip())  # удаляем пробелы есть праый левый и просто стрип


#Задания 2.3-2.7
#------------------------------------------------------
#вставить имя в вывод
name="sergey"
name=name.title()
print(f"Hello {name}")
#------------------------------------------------------
#вывести в верхнем регистре нижнем и тайтл
print()
print(name.lower())
print(name.upper())
print(name.title())
#------------------------------------------------------
#вывести цитату
print()
mes='волк в цирке не выступает'
print(f'великий сказал"{mes}"')
#------------------------------------------------------
#вывести цитату и имя автора
print()
mes='волк в цирке не выступает'
author="Великий"
print(f'{author} сказал"{mes}"')
#------------------------------------------------------
#вывести строку и удалить пробелы
print()
mess="   python    \n"
print(mess.rstrip())
print(mess.lstrip())
print(mess.strip())
