def decorator_apply(lambda_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = lambda_func(args[0])  # Call the lambda function with the first positional argument
            return func(result, *args[1:], **kwargs)  # Call the decorated function with the modified arguments

        return wrapper  # Return the modified wrapper function

    return decorator  # Return the decorator itself


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) -> int:
    return num

