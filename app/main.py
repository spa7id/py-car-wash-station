class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> int:
        total_price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.wash_single_car(car)
                total_price += price
        return round(total_price, 1)

    def calculate_washing_price(self, car: Car) -> int:
        diff = self.clean_power - car.clean_mark
        price = (
            car.comfort_class * diff * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> int:
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price

    def rate_service(self, new_rating: float) -> None:
        self.count_of_ratings += 1
        total_rating = (
            self.average_rating * (self.count_of_ratings - 1)
            + new_rating
        )
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
