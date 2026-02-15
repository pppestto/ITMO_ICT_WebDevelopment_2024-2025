from django.db import models


class Newspaper(models.Model):
    """Модель газеты"""
    title = models.CharField(max_length=200, verbose_name="Название газеты")
    publication_index = models.CharField(max_length=20, unique=True, verbose_name="Индекс издания")
    editor_first_name = models.CharField(max_length=100, verbose_name="Имя редактора")
    editor_last_name = models.CharField(max_length=100, verbose_name="Фамилия редактора")
    editor_middle_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество редактора")
    price_per_copy = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена экземпляра")
    
    class Meta:
        verbose_name = "Газета"
        verbose_name_plural = "Газеты"
        ordering = ['title']
    
    def __str__(self):
        return f"{self.title} ({self.publication_index})"
    
    @property
    def editor_full_name(self):
        """Полное имя редактора"""
        middle = f" {self.editor_middle_name}" if self.editor_middle_name else ""
        return f"{self.editor_last_name} {self.editor_first_name}{middle}"


class PrintingHouse(models.Model):
    """Модель типографии"""
    name = models.CharField(max_length=200, verbose_name="Название типографии")
    address = models.TextField(verbose_name="Адрес")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    
    class Meta:
        verbose_name = "Типография"
        verbose_name_plural = "Типографии"
        ordering = ['name']
    
    def __str__(self):
        status = "Активна" if self.is_active else "Закрыта"
        return f"{self.name} ({status})"


class PostOffice(models.Model):
    """Модель почтового отделения"""
    number = models.CharField(max_length=20, unique=True, verbose_name="Номер почтового отделения")
    address = models.TextField(verbose_name="Адрес")
    
    class Meta:
        verbose_name = "Почтовое отделение"
        verbose_name_plural = "Почтовые отделения"
        ordering = ['number']
    
    def __str__(self):
        return f"Почтовое отделение №{self.number}"


class PrintingRun(models.Model):
    """Модель тиража - связь между типографией и газетой с указанием тиража"""
    printing_house = models.ForeignKey(PrintingHouse, on_delete=models.CASCADE, verbose_name="Типография")
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE, verbose_name="Газета")
    circulation = models.IntegerField(verbose_name="Тираж")
    
    class Meta:
        verbose_name = "Тираж"
        verbose_name_plural = "Тиражи"
        unique_together = ['printing_house', 'newspaper']
        ordering = ['-circulation']
    
    def __str__(self):
        return f"{self.newspaper.title} в {self.printing_house.name} - тираж {self.circulation}"


class Distribution(models.Model):
    """Модель распределения - связь между почтовым отделением, газетой и типографией с количеством"""
    post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE, verbose_name="Почтовое отделение")
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE, verbose_name="Газета")
    printing_house = models.ForeignKey(PrintingHouse, on_delete=models.CASCADE, verbose_name="Типография")
    quantity = models.IntegerField(verbose_name="Количество экземпляров")
    
    class Meta:
        verbose_name = "Распределение"
        verbose_name_plural = "Распределения"
        unique_together = ['post_office', 'newspaper', 'printing_house']
        ordering = ['post_office', 'newspaper']
    
    def __str__(self):
        return f"{self.newspaper.title} ({self.printing_house.name}) -> {self.post_office.number}: {self.quantity} шт."