import time


class DecoratorTimer(object):
    __slots__ = ['function_to_decorate', 'time']

    def __init__(self, fun):
        self.function_to_decorate = fun
        self.time = time.time()

    def __call__(self):
        print ("start time decorator: ", self.time)
        result = self.function_to_decorate()
        print ("end time decorator: ", time.time())
        print ("Total time decorator: ", time.time() - self.time)
        return result


def decorator_str_to_html(html_tag):
    def real_decorator_fun(function_to_decorate):
        def decorate(*args, **kwargs):
            return "<%s> %s </%s>" % (html_tag, function_to_decorate(*args, **kwargs), html_tag)
        return decorate
    return real_decorator_fun


class TimeCounter(object):
    __slots__ = ['time']

    def __init__(self):
        self.time = time.time()

    def __enter__(self):
        print ("start time context: ", self.time)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print ("end time context: ", time.time())
        print ("Total time context: ", time.time() - self.time)


@DecoratorTimer
def foo():
    n = 0
    for i in range(0, 100000):
        n += n + 1 * 2
    return n


with TimeCounter() as timer:
    foo()


@decorator_str_to_html("b")
def boo(my_str):
    return my_str


print boo("lalala")