import csv
import time
import requests
from fake_useragent import UserAgent
from random import randint
from tqdm import tqdm


class ParseNumberT2:
    def __init__(self, num):
        """
        Инициализирует объект ParseNumberT2 с указанным номером.
        :param num: Номер, который будет использоваться в параметре 'indexSeed'.
        """

        ru = UserAgent().getRandom
        self.url = 'https://lipetsk.tele2.ru/api/shop/products/numbers/groups'
        self.params = {
            'indexSeed': f'{num}',
            'productId': 'prod1500781',
            'siteId': 'siteLIPETSK',
        }
        self.headers = {
            'User-Agent': ru.get('useragent'),
        }

    def parse(self):
        """
        Выполняет парсинг данных с веб-сайта и записывает их в файл numbers.csv.
        Метод отправляет HTTP GET-запрос на указанный URL с заданными параметрами и заголовками.
        Полученные данные обрабатываются, и цифры из них записываются в CSV файл numbers.csv.
        """
        res = requests.get(
            'https://lipetsk.tele2.ru/api/shop/products/numbers/groups',
            params=self.params,
            headers=self.headers,
        ).json()
        with open('numbers.csv', 'a') as file:
            wr = csv.writer(file)
            for i in range(len(res.get('data')[0].get('bundleGroups')[0].get('bundles'))):
                number = res.get('data')[0].get('bundleGroups')[0].get('bundles')[i].get('numbers')[0].get('number')[1:]
                wr.writerow([number])


if __name__ == '__main__':
    for i in tqdm(range(9113, 9163)):
        t = ParseNumberT2(i)
        t.parse()
        time.sleep(randint(1, 5))
