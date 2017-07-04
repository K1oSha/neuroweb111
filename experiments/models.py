from django.db import models


class Participant(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField()
    physical_data = models.TextField()
    bio = models.TextField()
    is_female = models.BooleanField()
    avatar_url = models.ImageField(upload_to='participant_photos/', default='participant_photos/no-img.jpg')
    test_list = models.TextField()




class Assistant(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField()
    position = models.CharField(max_length=128)

# https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield
class Experiments(models.Model):
    assistant = models.ForeignKey(
        Assistant,
        on_delete=models.CASCADE,
        verbose_name="Responsible person"
    )
    name = models.CharField(max_length=60)
    conditions = models.TextField()
    objectives = models.TextField()
    process = models.TextField()
    results = models.TextField()
    date = models.DateField()
