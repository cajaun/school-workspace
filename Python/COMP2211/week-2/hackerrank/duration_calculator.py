month_idx = {
    "JAN": 0, "FEB": 1, "MAR": 2, "APR": 3,
    "MAY": 4, "JUN": 5, "JUL": 6, "AUG": 7,
    "SEP": 8, "OCT": 9, "NOV": 10, "DEC": 11
}

pref_2019 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
pref_2020 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

s_mon, s_day = input().split()
e_mon, e_day = input().split()

s_day = int(s_day)
e_day = int(e_day)

s_idx = month_idx[s_mon]
e_idx = month_idx[e_mon]

s_doy = pref_2019[s_idx] + s_day
e_doy_2019 = pref_2019[e_idx] + e_day

if e_doy_2019 >= s_doy:
    print(e_doy_2019 - s_doy + 1)
else:
    rem_2019 = 365 - s_doy + 1
    e_doy_2020 = pref_2020[e_idx] + e_day
    print(rem_2019 + e_doy_2020)
