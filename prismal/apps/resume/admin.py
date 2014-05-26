from django.contrib import admin

# Register your models here.
from resume import models

admin.site.register(
    (
        models.City,
        models.Country,
        models.Education,
        models.LifeOccupation,
        models.Link,
        models.Place,
        models.Project,
        models.Task,
        models.WorkExperience
    )
)

