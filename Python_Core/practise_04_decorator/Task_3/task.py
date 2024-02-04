def validate(func):
    def wrapper(*args, **kwargs):

        for elem in args:
            if elem < 0 or elem > 256:
                return "Function call is not valid!"

        return "Pixel created!"

    return wrapper

@validate
def set_pixel(x: int, y: int, z: int) -> str:
    return

