def get_formatted_Name(first_name,last_name,third_name=''):
    if third_name!='':
        full_name="{} {} {}".format(first_name,last_name,third_name)
    else:
        full_name = "{} {}".format(first_name, last_name)
    return full_name

