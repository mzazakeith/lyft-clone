
User = get_user_model()

Gender_Choices = (
    ('F', 'female'),
    ('M', 'male'),
)


class DriverProfile(models.Model):
    profile_pic = ImageField()
    gender = models.CharField(max_length=30, choices=Gender_Choices, default='None', blank=True)
    phone_number = models.PositiveIntegerField()
    user = models.ForeignKey(User)


    @classmethod
    def delete_driver(id, self):
        self.delete()

    @classmethod
    def update_driver(driver):
        driver.update()


class Car(models.Model):
    car_capacity = models.PositiveIntegerField(default=3)
    car_number_plate = models.CharField(max_length=255)
    car_color = models.CharField(max_length=255)
    driver = models.ForeignKey(User)

    @classmethod
    def delete_car(id):
        id.delete()


class driver_location(models.Model):
    current_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    user = models.ForeignKey(User)

    @classmethod
    def update_locationr(location):
        location.update()

