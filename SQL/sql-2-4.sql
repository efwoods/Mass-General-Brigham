WITH persons_permissions AS (
SELECT persons.pk, persons.car, persons.name AS car_owner,
persons.age,
permissions.name AS permission_to_drive_car_from_owner
FROM public.persons 
LEFT JOIN public.permissions ON public.persons.car = public.permissions.car
ORDER BY persons.name
    )
SELECT cars.pk, car_owner, age, car, type, color, maximum_passengers, permission_to_drive_car_from_owner FROM cars
LEFT JOIN persons_permissions ON cars.pk=persons_permissions.pk