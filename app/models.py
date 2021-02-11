from django.contrib.auth.models import User
from django.db import models


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)

    def __str__(self):
        return f"{self.name}"


class Image(models.Model):
    file = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.file}"


class Video(models.Model):
    link = models.FileField(upload_to='videos/', )

    def save(self, *args, **kwargs):
        super(Video, self).save(*args, **kwargs)
        filename = self.link.url

    def __str__(self):
        return f"{self.link}"


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    price = models.IntegerField(null=True, blank=False)
    like = models.ManyToManyField(Like, related_name='productLike',
                                  through='ProductLike')
    shortDesc = models.TextField(null=True, blank=False)
    desc = models.TextField(null=True, blank=False)
    images = models.ManyToManyField(Image, related_name='productImage',
                                    through='ProductImage')
    videos = models.ManyToManyField(Video, related_name='productVideo',
                                    through='ProductVideo')
    tags = models.ManyToManyField(Tag, related_name='productTag',
                                  through='ProductTag')

    def __str__(self):
        return f"{self.name} ({self.shortDesc}, {self.price})"


class ProductLike(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    like = models.ForeignKey(Like, on_delete=models.CASCADE)


class ProductTag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)


class ProductVideo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
