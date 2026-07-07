from django.shortcuts import render, redirect
from .forms import LinkForm
from .models import Link
import string
import random
from django.shortcuts import get_object_or_404
from django.utils import timezone
import logging
from .logger import setup_logging

# Настройка логирования (один раз при старте)
setup_logging()
logger = logging.getLogger(__name__)


def generate_short_code():
    """
    Генерирует уникальный короткий код длиной 5 символов.
    Состоит из букв (верхний и нижний регистр) и цифр.
    Проверяет уникальность в БД перед возвратом.
    """
    chars = string.ascii_letters + string.digits
    length = 5
    code = ''.join(random.choices(chars, k=length))
    while Link.objects.filter(short_code=code).exists():
        code = ''.join(random.choices(chars, k=length))
    logger.info(f"Сгенерирован код: {code}")
    return code

def short_code_page(request, short_code):
    """
    Отображает страницу с результатом: короткая ссылка и оригинальный URL.
    Если ссылка не найдена — логируем предупреждение.
    """
    try:
        link = get_object_or_404(Link, short_code=short_code)
        return render(request, 'main/short_code.html', {
            'short_code': link.short_code,
            'original_url': link.original_url
        })
    except:
        logger.warning(f"Запрошена несуществующая ссылка: {short_code}")
        raise

def add_url(request):
    """
    Обрабатывает создание короткой ссылки:
    - Проверяет, существует ли уже такой URL
    - Если да — возвращает существующий короткий код (избегаем дубликатов)
    - Если нет — генерирует новый код и сохраняет ссылку
    """
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            logger.info(f"Запрос на сокращение: {original_url}")
            existing_link = Link.objects.filter(original_url=original_url).first()
            if existing_link:
                return redirect('short_code', short_code=existing_link.short_code)
            else:
                link = form.save(commit=False)
                link.short_code = generate_short_code()
                link.save()
                return redirect('short_code', short_code=link.short_code)
    else:
       form = LinkForm()
    return render(request, 'main/link.html', {'form': form})

def redirect_to_original(request, short_code):
    """
    Перенаправляет по короткой ссылке на оригинальный URL.
    Увеличивает счётчик кликов и обновляет дату последнего перехода.
    """
    try:
        link = get_object_or_404(Link, short_code=short_code, is_active=True)
        link.clicks_count += 1
        link.last_accessed = timezone.now()
        link.save(update_fields=['clicks_count', 'last_accessed'])
        return redirect(link.original_url)
    except Exception as e:
        logger.error(f"Ошибка при переходе по {short_code}: {e}")
        raise