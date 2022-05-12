import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

# the result of select a single column is a serie, in this case, Age
#print(df["Age"])

ages = pd.Series([22,35,58], name="Age")

# algunos metodos

print(df["Age"].max())
print(ages.max())
print(ages.describe())
