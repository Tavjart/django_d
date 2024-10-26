import csv
from .models import Solution


def import_csv(file):
    # Чтение CSV файла
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.reader(decoded_file)

    # Пропустим заголовки
    next(reader)

    # Парсинг строк и создание записей в модели Solution
    for row in reader:
        Solution.objects.create(
            short_name=row[0],
            page_number=row[1],
            title=row[2],
            image_name=row[3],
            folder=row[4],
            quantity=row[5],
            solution=row[6],
            name_1=row[7],
            name_2=row[8],
        )
