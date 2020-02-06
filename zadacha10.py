Недавно мы считали для каждого слова количество его вхождений в строку. 
Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) 
и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.


















file=open('E:\Downloads\dataset_3363_3 (9).txt',"r")
maxslovo=""
count=0
g=[]
dict={}
spisok=file.read().lower().split()
dlina=len(spisok)
spisok.sort()
file.close()
for i in spisok:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
max_value = max(dict.values())
final_dict = {k: v for k, v in dict.items() if v == max_value}

file=open('E:\Downloads\dataset_3363_3 (9).txt',"w")
for k in final_dict:
    g.append(k)
print(g[0],'',final_dict[g[0]])
stroka=str(g[0])+' '+str(final_dict[g[0]])
file.write(stroka)
file.close()

