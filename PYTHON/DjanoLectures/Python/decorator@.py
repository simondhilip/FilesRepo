def new_decorator(func):

    def wrap_func():
        print ("Code would be here, before executing the func")

        func()

        print ("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print ("This function is in need of a Decorator")

# Reassign func_needs_decorator the normal way
# func_needs_decorator = new_decorator(func_needs_decorator)
# func_needs_decorator()
# # above call is similar to below
# a = new_decorator(func_needs_decorator)
# a()

# Reassign func_needs_decorator the @ way
@new_decorator
def func_needs_decorator():
    print ("This function is in need of a Decorator")

func_needs_decorator()
