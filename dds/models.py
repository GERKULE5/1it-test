from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

# Модель статуса
class Status(models.Model):
  name = models.CharField("Название", max_length=200, unique=True)
  order = models.PositiveSmallIntegerField("Позиция", default=0)

  class Meta:
    verbose_name = "Статус"
    verbose_name_plural = "Статусы"
    ordering = ["order", "name"]
  
  def __str__(self):
    return self.name

# Модель типа операции
class OperationType(models.Model):
  name = models.CharField("Название", max_length=200, unique=True)
  order = models.PositiveSmallIntegerField("Позиция", default=0)

  class Meta:
    verbose_name = "Тип операции"
    verbose_name_plural = "Типы операций"
    ordering = ["order", "name"]

  def __str__(self):
    return self.name

# Модель категории
class Category(models.Model):
  operation_type = models.ForeignKey(
    OperationType,
    on_delete=models.CASCADE,
    related_name="categories",
    verbose_name="Тип операции"
  )
  name = models.CharField("Название", max_length=200)
  order = models.PositiveSmallIntegerField("Позиция", default=0)

  class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["order", "name"]
        unique_together = [("operation_type", "name")]

  def __str__(self):
    return self.name

# Модель подкатегории
class Subcategory(models.Model):
  category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name="subcategories",
    verbose_name="Категория",
  )
  name = models.CharField("Название", max_length=100)
  order = models.PositiveSmallIntegerField("Позиция", default=0)

  class Meta:
    verbose_name = "Подкатегория"
    verbose_name_plural = "Подкатегории"
    ordering = ["order", "name"]
    unique_together = [("category", "name")]

  def __str__(self):
    return self.name

# Модель транзакции
class Transaction(models.Model):
  date = models.DateField("Дата")
  status = models.ForeignKey(
    Status,
    on_delete=models.PROTECT,
    verbose_name="Статус",
  )
  operation_type = models.ForeignKey(
    OperationType,
    on_delete=models.PROTECT,
    verbose_name="Тип",
  )
  category = models.ForeignKey(
    Category,
    on_delete=models.PROTECT,
    verbose_name="Категория",
  )
  subcategory = models.ForeignKey(
    Subcategory,
    on_delete=models.PROTECT,
    verbose_name="Подкатегория",
  )
  amount = models.DecimalField(
    "Сумма (руб.)",
    max_digits=12,
    decimal_places=2,
    validators=[MinValueValidator(Decimal("0.01"))],
  )
  comment = models.TextField("Комментарий", blank=True)
  created_at = models.DateTimeField("Создано", auto_now_add=True)

  class Meta:
    verbose_name = "Запись ДДС"
    verbose_name_plural = "Записи ДДС"
    ordering = ["-date", "-created_at"]

  def __str__(self):
    return f"{self.date} : {self.status} : {self.operation_type} : {self.category} : {self.subcategory} : {self.amount} руб."
  