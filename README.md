# automatic-email-validation
[python] Automatic email validation 


## Описание

Скрипт для автоматической проверки элетронных почт из excel файла. Скрипт создаёт два файла: один для корректных адресов, другой для не корректных. Адреса проверяются на существование и возможность отправить сообщение

## Использование

Файл должен иметь расширение excel, а все адреса должны быть записаны в столбик.

```
python main.py [-h] --file FILE

Парсим почтовые адреса

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  file with data
  ```

## Пример использования

Запуск скрипта имеет такой вид: 
```
python3 sctipt.py --file=FILE_NAME
```
