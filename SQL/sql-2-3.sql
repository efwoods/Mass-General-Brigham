UPDATE permissions
SET name='{"Miriam","Abhinav","Randall"}'
FROM persons
WHERE public.persons.car = public.permissions.car AND persons.name='Miriam'