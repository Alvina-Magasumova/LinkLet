import pytest
from django.urls import reverse
from main.models import Link


@pytest.mark.django_db
class TestAddUrlIntegration:

    def setup_method(self):
        """Подготавливает данные для всех тестов"""
        self.url = reverse('add_url')

    def test_post_creates_link(self, client):
        """POST запрос создает новую запись в БД"""
        assert Link.objects.count() == 0
        response = client.post(self.url, {
            'original_url': 'https://google.com'
        })
        assert Link.objects.count() == 1
        link = Link.objects.first()
        assert link.short_code is not None

    def test_invalid_url_returns_error(self, client):
        """Невалидный URL не создает ссылку"""
        response = client.post(self.url, {
            'original_url': 'not_a_url'
        })
        assert Link.objects.count() == 0

    def test_post_duplicate_url(self, client):
        """Повторная отправка URL не создает дубликат"""
        client.post(self.url, {'original_url': 'https://google.com'})
        client.post(self.url, {'original_url': 'https://google.com'})
        assert Link.objects.count() == 1