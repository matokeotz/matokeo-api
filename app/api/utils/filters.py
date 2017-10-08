def field_filter(queryset, name, values):
    value_list = values.replace(" ", "").replace("-", " ").split(',')
    if len(value_list) > 0:
        kwargs = { '{0}__{1}'.format(name, 'in'): value_list }
        # print(kwargs)
        return queryset.filter(**kwargs)
    else:
        return queryset