import pytest
from main.views import generate_short_code
from main.models import Link
import string


@pytest.mark.django_db
class TestGenerateShortCode:

    def test_length_is_5(self):
        """Длина кода равна 5 символам"""
        code = generate_short_code()
        assert len(code) == 5

    def test_contains_only_allowed_chars(self):
        """Код состоит только из букв и цифр"""
        code = generate_short_code()
        allowed = string.ascii_letters + string.digits
        for char in code:
            assert char in allowed, f"Символ '{char}' не разрешен"

    def test_generates_unique_codes(self):
        """тест на уникальность"""
        codes = []
        for _ in range(10):
            code = generate_short_code()
            codes.append(code)
        unique_codes = set(codes)
        assert len(unique_codes) == len(codes), "Есть повторяющиеся коды"