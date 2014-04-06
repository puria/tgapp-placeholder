from tg import expose

@expose('placeholder.templates.little_partial')
def something(name):
    return dict(name=name)