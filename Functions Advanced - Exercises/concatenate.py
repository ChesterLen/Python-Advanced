def concatenate(*args, **kwargs):
    text = "".join(args)

    for key in kwargs.keys():
        text = text.replace(key, kwargs[key])

    return text