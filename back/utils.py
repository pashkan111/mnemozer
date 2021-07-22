def make_dict_out_of_list(queryset=None):
    list_of_notes = []
    for i in queryset:
        list_of_notes.append({"date": i.date.strftime(format='%Y-%m-%d')})
    return list_of_notes