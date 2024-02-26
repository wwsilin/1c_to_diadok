# Конвертер файлов 1С в Диадок

Скрипт предназначен для преобразования экспортированых файлов УПД  `*.xml` из 1С в формат импорта Диадок.

## Зачем это всё?

История умалчивает, умышленно ли было сделано небольшое различие в форматах файлов обмена электронными документами в вышеупомянутых конкурирующих системах, обе стороны утверждают, что системы работают с форматами файлов утвержденных Приказом ФНС России от 19.12.2023 № ЕД-7-26/970, но при этом, если попытаться импортировать файл xml, содержащий УПД из 1С в диадок, то скорее всего это мероприятие потерпит фиаско.

При разборе ситуации оказалось, что различия имеются только в использованных символах для разделения значений при заполнении всего лишь одного параметра.  

Для исправления этого досадного недоразумения был написан этот скрипт, котрый заменяет символы в экспортированых файлах УПД  `*.xml` из 1С.

## Как это работает

***Для работы скрипта на компьютер обязательно требуется установить Python3 !***  

Скрипт распаковывает экспортированные из 1С архивы, содержащие документы УПД в формате xml, удаляет лишние служебные файлы и каталоги, после чего конвертирует файл в формат, который сервис Диадок принимает без возмущения.

## Как использовать

### Windows

Сачиваем и сохраняем скрипт diadok_conv.py в ту же папку где будут храниться экспортированные из 1С файлы, удобно использовать для этих целей папку в каталоге "Загрузки", например, `\Downloads\1CExchange`.   

Двойным щелчком по файлу diadok_conv.py запускаем работу скрипта и вместо архивов видим файлы в формате `xml` пригодные для импорта в диадок.  

### Linux и MacOs

Если вы счастливый обладатель компьютера фирмы Apple или не менее счастливый пользователь операционной системы Linux, то последовательность ваших действий для использования скрипта должна быть следующей:  

Окрываем терминал и проверяем установлен ли у вас ЯП Python3  

```bash
$ python3
```

Если вы увидели сообщение похожее на такое:  

```bash
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

жмём `ctrl+d` для выхода и пропускаем следующий шаг.  

Если python у вас не установлен, в поиске ищем как установить python3 в вашу систему, выполняем и возвращаемся к этому месту.  

Откроем терминал, находясь в каталоге `~/`  создаем директорию, где мы разместим скрипт и куда будем сохранять файлы с документами из 1С

```bash
mkdir 1CExchange
```

Перемещаемся в этот каталог командой 

```bash
cd 1CExchange/
```

Скачиваем в этот каталог наш скрипт командой

```bash
wget https://raw.githubusercontent.com/wwsilin/1c_to_diadok/main/diadok_conv.py
```

Сохраняем в этот же каталог файлы подлежащие конвертации и запускаем скрипт командой 

```bash
python3 diadok_conv.py 
```

## Для тех, у кого лапки :feet:

Если вы пользователь Windows, у вас не установлен Python, вам лень заморачиваться, а ваш администратор смотрит сквозь пальцы на скачивание и использование `*.exe` файлов из интернета, вы можете скачать архив `Conv.zip` в папку с архивами, полученными из 1С и запустив `Diadok_conv.exe` его получить `xml` файлы для импорта в диадок.

Если вы пользователь Linux и вам вообще не охота в это вникать (а прийдется), качаем вместо скрипта в каталог исполняемы файл diadoc даем права на запуск и пользуемся.  
Последовательность команд следующая:

```bash
$ mkdir 1CExchange

$ cd 1CExchange/

$ wget https://raw.githubusercontent.com/wwsilin/1c_to_diadok/main/diadok

$ sudo chmod 755 diadoc

$ ./diadok
```

*Маленькая оговорка: в виду того, что кодировка файлов xml для сервисов ЭДО положена ср1251, в linux и MacOs работа данного ПО совершенно не  гарантируется. Надеюсь, вам повезёт!*

### Примечание

Работа программы была проверена на 1С версии 8.3 с сервисом Диадок, из 1С экспортировались УПД, сохраненные в ZIP-архив, результат работы программы загружался в сервис контур.диадок.   
Работа с другими видами документов не гарантируется, а также, имеейте в виду, что вся ответственность за использование программы лежит на ее пользователе, поэтому проверяем, что импортируется и что вы отправляете, автор за это не несет никакой ответственности.
