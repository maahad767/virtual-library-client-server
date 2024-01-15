from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)
    short_code = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=100)
    cover = models.ImageField()
    description = models.TextField()
    pages = models.IntegerField()

    author = models.ForeignKey("product.Author", on_delete=models.CASCADE)
    publisher = models.ForeignKey("product.Publisher", on_delete=models.CASCADE)
    category = models.ForeignKey("product.Category", on_delete=models.CASCADE)
    language = models.ForeignKey("product.Language", on_delete=models.CASCADE)
    publish_date = models.DateField()


class Copy(models.Model):
    owner = models.ForeignKey("account.User", on_delete=models.CASCADE)
    book = models.ForeignKey("product.Book", on_delete=models.CASCADE)
    status = models.SmallIntegerField()  # enum field

    def __str__(self):
        return f"{self.book} - {self.status}"
