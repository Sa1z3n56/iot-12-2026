from enum import Enum
from typing import List, Union


class PlanetType(Enum):
    """Перелік типів планет."""
    TERRESTRIAL = "Terrestrial (Земної групи)"
    JOVIAN = "Jovian (Газовий гігант)"


class Planet:
    """Клас, що описує окрему планету."""

    def __init__(
        self,
        name: str,
        planet_type: PlanetType,
        mass: float,
        orbital_velocity: float,
        mean_temperature: float,
        length_of_day: float,
        distance_from_sun: float,
    ) -> None:
        self.name = name
        self.planet_type = planet_type
        self.mass = mass                            # кг
        self.orbital_velocity = orbital_velocity    # км/с
        self.mean_temperature = mean_temperature    # °C
        self.length_of_day = length_of_day          # годин
        self.distance_from_sun = distance_from_sun  # млн км

    def __del__(self) -> None:
        # Перевірка наявності атрибута на випадок помилки під час ініціалізації
        if hasattr(self, "_name"):
            print(f"[Деструктор] Об'єкт планети '{self._name}' видалено з пам'яті.")

    # --- Функції доступу (Getters & Setters) ---

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Назва планети не може бути порожньою.")
        self._name = value.strip()

    @property
    def planet_type(self) -> PlanetType:
        return self._planet_type

    @planet_type.setter
    def planet_type(self, value: PlanetType) -> None:
        if not isinstance(value, PlanetType):
            raise TypeError("Тип планети має бути екземпляром PlanetType.")
        self._planet_type = value

    @property
    def mass(self) -> float:
        return self._mass

    @mass.setter
    def mass(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Маса планети має бути додатним числом.")
        self._mass = float(value)

    @property
    def orbital_velocity(self) -> float:
        return self._orbital_velocity

    @orbital_velocity.setter
    def orbital_velocity(self, value: float) -> None:
        if value < 0:
            raise ValueError("Орбітальна швидкість не може бути від'ємною.")
        self._orbital_velocity = float(value)

    @property
    def mean_temperature(self) -> float:
        return self._mean_temperature

    @mean_temperature.setter
    def mean_temperature(self, value: float) -> None:
        self._mean_temperature = float(value)

    @property
    def length_of_day(self) -> float:
        return self._length_of_day

    @length_of_day.setter
    def length_of_day(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Тривалість дня має бути додатною.")
        self._length_of_day = float(value)

    @property
    def distance_from_sun(self) -> float:
        return self._distance_from_sun

    @distance_from_sun.setter
    def distance_from_sun(self, value: float) -> None:
        if value < 0:
            raise ValueError("Відстань від Сонця не може бути від'ємною.")
        self._distance_from_sun = float(value)

    # --- Виведення інформації на екран ---

    def display_info(self) -> None:
        print(self)

    def __str__(self) -> str:
        return (
            f"Планета: {self._name:<10} | Тип: {self._planet_type.name:<11} | "
            f"Маса: {self._mass:.3e} кг | Орб. швидкість: {self._orbital_velocity:>5.2f} км/с | "
            f"Темп.: {self._mean_temperature:>6.1f} °C | День: {self._length_of_day:>6.1f} год | "
            f"Відстань від Сонця: {self._distance_from_sun:>6.1f} млн км"
        )


class Planetary:
    """Клас, що представляє планетарну систему з набором планет."""

    def __init__(self, system_name: str, planets: List[Planet] | None = None) -> None:
        self._system_name = system_name
        self._planets: List[Planet] = list(planets) if planets else []

    def __del__(self) -> None:
        if hasattr(self, "_system_name"):
            print(f"[Деструктор] Планетарну систему '{self._system_name}' видалено.")

    # --- Функції доступу та керування колекцією ---

    @property
    def system_name(self) -> str:
        return self._system_name

    @system_name.setter
    def system_name(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Назва системи не може бути порожньою.")
        self._system_name = value.strip()

    @property
    def planets(self) -> List[Planet]:
        return self._planets

    def add_planet(self, planet: Planet) -> None:
        if not isinstance(planet, Planet):
            raise TypeError("Можна додавати лише об'єкти класу Planet.")
        self._planets.append(planet)

    def remove_planet(self, planet_name: str) -> bool:
        for planet in self._planets:
            if planet.name.lower() == planet_name.lower():
                self._planets.remove(planet)
                return True
        return False

    # --- Виведення інформації ---

    def display_all(self) -> None:
        print(f"\n=== Планетарна система: {self._system_name} (кількість планет: {len(self._planets)}) ===")
        if not self._planets:
            print("Список планет порожній.")
            return
        for idx, planet in enumerate(self._planets, start=1):
            print(f"{idx}. {planet}")

    # --- Спеціальні методи за варіантом ---

    def sort_by_length_of_day(self, reverse: bool = False) -> List[Planet]:
        """Сортує планети системи за тривалістю світлового дня."""
        self._planets.sort(key=lambda planet: planet.length_of_day, reverse=reverse)
        return self._planets

    @staticmethod
    def findDistanceBetween(planetA: Planet, planetB: Planet) -> float:
        """Обчислює середню відстань між орбітами двох планет (у млн км)."""
        if not isinstance(planetA, Planet) or not isinstance(planetB, Planet):
            raise TypeError("Обидва аргументи мають бути об'єктами класу Planet.")
        return abs(planetA.distance_from_sun - planetB.distance_from_sun)

    @staticmethod
    def findAverageMass(*planets: Union[Planet, List[Planet]]) -> float:
        """
        Знаходить середню масу серед заданих планет (у кг).
        Приймає як довільну кількість аргументів Planet, так і список планет.
        """
        planet_list: List[Planet] = []
        for item in planets:
            if isinstance(item, (list, tuple)):
                planet_list.extend(item)
            elif isinstance(item, Planet):
                planet_list.append(item)
            else:
                raise TypeError("Аргументи мають бути об'єктами Planet або списком Planet.")

        if not planet_list:
            raise ValueError("Не передано жодної планети для обчислення середньої маси.")

        total_mass = sum(planet.mass for planet in planet_list)
        return total_mass / len(planet_list)


def main() -> None:
    # 1. Створення об'єктів класу Planet
    mercury = Planet("Меркурій", PlanetType.TERRESTRIAL, 3.301e23, 47.36, 167.0, 4222.6, 57.9)
    earth = Planet("Земля", PlanetType.TERRESTRIAL, 5.972e24, 29.78, 15.0, 24.0, 149.6)
    mars = Planet("Марс", PlanetType.TERRESTRIAL, 6.417e23, 24.07, -65.0, 24.7, 227.9)
    jupiter = Planet("Юпітер", PlanetType.JOVIAN, 1.898e27, 13.07, -110.0, 9.9, 778.5)
    saturn = Planet("Сатурн", PlanetType.JOVIAN, 5.683e26, 9.68, -140.0, 10.7, 1433.5)

    # 2. Створення об'єкта класу Planetary та додавання планет
    solar_system = Planetary("Сонячна система", [mercury, earth, mars, jupiter])
    solar_system.add_planet(saturn)

    # 3. Виведення початкового стану
    solar_system.display_all()

    # 4. Демонстрація роботи функцій доступу (getters / setters)
    print("\n--- Перевірка функцій доступу ---")
    print(f"Поточна середня температура Марса: {mars.mean_temperature} °C")
    mars.mean_temperature = -63.0
    print(f"Оновлена середня температура Марса: {mars.mean_temperature} °C")

    # 5. Сортування за довжиною світлового дня
    print("\n--- Сортування планет за тривалістю дня (за зростанням) ---")
    solar_system.sort_by_length_of_day()
    solar_system.display_all()

    # 6. Обчислення відстані між двома планетами
    dist_earth_mars = Planetary.findDistanceBetween(earth, mars)
    print(f"\nСередня відстань між орбітами Землі та Марса: {dist_earth_mars:.1f} млн км")

    # 7. Обчислення середньої маси заданих планет
    avg_terrestrial_mass = Planetary.findAverageMass(mercury, earth, mars)
    avg_all_mass = Planetary.findAverageMass(solar_system.planets)

    print(f"Середня маса планет земної групи (Меркурій, Земля, Марс): {avg_terrestrial_mass:.3e} кг")
    print(f"Середня маса всіх планет у системі: {avg_all_mass:.3e} кг\n")


if __name__ == "__main__":
    main()