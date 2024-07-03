import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill
        self.enemies = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            time.sleep(5 / self.skill)
            self.enemies -= self.skill
            self.enemies = max(self.enemies, 0)  
            print(f'{self.name}, сражается {100 // self.skill - self.enemies // self.skill} день(дня)..., осталось {self.enemies} воинов.')
        print(f'{self.name} одержал победу спустя {100 // self.skill} дней!')


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)   # Высокий уровень умения


knight1.start()
knight2.start()


knight1.join()
knight2.join()

print('Все битвы закончились!')
