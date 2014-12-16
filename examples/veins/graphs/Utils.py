__author__ = 'admin'


def flatten(seq):
    l = []
    for elt in seq:
        t = type(elt)
        if t is tuple or t is list:
            for elt2 in flatten(elt):
                if elt2 > 0:
                    l.append(elt2)
        else:
            l.append(elt)
    return l