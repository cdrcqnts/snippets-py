def name_filter(name):
    """This is the docstring for name_filter"""

    def inner(row):
        if row["name"].lower() == name.lower():
            return row

    return inner


paul_filter = name_filter("Paul")
john_filter = name_filter("John")
george_filter = name_filter("George")
ringo_filter = name_filter("Ringo")


def or_op(filters):
    def inner(row):
        for f in filters:
            if f(row):
                return row

    return inner


filters = [paul_filter, john_filter, george_filter, ringo_filter]
beatle = or_op(filters)
