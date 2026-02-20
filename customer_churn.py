import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
url=r"C:\Users\nerth\Desktop\Data Sets\kaggle datasets\customer churn.csv"
df=pd.read_csv(url)
# print(df.info())
#!replacing blank values in totalcharges with 0
# df["TotalCharges"]=df["TotalCharges"].replace(" ",0)

#!converting data type of totalcharges into float
# df["TotalCharges"]=df["TotalCharges"].astype("float")

#!checking total null values
# print(df.isnull().sum().sum())

#!stastistical analysis
# print(df.describe())

#!checking duplicated values
# print(df.duplicated())

#!checking duplicates based on unique column="customerID"
# print(df["customerID"].duplicated().sum())

#!changing values and data type of senior citizen
# def conv(value):
#     if value==0:
#         return "no"
#     else: 
#         return "yes"
# df["SeniorCitizen"]=df["SeniorCitizen"].apply(conv)
# df["SeniorCitizen"]=df["SeniorCitizen"].astype("string")
# print(df["SeniorCitizen"].head(100))

#TODO inspection of data done
#TODO we corrected datatypes , handled null values , understood the basic statistical analysis

#!plotting counts of churn
# ax=sns.countplot(x="Churn",data=df)
# ax.bar_label(ax.containers[0])#*this here puts the total value of count above the bar plot
# plt.show()

#!pie chart
#*using groupby first cause pie chart takes integers to calculate percentage but the Churn column is string
#*groupby returns totals counts of yes and no in Churn in integer format
# gp=df.groupby("gender").agg({"tenure":"count"})#?returns a dataframe
# gp=df.groupby("tenure")["tenure"].count()#? returns a series
# print(gp1)
# print(gp)
# print(gp2)
# sns.kdeplot(x=gp,fill=True)
# plt.show()
# def ten(x):
#     if x>=3 and x<10:
#         return x
#     else:
#         return None
# def yes(x):
#     if x=="Yes":
#         return x
#     else:
#         return None
# df["Churn"]=df["Churn"].apply(yes)
# df.dropna(subset=["Churn"],axis=0,inplace=True)
# # gp3=df.groupby("gender").agg({"tenure":"mean"})
# df["tenure"]=df["tenure"].apply(ten)
# df.dropna(subset=["tenure"],axis=0,inplace=True)
# gp3=df.groupby("tenure")["gender"].agg({"gender":"count"})
# sns.countplot(x=gp3,data=df,hue="gender")
# print(gp3)
# sns.kdeplot(x=df["Churn"],fill=True)
# print(df)
#? you can also use above mentioned group by method the result is some
#? it's just better to use value_counts / size method is working on single column and not multi column relationships
# count=df["Churn"].value_counts()
# plt.pie(count,labels=count.index,autopct="%1.2f%%")
#* this plots a pie chart with the different values in the count variable and label them according to the index's of count
#? the autopct arguement displays perfectages in the piechart according to the format we give
# plt.figure(10,10)
# plt.pie(gp,labels=gp.index,autopct="%1.2f%%")
# plt.title("gender & tenure based pie chart")
# sns.countplot(x="tenure",data=df,hue="gender")
# plt.ylabel("")
# plt.title("gender & tenure based count plot")
# plt.show()
#?[so the pie chart shows us that 25.54% of the customers have churned out]

#!exploring reason behind the ~25% customers churning
# ax=sns.countplot(x="gender",data=df)
# ax.bar_label(ax.containers[0])
# plt.show()
# gp=df.groupby("gender")["Churn"]
# plt.pie(gp.value_counts(),colors='rgb',labels=gp.value_counts().index,autopct="%1.2f%%")
# plt.show()
#? the above gender based analysis can also be done using countplot , pie charts gives % instead of counts
# sns.countplot(x="gender",data=df,hue="Churn")
# plt.show()
#* with the above plot we noticed the % or 
#*the number of people churning or not churning is not related with gender

#!analysing data based on PaymentMethod
# ax=sns.countplot(x="PaymentMethod",data=df,hue="Churn")
# ax.bar_label(ax.containers[0])
# ax.bar_label(ax.containers[1])
# plt.show()


#!analysing data based on Contract
ax=sns.countplot(x="Contract",data=df,hue="Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Contract EDA")
plt.show()

#!analysing data based on Dependents
# ax=sns.countplot(x="Dependents",data=df,hue="Churn")
# pct=ax.containers[0]
# ax.bar_label(ax.containers[0])
# ax.bar_label(ax.containers[1])
# plt.show()

#!exploring data on the basis of services provided
# columns=df.columns.array[6:15]
# n_col=3
# n_rows=(n_col+len(columns)-1)//n_col
# fig,axes=plt.subplots(n_rows,n_col,figsize=(17,n_rows*2))
# axes=axes.flatten()
# for i,col in enumerate(columns):
#     ax=sns.countplot(x=col,ax=axes[i],data=df,hue="Churn")
#     axes[i].set_title(col)
#     axes[i].set_xlabel(col)
#     axes[i].set_ylabel("Count")
#     ax.bar_label(ax.containers[0],label_type="center")
#     ax.bar_label(ax.containers[1],label_type="center")
# for j in range(i + 1, len(axes)):
#     fig.delaxes(axes[j])
# plt.tight_layout()
# plt.show()


