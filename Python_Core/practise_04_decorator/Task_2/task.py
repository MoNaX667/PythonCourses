import time
import inspect

def log(fn):
    """
    Add your code here or call it from here   
    """

    def logging(*args,**kwargs):
        my_log = open("log.txt","a")
        start_time = time.time()
        result = fn(*args, **kwargs)
        time.sleep(2)

        kwargs_list = "None"
        for key in kwargs:
            if kwargs_list == "None":
                kwargs_list = f"{key}={kwargs[key]}"
            else:
                kwargs_list = f"{kwargs_list}, {key}={kwargs[key]}"

        new_row = f"{fn.__name__}; args: a={args[0]}, b={args[1]}; kwargs: {kwargs_list}; execution time: {time.time() - start_time}"
        my_log.write(new_row)

        return result

    return logging
    pass

@log
def foo(a, b, c):
    arguments = locals()
    return
