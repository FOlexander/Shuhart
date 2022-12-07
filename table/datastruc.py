import csv
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats
import controlchart

from table.models import Tables


def read_file(filename, current_user):
    df_list = []
    with open(f'media/{filename}', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            df_list.append(row)

    a = df_list[1:]
    c = [int(x[0].split('.')[1]) for x in a]
    counted_c = Counter(c)
    x = sorted(dict(counted_c, ).items())
    count_month = []
    for i in x:
        count_month.append(i[1])

    # widgets_quality = [56, 75, 82, 12, 34, 18, 22, 81, 88, 91, 76, 85, 100, 88, 43, 44]
    s = controlchart.Spc(count_month, controlchart.CHART_X_MR_X)
    s.get_chart(title=filename)
    csvadress = filename
    plotadress = filename.replace('csv', 'png')
    p = Tables(user=current_user, user_table=csvadress, user_model=plotadress)
    p.save()

