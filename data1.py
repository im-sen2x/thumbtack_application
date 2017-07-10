import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv("Requests_Ops_Analyst_Case_Data.csv")

df1.columns = df1.columns.str.replace(" ",  "_")


#1 A & B
uniqueIDs = df1.User_ID.unique()

print(uniqueIDs.size)
syndicated = (df1[df1.Request_Syndication_Status == 32].index.size)

syndicated_uniques = 0
for uniques in uniqueIDs:
	a = df1[(df1.User_ID == uniques) & (df1.Request_Syndication_Status == 32)]
	if a.index.size > 0:
		syndicated_uniques += a.index.size


print("1A & B")
print(df1.index.size)
print("syndicated requests: " + str(syndicated))
print("non-syndicated requests: " + str(df1.index.size - syndicated))
print("syndicated unique users: " + str(syndicated_uniques))
print("syndicated requests / user: " + str(syndicated_uniques / len(uniqueIDs)))

#1 C
print("1C")
RCIDs = df1.loc[:, "Request_Category_ID"]
print(RCIDs.value_counts().head())
print(RCIDs.value_counts().tail())

print("MOST")
print(df1[df1.Request_Category_ID.isin([97, 12, 96, 1128, 40])]["Request_Title"].value_counts())
print("LEAST")
print(df1[df1.Request_Category_ID.isin([815, 1012, 203, 202, 1179])]["Request_Title"])

#1 D & E
print("1D & E")
df1["Edited_Time"] = df1.Request_Create_Time.str[0:2].astype(int)

hrs_lapsed = 0

for i in range(0, df1.Edited_Time.size):
	try:
		if (df1.Edited_Time[i]) == 59 and (df1.Edited_Time[i +1] == 0):
			hrs_lapsed += 1 
	except:
		break

print("number of hours: " + str(hrs_lapsed))
print("days elapsed: " + str(hrs_lapsed/24))


#2 A
print("2A")
syndicated_request_ids= {}
non_synd_requests =  df1.loc[df1.Request_Syndication_Status != 32, "Request_Status"] #request status
synd_requests =  df1.loc[df1.Request_Syndication_Status == 32, "Request_Status"] #request status

print(non_synd_requests.value_counts()) #to eval
print(synd_requests.value_counts()) #to eval

#2 B
print("2B")
blocked_RCID = df1.loc[df1.Request_Syndication_Status != 32, "Request_Category_ID"]
print(blocked_RCID.value_counts())

print(blocked_RCID.value_counts().head()) #most non-syndicated RCID
print(blocked_RCID.value_counts().tail()) #least non-syndicated RCID
print(blocked_RCID.value_counts().tail().index.values)
print(df1[df1.Request_Category_ID.isin([605, 593, 565, 553, 1291])]["Request_Title"].value_counts())

#AUX
print("AUX")

print("avg syndication rate/wk: " + str(syndicated/df1.size))
print("avg syndication rate/day(6.67 days): " + str(syndicated/df1.size/6.67))

print(df1.loc[df1.Request_Syndication_Status == 32, "Request_Category_ID"].value_counts())

RC_ID_values = df1.Request_Category_ID.values
tsum = 0
for reqc_ids in RC_ID_values:
	x = df1[(df1.Request_Category_ID == reqc_ids)].index.size
	y = df1[(df1.Request_Category_ID == reqc_ids) & (df1.Request_Syndication_Status == 32)].index.size
	tsum += y
	syndicated_request_ids[reqc_ids] = y / x 

print(syndicated_request_ids)

#print(df1.Request_Category_ID.value_counts().size, df1.Request_Category_ID.value_counts().values.sum())
#print(len(syndicated_request_ids), tsum)


ratio_list = sorted(syndicated_request_ids.values(), reverse=True)
ratio_dict = {}

for ratio in ratio_list:
	for k in syndicated_request_ids:
		if syndicated_request_ids[k] == ratio:
			ratio_dict[ratio] = k
			break

print(sorted(ratio_dict.items(), reverse=True)) 
print(sorted(ratio_dict.items(), reverse=True)[0:5])
print(sorted(ratio_dict.items(), reverse=True)[-5::1])  