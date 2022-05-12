import pandas as pd

"""
titanic = pd.read_csv('titanic.csv')

# to see the first 10 rows
print(titanic.head(10))

#types interpreted by pandas with attribute dtypes 
print(titanic.dtypes)

# save the dataframe as an excel file
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
"""
# load the dataframe now from the excel file
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
"""
# to read some data about the dataset
print(titanic.info())

age_sex = titanic[["Age","Sex"]]
print(age_sex.head)

print(type(age_sex))

print(titanic[["Age","Sex"]])
"""
# ------------------------------------------------------------------------------------------------------
# FILTER
# ------------------------------------------------------------------------------------------------------
"""
# I’m interested in the passengers older than 35 years.

above_35 = titanic[titanic["Age"]>35]
print(above_35.head())
print(above_35.shape)

# I’m interested in the Titanic passengers from cabin class 2 and 3.

class_23= titanic[titanic["Pclass"].isin([2,3])]
print(class_23.head)

# Another way | or operator & operator

class_2_3 = titanic[(titanic["Pclass"]==2) | (titanic["Pclass"]==3)]
print(class_2_3.head)

# I want to work with passenger data for which the age is known.

age_no_na = titanic[titanic["Age"].notna()]
print(age_no_na.head())
"""
# I’m interested in the names of the passengers older than 35 years.
adult_names= titanic.loc[titanic["Age"]> 35, "Name"]
print(adult_names.head())