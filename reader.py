import re


def read_sql(data):
    """
    Read sql with queries from data string and return a list of lines

    :return: A formatted string of the sql queries and tables
    """
    # data = data.strip('\r')
    data = re.sub('\\(\\d* \\w*\\)', ";", data)
    data = re.sub('&', '\&', data)
    data = re.sub('_', '\_', data)
    data = re.sub('%', '\%', data)
    data = data.split(';')
    return data
