from django.db import models


class goods(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sales = models.IntegerField()
    stock = models.IntegerField()
    detail = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id) + str(self.name) + str(self.price) + str(self.sales) + str(self.stock) + str(self.detail)


class PosiN(models.Model):
    position = models.CharField(max_length=255)
    num = models.IntegerField()


class CompN(models.Model):
    company = models.CharField(max_length=255)
    num = models.IntegerField()


class WorkSalN(models.Model):
    workplace = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    num = models.IntegerField()


class WorkEduN(models.Model):
    workplace = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    num = models.IntegerField()


class WorkN(models.Model):
    workplace = models.CharField(max_length=255)
    num = models.IntegerField()


class EduSalN(models.Model):
    education = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    num = models.IntegerField()


class ExpSalN(models.Model):
    experience = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    num = models.IntegerField()


class Jobs(models.Model):
    position = models.TextField()
    link = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    workplace = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    description = models.TextField()


class NewJobs(models.Model):
    position = models.TextField()
    link = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    workplace = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    attribute = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    description = models.TextField()


class SizeN(models.Model):
    size = models.CharField(max_length=255)
    num = models.IntegerField()


class AttributeN(models.Model):
    Attribute = models.CharField(max_length=255)
    num = models.IntegerField()


class FieldN(models.Model):
    Field = models.CharField(max_length=255)
    num = models.IntegerField()
