def pretty(value, htchar=' ', width=4, lfchar='\n', indent=0):
    '''This is pretty printer function.
    Edited from y.petremann [answer](https://stackoverflow.com/a/26209900).

    You can add your new data type such as:

        if value.__class__.__name__ == 'Struct':
            ...
            return ...

    htchar also accept '\t' for tab (set width to 1 if use '\t')
    '''
    nlch = lfchar + htchar * width * (indent + 1)
    if type(value) is dict:
        items = [
            nlch + repr(key) + ': ' + pretty(value[key], htchar, width, lfchar, indent + 1)
            for key in value
        ]
        return '{%s}' % (','.join(items) + lfchar + htchar * width * indent)
    elif type(value) is list:
        items = [
            nlch + pretty(item, htchar, width, lfchar, indent + 1)
            for item in value
        ]
        return '[%s]' % (','.join(items) + lfchar + htchar * width * indent)
    elif type(value) is tuple:
        items = [
            nlch + pretty(item, htchar, width, lfchar, indent + 1)
            for item in value
        ]
        return '(%s)' % (','.join(items) + lfchar + htchar * width * indent)
    else:
        return repr(value)