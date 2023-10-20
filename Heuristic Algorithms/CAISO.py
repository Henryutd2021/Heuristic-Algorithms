# this runs in python 3 as of Jan. 2018
import pandas as pd
import time
import urllib
from bs4 import BeautifulSoup
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt
import datetime


starttime = datetime.datetime.now()
dates = pd.date_range(start='4/20/2010', end='2/7/2020')
dates = dates.strftime('%Y%m%d')

hours = pd.date_range(start='4/20/2010', end='2/8/2020', freq='H')
cols = ['geothermal', 'biomass', 'biogas', 'small hydro', 'wind total', 'solar',
        'renewables', 'nuclear', 'thermal', 'imports', 'hydro']

# this will be the dataframe we fill in
total_gen = pd.DataFrame(index=hours, columns=cols)

for d in dates:

    if d in ['20150308', '20160313', '20170312']:  # some bad bad days
        continue

    print(d)
    url = f'http://content.caiso.com/green/renewrpt/{d}_DailyRenewablesWatch.txt'

    try:
        page = urllib.request.urlopen(url).read()
    except:
        print(f'Day {d} failed, continuing...')

    soup = BeautifulSoup(page, 'lxml')
    t = str(soup.find('p').text).replace('\t\t', ',').replace('\t', ',')

    # grab the two tables and combine them into one
    df1 = pd.read_csv(StringIO(t), header=1, nrows=24)
    df2 = pd.read_csv(StringIO(t), header=29, nrows=24)
    df = pd.concat([df1, df2.drop('Hour', axis=1)], axis=1)
    df.set_index('Hour', inplace=True)
    df = df[df.columns[~df.columns.str.contains('Unnamed:')]]
    df.columns = [c.lower() for c in df.columns]  # uppercase

    # starting in July 2012, they separate solar pv and solar thermal
    # add them back together and fix missing values
    if df.values.shape[1] > 11:

        if df['solar thermal'].dtype == np.object_:  # string
            ix = df['solar thermal'].str.contains('No Good Data')
            df['solar thermal'][ix] = np.nan
            df['solar thermal'] = pd.to_numeric(df['solar thermal'])

        df['solar'] = df['solar pv'] + df['solar thermal']
        df = df[list(total_gen.columns)]  # re-order and only keep cols in output

    total_gen[d] = df.values

# renew_gen.to_csv('CAISO-renewables-hourly.csv')
total_gen.to_csv('CAISO-all-hourly.csv')
endtime = datetime.datetime.now()
print('Time: ', endtime - starttime)
# even after this, beware of bad data values like #NAME, #REF, #VALUE etc
# I did some manual cleaning in the final CSV files