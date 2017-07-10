import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df2 = pd.read_csv("Copy of Copy of CSAT Raw Data 2017 YTD (All Support) - Sheet1.csv")

df2.columns = df2.columns.str.replace(" ", "_")


print("Are there any cells with null values: " + str(df2.isnull().values.any())) #There are cells with empty elements
print()

blanks = 0
for cl in df2.columns.values:
	blank = df2[cl].isnull().sum()
	print(cl + " column has " + str(blank) + " null values.")
	blanks += blank

print("Total null values: " + str(blanks) + "\n")

cases = df2.index.size

print("Number of cases: " + str(cases)) #of cases
print("Number of unique cases with null values as CASE: " + str(len(df2.Case.unique())))
print("Number of unique cases w/o null values as CASE: " + str(df2.Case.nunique()))
print()

print("Case Origin Breakdown")
print(df2.Case_Origin.value_counts())
print()
print("Live Ops Inbound Support Call, Live Chat, and Text Message are the main means of inquiry, and")
print("makes up " + str((2417 + 1427 + 1019) * 100 / 6177) + " percent of all queries.")
print("What's interesting is that web-based queries make the most portion of all queries(Live Chat, Email, Web) excluding social media")
print("With at total of 2713 queries, " + str(100 * 2713/6177) + " percent of all queries")
print("Average query/Case Origin: " + str(cases / df2.Case_Origin.value_counts().size))
print("Standarad Deviation: " + str(df2.Case_Origin.value_counts().std()))
print()

print("Case Category Breakdown")
print(df2.Case_Category.value_counts())
print()
print(100 * (df2.Case_Category.value_counts() / df2.Case_Category.value_counts().sum()))
print()
print("We have " + str(df2.Case_Category.value_counts().index.size) + " categories")
print("Requests, Account/Profile, and Refunds are the most handled cases.(1180, 1152, 1050)")
print("It is interesting to point out that Requests, Accounts / Profile, Refunds, Quotes, Reviews, and Credits/Pricing/Payments")
print("make up a big of the queries(86.26%).")
print("Average query/category: " + str(df2.Case_Category.value_counts().mean()))
print("Standard Deviation: " + str(df2.Case_Category.value_counts().std()))
print()


print("CSAT: Owner Name breakdown")
#print(df2["CSAT:_Owner_Name"].value_counts())
print() 
print("We have " + str(df2["CSAT:_Owner_Name"].value_counts().size) + " agents handling 6177 queries")
print("Travis Oliver, Devin Lane, and Sarah Levorsen are the agents with the most queries(107, 103, 94)")
print("Average query/agent: " + str(df2["CSAT:_Owner_Name"].value_counts().mean()))
print("Standard deviation: " + str(df2["CSAT:_Owner_Name"].value_counts().std()))
print()

dq = pd.DataFrame(df2["CSAT:_Owner_Name"].value_counts())
dq.rename(columns={"CSAT:_Owner_Name": "No_of_Queries"}, inplace=True)
print("Agents who only handled single queries")
print(dq.loc[dq.No_of_Queries == 1, :])
print(str(dq.loc[dq.No_of_Queries == 1, :].index.size) + " agents")
print()

print("Team Breakdown")
print(df2.Team.value_counts())
print()
print("We have a total of " + str(df2.Team.value_counts().size) + " teams")
print("TPH Chat, TPH Tier 4, adnd TPH Text are the teams with the most queries(1253, 1126, 796)")
print("Average query/team: " + str(cases / df2.Team.value_counts().size))
print("Standard Deviation: " + str(df2.Team.value_counts().std()))
print()

print("Reporting Manager Breakdown")
print(df2.Reporting_Manager.value_counts())
print()
print("We have " + str(df2.Reporting_Manager.value_counts().index.size) + " Reporting Managers")
print("Average query/manager: " + str(cases / df2.Reporting_Manager.value_counts().size))
print("Standard deviation: " + str(df2.Reporting_Manager.value_counts().std()))
print()


print("Offer Date and Offer Response Date Breakdown")

df2.Offer_Date = pd.to_datetime(df2.Offer_Date)
df2.Offer_Response_Date = pd.to_datetime(df2.Offer_Response_Date)
print()
print("Queries are done in a period of: " + str((((df2.Offer_Date[6176] - df2.Offer_Date[0]) / np.timedelta64(1, "D")).astype(int))) + " days")
print("Queries are responded in a period of: " + str((((df2.Offer_Response_Date[6176] - df2.Offer_Response_Date[0]) / np.timedelta64(1, "D")).astype(int))) + " days")
action_time = ((df2.Offer_Response_Date - df2.Offer_Date) / np.timedelta64(1, "m"))
df2["Action_Time"] = action_time #in minutes
print("Average time till an action from our agents takes place: " + str(df2.Action_Time.mean()) + " mins")
print("Standard Deviation: " + str(df2.Action_Time.std()))
print()

print("Number of interactions to resolution Breakdown")
print(df2.Number_of_interactions_to_resolution.value_counts())
print(df2.Number_of_interactions_to_resolution.value_counts().size)
print()

print("CSAT breakdown")
print(df2.CSAT_Response.value_counts())


subpar_responses = 1295
pct_bad_responses = 100 * (1295/6177)
pct_good_responses = 100 - pct_bad_responses
average_csat_rating = (np.array([5, 1, 4, 3, 2]) * np.array([4331/6177, 573/6177, 551/6177, 364/6177, 358/6177])).sum()

print("pct bad responses: " + str(pct_bad_responses))
print("pct good responses: " + str(pct_good_responses))
print("Avg CSAT rating: " + str(average_csat_rating))
print()

#PART 2 - 4
print("Part 2")

#Time
def CSAT_constructor(df2, n, attr):
	return df2.loc[df2.CSAT_Response == n, attr]

def subpar_pct(df):
    narr, sparr = [], []
    for index_name in df.index.values:
        subpars = df.loc[index_name, 1:3].sum()
        subpars_sum = df.loc[index_name, :].sum()
        narr.append(index_name)
        sparr.append(100 * (subpars / subpars_sum))
    
    return(narr, sparr)

def CSAT_print_mean(a, line):
	print(line)
	for e in (a):
		print(e.values.mean())
def CSAT_print_max(a, line):
	print(line)
	for e in (a):
		print(e.values.max())
def CSAT_print_min(a, line):
	print(line)
	for e in (a):
		print(e.values.min())


a1 =  CSAT_constructor(df2, 1, "Action_Time")
a2 =  CSAT_constructor(df2, 2, "Action_Time")
a3 =  CSAT_constructor(df2, 3, "Action_Time")
a4 =  CSAT_constructor(df2, 4, "Action_Time")
a5 =  CSAT_constructor(df2, 5, "Action_Time")
print()

CSAT_print_mean((a1, a2, a3, a4, a5), "Average Action Time for CSAT responses 1 - 5(in mins)")
CSAT_print_max((a1, a2, a3, a4, a5), "Maximum Action Time for CSAT responses 1 - 5(in mins)")
CSAT_print_min((a1, a2, a3, a4, a5), "Minimum Action Time for CSAT responses 1 - 5(in mins)")

avg_resp = pd.DataFrame({1: a1.mean(),
                         2: a2.mean(),
                         3: a3.mean(),
                         4: a4.mean(),
                         5: a5.mean()
                         }, index = ["Average response time(mins)"])
avg_resp.to_csv("avg_response_time.csv")


#Case Category
cc1 = CSAT_constructor(df2, 1, "Case_Category")
cc2 = CSAT_constructor(df2, 2, "Case_Category")
cc3 = CSAT_constructor(df2, 3, "Case_Category")
cc4 = CSAT_constructor(df2, 4, "Case_Category")
cc5 = CSAT_constructor(df2, 5, "Case_Category")

cc2 = pd.Series(cc2.value_counts(), name=2)
cc3 = pd.Series(cc3.value_counts(), name=3)
cc4 = pd.Series(cc4.value_counts(), name=4)
cc5 = pd.Series(cc5.value_counts(), name=5)

df_cc = pd.DataFrame(cc1.value_counts())
df_cc.rename(columns={"Case_Category":1}, inplace=True)
df_cc = pd.concat([df_cc, cc2, cc3, cc4, cc5], axis = 1)
print(df_cc)
   
cc_params = subpar_pct(df_cc)

df_cc2 = pd.DataFrame(cc_params[1], index=cc_params[0], columns=["subpar_pct"])
df_cc2 = pd.concat([df_cc2, pd.Series(df2.loc[:, "Case_Category"].value_counts(), name="CC_Value_Counts")], axis=1)
print(df_cc2)
print(df_cc2.loc[["Account / Profile", "Quotes", "Refunds", "Requests"],"subpar_pct"].mean())

df_cc.to_csv("case_categories.csv")
df_cc2.to_csv("case_categories1.csv")
print()

#Case Origin
co1 = CSAT_constructor(df2, 1, "Case_Origin")
co2 = CSAT_constructor(df2, 2, "Case_Origin")
co3 = CSAT_constructor(df2, 3, "Case_Origin")
co4 = CSAT_constructor(df2, 4, "Case_Origin")
co5 = CSAT_constructor(df2, 5, "Case_Origin")

co2 = pd.Series(co2.value_counts(), name=2)
co3 = pd.Series(co3.value_counts(), name=3)
co4 = pd.Series(co4.value_counts(), name=4)
co5 = pd.Series(co5.value_counts(), name=5)


df_co = pd.DataFrame(co1.value_counts())
df_co.rename(columns={"Case_Origin":1}, inplace=True)

df_co = pd.concat([df_co, co2, co3, co4, co5], axis = 1)
print(df_co)

   
co2_params = subpar_pct(df_co)

df_co2 = pd.DataFrame(co2_params[1], index=co2_params[0], columns=["subpar_pct"])
df_co2 = pd.concat([df_co2, pd.Series(df2.loc[:, "Case_Origin"].value_counts(), name="CO_Value_Counts")], axis=1)
print(df_co2)
print(df_co2.loc[["Live Chat", "LiveOps Inbound Supoort Call", "Text Message"], "subpar_pct"].mean())

df_co.to_csv("case_origin.csv")
df_co2.to_csv("case_origin1.csv")
print()

#Team
t1 = CSAT_constructor(df2, 1, "Team")
t2 = CSAT_constructor(df2, 2, "Team")
t3 = CSAT_constructor(df2, 3, "Team")
t4 = CSAT_constructor(df2, 4, "Team")
t5 = CSAT_constructor(df2, 5, "Team")

t2 = pd.Series(t2.value_counts(), name=2)
t3 = pd.Series(t3.value_counts(), name=3)
t4 = pd.Series(t4.value_counts(), name=4)
t5 = pd.Series(t5.value_counts(), name=5)

df_t = pd.DataFrame(t1.value_counts())
df_t.rename(columns={"Team":1}, inplace=True)

df_t = pd.concat([df_t, t2, t3, t4, t5], axis = 1)
print(df_t)

t_params = subpar_pct(df_t)

df_t2 = pd.DataFrame(t_params[1], index=t_params[0], columns=["subpar_pct"])
df_t2 = pd.concat([df_t2, pd.Series(df2.loc[:, "Team"].value_counts(), name="Team_Value_Counts")], axis=1)
print(df_t2)

support = df_t2.loc["Support 01" : "Support 12", "subpar_pct"]
TPH_Chat = df_t2.loc["TPH Chat" , "subpar_pct"]
TPH_Tier4 = df_t2.loc["TPH Tier 4" , "subpar_pct"]
t_all = (df_t2.loc[:, "subpar_pct"] * df_t2.loc[:, "Team_Value_Counts"] / 6155).sum() 
print("Avg subpar pct of Team: " + str(t_all)) #weighted
print("Support avg subpar pct: " + str(support.mean()))
print("Queries handled by Support teams: "
     + str(df_t2.loc["Support 01" : "Support 12", "Team_Value_Counts"].sum()))
print("TPH Chat subpar pct: " + str(TPH_Chat))
print("TPH Tier 4 subpar pct: " + str(TPH_Tier4))
support2 = df_t2.loc["Support 01" : "Support 12", "Team_Value_Counts"]
TPH_Chat2 = df_t2.loc["TPH Chat" , "Team_Value_Counts"]
TPH_Tier42 = df_t2.loc["TPH Tier 4" , "Team_Value_Counts"]

print(100 * (support2.sum() + TPH_Chat2.sum() + TPH_Tier42.sum()) / 6177)

df_t.to_csv("team.csv")
df_t2.to_csv("team1.csv")
print()

#Number of interactions to resolution
r1 = CSAT_constructor(df2, 1, "Number_of_interactions_to_resolution")
r2 = CSAT_constructor(df2, 2, "Number_of_interactions_to_resolution")
r3 = CSAT_constructor(df2, 3, "Number_of_interactions_to_resolution")
r4 = CSAT_constructor(df2, 4, "Number_of_interactions_to_resolution")
r5 = CSAT_constructor(df2, 5, "Number_of_interactions_to_resolution")


r2 = pd.Series(r2.value_counts(), name=2)
r3 = pd.Series(r3.value_counts(), name=3)
r4 = pd.Series(r4.value_counts(), name=4)
r5 = pd.Series(r5.value_counts(), name=5)

df_r = pd.DataFrame(r1.value_counts())
df_r.rename(columns={"Number_of_interactions_to_resolution":1}, inplace=True)

df_r = pd.concat([df_r, r2, r3, r4, r5], axis = 1)
print(df_r)


r_params = subpar_pct(df_r)


df_r2 = pd.DataFrame(r_params[1], index=r_params[0], columns=["subpar_pct"])
df_r2 = pd.concat([df_r2, pd.Series(df2.loc[:, "Number_of_interactions_to_resolution"].value_counts(), name="No_of_interactions_to_r_val_counts")], axis=1)

n1 = df2.loc[df2.Number_of_interactions_to_resolution.isnull() & (df2.CSAT_Response == 1), "Number_of_interactions_to_resolution"]
n2 = df2.loc[df2.Number_of_interactions_to_resolution.isnull() & (df2.CSAT_Response == 2), "Number_of_interactions_to_resolution"]
n3 = df2.loc[df2.Number_of_interactions_to_resolution.isnull() & (df2.CSAT_Response == 3), "Number_of_interactions_to_resolution"]
n4 = df2.loc[df2.Number_of_interactions_to_resolution.isnull() & (df2.CSAT_Response == 4), "Number_of_interactions_to_resolution"]
n5 = df2.loc[df2.Number_of_interactions_to_resolution.isnull() & (df2.CSAT_Response == 5), "Number_of_interactions_to_resolution"]

m1 = df2.loc[(df2.CSAT_Response == 1),:].index.size
m2 = df2.loc[(df2.CSAT_Response == 2),:].index.size
m3 = df2.loc[(df2.CSAT_Response == 3),:].index.size
m4 = df2.loc[(df2.CSAT_Response == 4),:].index.size
m5 = df2.loc[(df2.CSAT_Response == 5),:].index.size


print([n1.index.size, n2.index.size, n3.index.size, n4.index.size, n5.index.size])
print([m1, m2, m3, m4, m5])

print(df_r2)

df_r.to_csv("no_of_interactions_to_r.csv")
df_r2.to_csv("no_of_interactions_to_r1.csv")







