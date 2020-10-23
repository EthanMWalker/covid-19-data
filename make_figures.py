#!/usr/bin/python3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt, dates
import datetime

import warnings
warnings.filterwarnings('ignore')

# read in data
cnty_df = pd.read_csv('us-counties.csv')
cnty_df.date = pd.to_datetime(cnty_df.date,format='%Y-%m-%d')

# create needed masks
utah_mask = cnty_df.state == 'Utah'
salt_lake_mask = cnty_df.county == 'Salt Lake'
utah_cnty_mask = cnty_df.county == 'Utah'
utah_cnty_df = cnty_df[utah_cnty_mask]
salt_cnty_df = cnty_df[salt_lake_mask]
utah_st_df = cnty_df[utah_mask]

washoe_mask = cnty_df.county == 'Washoe'
washoe_df = cnty_df[washoe_mask]
douglas_mask = cnty_df.county == 'Douglas'
nv_mask = cnty_df.state == 'Nevada'
doug_cnty_df = cnty_df[douglas_mask & nv_mask]
sc_mask = cnty_df.county == 'Santa Cruz'
cali_mask = cnty_df.state == 'California'
sc_df = cnty_df[sc_mask & cali_mask]
cc_mask = cnty_df.county == 'Carson City'
cc_df = cnty_df[cc_mask]

ind_mask = cnty_df.state == 'Indiana'
ken_mask = cnty_df.state == 'Kentucky'
jef_mask = cnty_df.county == 'Jefferson'
flo_mask = cnty_df.county == 'Floyd'
jef_df = cnty_df[ken_mask & jef_mask]
flo_df = cnty_df[ind_mask & flo_mask]

ten_mask = cnty_df.state == 'Tennessee'
knox_mask = cnty_df.county == 'Knox'
davi_mask = cnty_df.county == 'Davidson'
knox_df = cnty_df[ten_mask & knox_mask]
david_df = cnty_df[ten_mask & davi_mask]

oak_mask = cnty_df.county == 'Oklahoma' 
oak_df = cnty_df[oak_mask]

diego_mask = cnty_df.county == 'San Diego'
diego_df = cnty_df[diego_mask]

wash_mask = cnty_df.state == 'Washington'
king_mask = cnty_df.county == 'King'
king_df = cnty_df[wash_mask & king_mask]

tex_mask = cnty_df.state == 'Texas'
guad_mask = cnty_df.county == 'Guadalupe'
guad_df = cnty_df[tex_mask & guad_mask]

san_mask = cnty_df.county == 'San Antonio'
san_df = cnty_df[tex_mask & guad_mask]


# utah county
utah_cnty_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(utah_cnty_df.cases.values)])
utah_cnty_df.loc[:,'roll'] = utah_cnty_df.new_cases.rolling(window=7).mean()
utah_cnty_df.plot(x='date',y='roll',title='Utah County 7 Day Rolling Average', legend=False)
plt.savefig('visuals/utah_county')
plt.clf()


# utah state
state_df = pd.read_csv('us-states.csv')
state_df.date = pd.to_datetime(state_df.date,format='%Y-%m-%d')
utah_mask = state_df.state == 'Utah'
utah_st_df = state_df[utah_mask]
utah_st_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(utah_st_df.cases.values)])
utah_st_df.loc[:,'roll'] = utah_st_df.new_cases.rolling(window=7).mean()
utah_st_df.plot(x='date',y='roll',title='Utah State 7 Day Rolling Average',legend=False)
plt.savefig('visuals/utah_state')
plt.clf()


# santa cruz
sc_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(sc_df.cases.values)])
sc_df.loc[:,'roll'] = sc_df.new_cases.rolling(window=7).mean()
sc_df.plot(x='date',y='roll',title='Santa Cruz County 7 Day Rolling Average',legend=False)
plt.savefig('visuals/santa_cruz_county')
plt.clf()


# carson city 
cc_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(cc_df.cases.values)])
cc_df.loc[:,'roll'] = cc_df.new_cases.rolling(window=7).mean()
cc_df.plot(x='date',y='roll',title='Carson City County 7 Day Rolling Average',legend=False)
plt.savefig('visuals/carson_city_county')
plt.clf()


# douglas county
doug_cnty_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(doug_cnty_df.cases.values)])
doug_cnty_df.loc[:,'roll'] = doug_cnty_df.new_cases.rolling(window=7).mean()
doug_cnty_df.plot(x='date',y='roll',title='Douglas County 7 Day Rolling Average',legend=False)
plt.savefig('visuals/douglas_county')
plt.clf()


# washoe county
washoe_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(washoe_df.cases.values)])
washoe_df.loc[:,'roll'] = washoe_df.new_cases.rolling(window=7).mean()
washoe_df.plot(x='date',y='roll',title='Wahsoe County 7 Day Rolling Average',legend=False)
plt.savefig('visuals/washoe_county')
plt.clf()

# jefferson county
jef_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(jef_df.cases.values)])
jef_df.loc[:,'roll'] = jef_df.new_cases.rolling(window=7).mean()
jef_df.plot(x='date',y='roll',title='Jefferson County Kentucky 7 Day Rolling Average of Daily New Cases',legend=False)
plt.savefig('visuals/jefferson_county')
plt.clf()

# floyd county
flo_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(flo_df.cases.values)])
flo_df.loc[:,'roll'] = flo_df.new_cases.rolling(window=7).mean()
flo_df.plot(x='date',y='roll',title='Floyd County Indiana 7 Day Rolling Average of Daily New Cases',legend=False)
plt.savefig('visuals/floyd_county')
plt.clf()

# knox county
knox_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(knox_df.cases.values)])
knox_df.loc[:,'roll'] = knox_df.new_cases.rolling(window=7).mean()
knox_df.plot(x='date',y='roll',title='Knox County Tennesee 7 Day Rolling Average of Daily New Cases',legend=False)
plt.savefig('visuals/knox_county')
plt.clf()

# davidson county
david_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(david_df.cases.values)])
david_df.loc[:,'roll'] = david_df.new_cases.rolling(window=7).mean()
david_df.plot(x='date',y='roll',title='Davidson County Tennesee 7 Day Rolling Average of Daily New Cases',legend=False)
plt.savefig('visuals/davidson_county')
plt.clf()

# oklahoma county
oak_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(oak_df.cases.values)])
oak_df.loc[:,'roll'] = oak_df.new_cases.rolling(window=7).mean()
oak_df.plot(x='date',y='roll',title='Oklahoma County 7 Day Rolling Average of Daily New Cases',legend=False)
plt.savefig('visuals/oklahoma_county')
plt.clf()

# san diego county
diego_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(diego_df.cases.values)])
diego_df.loc[:,'roll'] = diego_df.new_cases.rolling(window=7).mean()
diego_df.plot(x='date',y='roll',title='San Diego County 7 Day Rolling Average of Daily New Cases',legend=False)
plt.savefig('visuals/san_diego_county')
plt.clf()

# king county
king_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(king_df.cases.values)])
king_df.loc[:,'roll'] = king_df.new_cases.rolling(window=7).mean()
king_df.plot(x='date',y='roll',title='King County Washington 7 Day Rolling Average of Daily New Cases',legend=False)
plt.savefig('visuals/king_county')
plt.clf()

# guadalupe county
guad_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(guad_df.cases.values)])
guad_df.loc[:,'roll'] = guad_df.new_cases.rolling(window=7).mean()
guad_df.plot(x='date',y='roll',title='Guadalupe County Texas 7 Day Rolling Average of Daily New Cases',legend=False)
plt.savefig('visuals/guadalupe_county')
plt.clf()

# san antonio county
san_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(san_df.cases.values)])
san_df.loc[:,'roll'] = san_df.new_cases.rolling(window=7).mean()
san_df.plot(x='date',y='roll',title='San Antonio County Texas 7 Day Rolling Average of Daily New Cases',legend=False)
plt.savefig('visuals/san_antonio_county')
plt.clf()

# Texas county
texas_mask = state_df.state == 'Texas'
texas_st_df = state_df[texas_mask]
texas_st_df.loc[:,'new_cases'] = np.hstack([np.array([0]), np.diff(texas_st_df.cases.values)])
texas_st_df.loc[:,'roll'] = texas_st_df.new_cases.rolling(window=7).mean()
texas_st_df.plot(x='date',y='roll',title='Texas State 7 Day Rolling Average',legend=False)
plt.savefig('visuals/texas_state')
plt.clf()

