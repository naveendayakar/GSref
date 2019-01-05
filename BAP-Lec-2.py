import numpy as np
import pandas as pd
nyc = pd.read_csv('ny.csv')
nyc.head()

# 1) add column 'Party' to the  data frame using the dictionary on slide 33, Lecture 3
nyc.columns
nyc.cand_id.unique()
parties= {'Clinton, Hillary Rodham':'Democrat', 'Sanders, Bernard':'Democrat', 'Trump, Donald J.':'Republican',
"O'Malley, Martin Joseph":'Democrat', "Cruz, Rafael Edward 'Ted'":'Republican',
'Walker, Scott':'Republican', 'Bush, Jeb':'Republican', 'Rubio, Marco':'Republican', 'Kasich, John R.':'Republican',
'Christie, Christopher J.':'Republican', 'Stein, Jill':'Green', 'Johnson, Gary':'Libertarian',
'Graham, Lindsey O.':'Republican', 'Webb, James Henry Jr.':'Democrat',
'Carson, Benjamin S.':'Republican', 'Paul, Rand':'Republican', 'Fiorina, Carly':'Republican',
'Santorum, Richard J.':'Republican', 'Jindal, Bobby':'Republican', 'Huckabee, Mike':'Republican',
'Pataki, George E.':'Republican', 'Gilmore, James S III':'Republican', 'Lessig, Lawrence':'Democrat',
'Perry, James R. (Rick)':'Republican', 'McMullin, Evan':'Independent'}

nyc['party']=nyc.cand_id.map(parties)
nyc.head()


#               file_num tran_id  election_tp     party  
# C00575795     C4732422   P2016          NaN  Democrat  
# C00575795     C4752463   P2016          NaN  Democrat  
# C00577130  VPF7BKZ1KR1   P2016          NaN  Democrat  
# C00577130  VPF7BKWHRY0   P2016          NaN  Democrat  
# C00575795     C4714688   P2016          NaN  Democrat 


# 2) convert the contb_receipt_dt column into an actual data object
nyc['contb_receipt_dt']=pd.to_datetime(nyc['contb_receipt_amt'])
print(nyc.dtypes)
nyc.head()

# contb_receipt_amt     object
# contb_receipt_dt      object
# receipt_desc          object
# memo_cd               object
# memo_text             object

# 3)Using group by, show the number of donations given to each party
nyc.party.value_counts()

# Democrat       574591
# Republican      72983
# Green            1001
# Libertarian       782
# Independent       103


# 4)Using group by, show the number of donations given to each party, by date
nyc.groupby(['party','contb_receipt_amt'])['contbr_occupation'].sum()

# party       contb_receipt_amt
# Democrat    01-APR-16            162457.05
#             01-AUG-15             18560.33
#             01-AUG-16            222029.56
#             01-DEC-15             49278.58
#             01-DEC-16              -205.00
#             01-FEB-16            120723.92?

# 5)Using group by, show the total amount of donations given to each party

nyc.groupby(['party','contbr_occupation'])['contbr_occupation'].sum()

# Republican   2700.00             8675100.00
#              2750.00               11000.00
#              2800.00               16800.00
#              2849.00                5698.00
#              2853.18                2853.18
#              3000.00                6000.00
#              3200.00                6400.00

# 6)Using group by, show the total amount of donations given to each party, by date
nyc.groupby(['party','contb_receipt_amt'])['contbr_occupation'].sum()

# party       contb_receipt_amt
# Democrat    01-APR-16            162457.05
#             01-AUG-15             18560.33
#             01-AUG-16            222029.56
#             01-DEC-15             49278.58
#             01-DEC-16              -205.00
#             01-FEB-16            120723.92
#             01-JAN-16             13554.18

# 7)Which occupations donated the top 5 most money?

nyc7=nyc.groupby(['contbr_employer'])['contbr_occupation'].max()
nyc7
nyc8=nyc7.sort_values()
nyc8.tail()

# contbr_employer
# INVESTMENT MANAGER         10800.00
# SECURITIES TRADER          10800.00
# CHAIRMAN                   10800.00
# INVESTMENT PROFESSIONAL    10800.00
# COUNCIL                    11816.25
# Name: contbr_occupation, dtype: float64

# 8)Which occupations donated the least 5 amount of money?

nyc8.head()

# contbr_employer
# TENANT RELATIONS              -340.0
# HOMECARE DIRECTOR             -200.0
# DIABLED VET.FIGHTING CANCER   -200.0
# ROOF CONSULTANT               -160.0
# LAW OFFICER                   -147.2
# Name: contbr_occupation, dtype: float64
# >>> 

# 9)Which employer's employees gave the most money, give the top 5.
nyc.head()
nyc9=nyc.groupby(['contbr_zip'])['contbr_occupation'].sum().sort_values(ascending=False)
nyc9.head(5)

# contbr_zip
# SELF-EMPLOYED            12060418.91
# RETIRED                   4748780.15
# INFORMATION REQUESTED     3611890.31
# NOT EMPLOYED              1804569.37
# NONE                      1337244.12
# Name: contbr_occupation, dtype: float64



# 10) For each candidate, what were the top 5 occupations that donated to their election

res = nyc.groupby(['cand_id','contbr_occupation']).sum().reset_index()
def top5(group):
    return group.sort_index(by='contb_receipt_amt',ascending=False)[:5]
print(res.groupby('cand_id').apply(top5)[['contbr_occupation','contb_receipt_amt']])

# cand_id                                                                   
# P00003392 8231                                  RETIRED         6817180.60
#           807                                  ATTORNEY         5889758.91
#           5383                                   LAWYER         2827222.52
#           4980                    INFORMATION REQUESTED         2612108.21
#           4770                                HOMEMAKER         1876407.49
# P20002671 10824                                 RETIRED           26566.95
#           10854        TWICE REQUESTED NOT YET RECEIVED           26263.50
#           10856       TWICE REQUESTED, NOT YET RECEIVED           17890.00
#           10853            TWICE REQUESTED NOT RECEIVED           17623.78
#           10855           TWICE REQUESTED, NOT RECEIVED            9764.65
# P20002721 10879                                 RETIRED            4220.00
#           10870  INFORMATION REQUESTED PER BEST EFFORTS            3000.00
#           10873                                 MANAGER            2700.00
#           10864                                CHAIRMAN            2700.00
#           10871                                INVESTOR            2700.00
# P20003281 10887                                  C.E.O.            2700.00
#           10888                                     CEO            2700.00
#           10891  GROUP CFO & HEAD OF CORPORATE DEVELOPM            2700.00
#           10898                                 STUDENT            2700.00
#           10890                        COMMUNITY BANKER            2354.04
# P20003984 11093                                 RETIRED           20119.00
#           10920                                ATTORNEY           14544.00
#           11071                               PROFESSOR            9408.20
#           10942                              CONSULTANT            7359.00
#           10913                                  ARTIST            7315.00
# P40003576 11242                   INFORMATION REQUESTED           22600.00
#           11312                                 RETIRED           21233.74
#           11225                                 FINANCE           13773.75
#           11355                           VICE-CHAIRMAN           10000.00
#           11203                                 DENTIST            7700.00



# 11) For the 5 candidates that raised the most money, graph their donations by time, in a line graph, similar to the chart on slide 39 on lecture 3 ppt


result=nyc.groupby(['cand_id','contb_receipt_dt'])['contb_receipt_amt'].max()
result.head()
result2 = result.reset_index()
result2
result2.head()  



nyc11=nyc.groupby(['cand_id','contb_receipt_dt'])['contb_receipt_amt'].sum()
nyc11
nyc12=nyc11.sort_values(ascending=False)
nyc13=nyc12.head()
nyc14=nyc13.head()
nyc14

nyc14.head()

nyc12

result2.loc[result2['cand_id'] == 'P00003392']
res=result2.loc[result2.index.isin(['P00003392','P60007168','P80001571','P60008059','P60006723'])]
res
res.plot()



result2 = result2.set_index(['cand_id'])
out1=result2.loc['P00003392']
out2= pd.concat([out2,out1])
out2
out1
res


##res is the final result

res['contb_receipt_amt']=pd.to_datetime(res['contb_receipt_amt'])
by_date = res.groupby(['cand_id'])['contb_receipt_amt'].sum()
by_date.unstack('cand_id')
by_date.unstack('cand_id').cumsum().plot()



