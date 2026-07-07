from django.db import models

class Link(models.Model):
    original_url = models.URLField(max_length=2000, verbose_name="Оригинальный URL")
    short_code = models.CharField(max_length=50, unique=True, blank=True, verbose_name="Короткий код")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    clicks_count = models.IntegerField(default=0, verbose_name="Количество переходов")
    last_accessed = models.DateTimeField(null=True, blank=True, verbose_name="Последний переход")
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.short_code} -> {self.original_url[:50]}"
