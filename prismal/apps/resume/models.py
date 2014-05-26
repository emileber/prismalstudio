from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _

class Link(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    def __str__(self):
        return "%s (%s)" % (self.title, self.url)


class LifeOccupation(models.Model):
    start_date = models.DateField(_("date started"))
    finished_date = models.DateField(_("date finished"), null=True, blank=True)
    name = models.CharField(_("Event title"), max_length=200)
    hour_per_week = models.PositiveSmallIntegerField(
        help_text=_("How many hours per week does that occupation takes you?"), 
        default=0,
        validators=[
            MaxValueValidator(168),
            MinValueValidator(0)
        ])
    class Meta:
        ordering = ('finished_date', 'name',)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    description = models.TextField()
    link = models.ForeignKey(Link, blank=True)
    life_occupation = models.OneToOneField(LifeOccupation)
    
    def __str__(self):
        return self.life_occupation.__str__()


class Country(models.Model):
    name = models.CharField(max_length=40, unique=True)
    code = models.CharField(max_length=2, blank=True)  # not unique as there are duplicates (IT)
    
    class Meta:
        verbose_name_plural = _('Countries')
        ordering = ('name',)
    
    def __str__(self):
        return u'%s' % (self.code or self.name)

class City(models.Model):
    name = models.CharField(max_length=40, unique=True)
    country = models.ForeignKey(Country)
    class Meta:
        verbose_name_plural = _('Cities')
        ordering = ('country', 'name',)
    
    def __str__(self):
        return u'%s, %s' % (self.name, self.country.name)


class Place(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City)
    link = models.ForeignKey(Link, blank=True)
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return u'%s, %s' % (self.name, self.city.__str__())

# is-a LifeOccupation
class Education(models.Model):
    life_occupation = models.OneToOneField(LifeOccupation)
    place = models.ForeignKey(Place, verbose_name=_("school"))
    
    def __str__(self):
        return "%s at %s" % (self.life_occupation.name, self.place.__str__())


class Task(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# is-a LifeOccupation
class WorkExperience(models.Model):
    life_occupation = models.OneToOneField(LifeOccupation)
    place = models.ForeignKey(Place, verbose_name=_("place worked at"))
    task = models.ManyToManyField(Task)
    
    def __str__(self):
        return "%s at %s" % (self.life_occupation.name, self.place.__str__())
