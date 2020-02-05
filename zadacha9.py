#На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.

#Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования п
#овторов, и производит обратную операцию, получая исходный текст.

#Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

#В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

#Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас п
#оявляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными 
#данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных.
#Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.
file=open('E:\Downloads\dataset_3363_2 (3).txt',"r")
tekst=''
spisok=file.readline()
file.close()
spisok+=" "
dlina=len(spisok)
for i in range(dlina):
    if i==dlina:
        s = spisok[i]
        b = int(spisok[i])
        #print(s * b,end="")
        c = s * b
        tekst += c
    elif spisok[i]==" ":
        break
    elif spisok[i].isalpha() and spisok[i+1].isdigit() and spisok[i+2].isdigit():
        s=spisok[i]
        b=int(spisok[i+1]+spisok[i+2])
        #print(s * b,end="")
        c = s * b
        tekst += c
    elif spisok[i].isalpha() and spisok[i+1].isdigit():
        s = spisok[i]
        b = int(spisok[i + 1])
        #print(s * b,end="")
        c = s * b
        tekst += c
file=open('E:\Downloads\dataset_3363_2 (3).txt',"w")
file.write(tekst)
file.close()

