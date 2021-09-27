import time
from typing import Callable, Any
import functools


def time_slip(function: Callable) -> Any:
    """Функция декаратор перед проверки измененые данних на веб странице или её код ждет 2 секунды"""

    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        time.sleep(2)
        print("Изменилось данние на веб странице или её код", end=" ")
        return function(*args, **kwargs)
    return wrapper


@time_slip
def variation() -> bool:
    return False


print(variation())

# зачет!
