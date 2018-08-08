
class Car(models.Model):
    car_capacity = models.PositiveIntegerField(default=3)
    car_number_plate = models.CharField(max_length=255)
    car_color = models.CharField(max_length=255)
    driver = models.ForeignKey(User)

    @classmethod
    def delete_car(id):
        id.delete()


