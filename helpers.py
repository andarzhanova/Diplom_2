from faker import Faker

faker = Faker()

payload = {
    "email": faker.email(),
    "password": faker.random_int(100000, 999999),
    "name": faker.name()
}
