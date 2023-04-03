from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street},  {self.city}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True
    )

    def full_name(self):
        return f"{self.first_name} + "" + {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=75)
    rating = models.IntegerField(validators=[MaxValueValidator(5),
                                             MinValueValidator(1)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)  # Cascade deletes books when author gets
    # deleted then
    # protect which protects books when author gets deleted also null which makes books null
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True)  # Harry Potter 1 => harry-potter-1

    def __str__(self):
        return f" {self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.id])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


