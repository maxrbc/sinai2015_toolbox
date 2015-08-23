from datetime import date, timedelta
from django.conf import settings


# Table loader only works for saving right now a txt
# still need to be added version for the biom table

def table_loader(FILE):
    import os
    with open(settings.MEDIA_ROOT + "/table_upload.txt", "wb+") as destination:
        for chunk in FILE.chunks():
            destination.write(chunk)


def generate_cluster_index(dates):
    result = []
    for i in dates:
        if not i in result:
            result.append(i)
    return result


# In case of negative values , then normalize by
# lowest and correct identification by that value
def correct_timepoint_for_negatives(timepoint):
    # Do not care for order at this step , since
    # we are just creating a reference index for
    # the actual data.
    temp = list(set(list(timepoint.copy())))
    temp.sort()
    result = []
    for i in timepoint:
        index = temp.index(i)
        result.append(index)
    return result


# makes a new column but with the
# timepoint variable parsed to a new
# variable with the date like value
def convert_timepoint_to_date(table, timepoint):
    converted = []
    d = date(1, 1, 1)
    for i in table[timepoint]:
        converted.append(str(d + timedelta(i)))

    name = timepoint + "_to_date"
    table[name] = converted
    return name, table


# this expects you passing a panda table
# as the internal is desing for it
def generate_discrete_timepoint(table, timestamp):
    indexer = generate_cluster_index(table[timestamp])
    result = []
    for i in table[timestamp]:
        result.append(indexer.index(i))
    name = timestamp + "_descrete"
    table[name] = result
    return name, table
