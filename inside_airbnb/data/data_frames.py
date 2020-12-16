import pandas as pd

# Ashville
ashville_lst = pd.read_csv('data/Asheville/listings.csv')
ashville_rvs = pd.read_csv('data/Asheville/reviews.csv')
# Austin
austin_lst = pd.read_csv('data/Austin/listings.csv')
austin_rvs = pd.read_csv('data/Austin/reviews.csv')
# Broward County
broward_lst = pd.read_csv('data/Broward_County/listings.csv')
broward_rvs = pd.read_csv('data/Broward_County/reviews.csv')
# Clark County
clark_lst = pd.read_csv('data/Clark_County/listings.csv')
clark_rvs = pd.read_csv('data/Clark_County/reviews.csv')
# Nashville
nashville_lst = pd.read_csv('data/Nashville/listings.csv')
nashville_rvs = pd.read_csv('data/Nashville/reviews.csv')
# Ottawa
ottawa_lst = pd.read_csv('data/Ottawa/listings.csv')
ottawa_rvs = pd.read_csv('data/Ottawa/reviews.csv')
# Salem, OR
salem_lst = pd.read_csv('data/Salem_OR/listings.csv')
salem_rvs = pd.read_csv('data/Salem_OR/reviews.csv')

all_dfs = [ashville_lst, ashville_rvs, 
           austin_lst, austin_rvs, 
           broward_lst, broward_rvs, 
           clark_lst, clark_rvs, 
           nashville_lst, nashville_rvs, 
           ottawa_lst, ottawa_rvs, 
           salem_lst, salem_rvs]

all_df_names = ['ashville_lst', 'ashville_rvs', 
                'austin_lst', 'austin_rvs', 
                'broward_lst', 'broward_rvs', 
                'clark_lst', 'clark_rvs', 
                'nashville_lst', 'nashville_rvs', 
                'ottawa_lst', 'ottawa_rvs', 
                'salem_lst', 'salem_rvs']

rvs_dfs = [ashville_rvs, 
           austin_rvs, 
           broward_rvs, 
           clark_rvs, 
           nashville_rvs, 
           ottawa_rvs, 
           salem_rvs]

rvs_names = ['ashville_rvs',
             'austin_rvs',
             'broward_rvs',
             'clark_rvs',
             'nashville_rvs', 
             'ottawa_rvs',
             'salem_rvs']