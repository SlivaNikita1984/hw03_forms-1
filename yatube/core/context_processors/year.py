import datetime

year_now = datetime.date.today().year


def year(request):
    """Добавляет переменную с текущим годом."""
    return {
        'year': year_now,
    }
