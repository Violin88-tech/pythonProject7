
import datetime
from datetime import time

def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)


    if  datetime.time(22)<=current_time>=datetime.time(6):


        is_dark_theme = True
    else:
        is_dark_theme = None
    assert is_dark_theme is True



