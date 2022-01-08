class InfoMessage:
    """Информационное сообщение о тренировке."""
    print('тип тренировки, длительность тренировки, дистанция, средняя скорость, расход энергии')
    pass


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 LEN_STEP:int,
                 M_IN_KM:int
                 ) -> None:
                 self.action=action
                 self.duration=duration
                 self.weight=weight
                 self.LEN_STEP=100



        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance=action * LEN_STEP / M_IN_KM 
        pass

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed=преодоленная_дистанция_за_тренировку / время_тренировки 
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        print('возвращает объект класса сообщения.')
        pass


class Running(Training):
    """Тренировка: бег."""
    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
