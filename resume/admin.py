from django.contrib import admin

# Register your models here.
from resume.models import City, Country, Education, LifeOccupation, Link, Place, Project, Task, WorkExperience

admin.site.register(
                    (
                     City,
                     Country,
                     Education,
                     LifeOccupation,
                     Link,
                     Place,
                     Project,
                     Task,
                     WorkExperience
                     )
                    )
