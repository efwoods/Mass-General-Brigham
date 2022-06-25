SELECT cars.pk, type, color, maximum_passengers, name, age, car FROM cars
LEFT JOIN persons ON cars.pk = persons.pk;