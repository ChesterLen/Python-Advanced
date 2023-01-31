def even_odd_filter(**kwargs):
    if "even" in kwargs:
        kwargs["even"] = [x for x in kwargs["even"] if x % 2 == 0]

    if "odd" in kwargs:
        kwargs["odd"] = [x for x in kwargs["odd"] if x % 2 != 0]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
