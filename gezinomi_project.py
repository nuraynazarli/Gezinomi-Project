import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.width", 500)
pd.set_option("display.max_columns", None)

df = pd.read_excel(f"C:/Users/User/Downloads/miuul_gezinomi.xlsx")
df.head()

# Task 1
# Question 1
df.info
df.shape
df.index
df.describe()
df.dtypes
df.columns
df.ndim

# Question 2
df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()

# Question 3
df["ConceptName"].nunique()

# Question 4
df.groupby("ConceptName").agg({"SaleId": "count"})
df["ConceptName"].value_counts()

# Question 5
df.groupby("SaleCityName").agg({"Price": "sum"})

# Question 6
df.groupby("ConceptName").agg({"Price": "sum"})

# Question 7
df.groupby("SaleCityName").agg({"Price": "mean"})

# Question 8
df.groupby("ConceptName").agg({"Price": "mean"})

# Question 9
df.groupby(["SaleCityName", "ConceptName"]).agg({"Price": "mean"})

#######################################################################
# Task 2
bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]
df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins=bins, labels=labels)

# Task 3
df.groupby(["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price": ["mean", "count"]})
df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]})
df.groupby(["SaleCityName", "ConceptName", "CheckInDate"]).agg({"Price": ["mean", "count"]})

# Task 4
agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price", ascending=False)

# Task 5
agg_df.reset_index(inplace=True)

# Task 6
agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: "_".join(x).upper(), axis=1)

# Task 7
agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})

# Task 8
agg_df[agg_df["sales_level_based"] == "ANTALYA_HERŞEY DAHIL_HIGH"]["Price"].mean()

agg_df[agg_df["sales_level_based"] == "GIRNE_YARIM PANSIYON_LOW"]["SEGMENT"]
