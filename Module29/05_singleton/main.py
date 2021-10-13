import functools


def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if wrapper.wrapper_obj == 0:
            wrapper.wrapper_obj = cls(*args, **kwargs)
        return wrapper.wrapper_obj

    wrapper.wrapper_obj = 0
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
