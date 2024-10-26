from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Subject(models.Model):
    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GradeLevel(models.Model):
    level = models.IntegerField()

    def __str__(self):
        return str(self.level)


class Textbook(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, blank=True, null=True)
    grade_level = models.ForeignKey('GradeLevel', on_delete=models.CASCADE, blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    book_type = models.CharField(max_length=100, blank=True, null=True)
    book_series = models.CharField(max_length=100, blank=True, null=True)
    authors = models.CharField(max_length=255, blank=True, null=True)
    publication_year = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    edited_by = models.CharField(max_length=255, blank=True, null=True)
    fgos = models.BooleanField(default=False)
    education_level = models.CharField(max_length=100, blank=True, null=True)
    place_of_publication = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    short_name = models.SlugField(unique=True)
    cover_color = models.CharField(max_length=50, blank=True, null=True)
    number_of_parts = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.short_name:
            # Генерация короткого имени, если его нет
            self.short_name = f"{slugify(self.grade_level.level)}-{slugify(self.subject.english_name)}"
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Формирование URL для детальной страницы учебника
        return reverse('textbook_detail', kwargs={
            'grade': self.grade_level.level,
            'subject': self.subject.english_name,
            'short_name': self.short_name
        })

    def get_list_url(self):
        # Формирование URL для списка учебников по классу и предмету
        return reverse('textbook_list', kwargs={
            'grade': self.grade_level.level,
            'subject': self.subject.english_name
        })

    def __str__(self):
        return self.short_name


class Solution(models.Model):
    # textbook = models.ForeignKey(Textbook, on_delete=models.CASCADE)
    short_name = models.CharField(max_length=100)  # Связь с основной моделью по короткому названию
    page_number = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    image_name = models.CharField(max_length=20, blank=True, null=True)
    folder = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    solution = models.PositiveIntegerField(blank=True, null=True)
    name_1 = models.CharField(max_length=100, blank=True, null=True)
    name_2 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.short_name
