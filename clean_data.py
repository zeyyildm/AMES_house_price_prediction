import pandas as pd

df = pd.read_csv('AmesHousing.csv') #import and write data
print(df)
#now we should analize the data
initial_columns = list(df.columns)
print("DATA INFO:\n")
df.info()

#FINDING EMPTY CELLS AND DUPLICATES


#bad data could be: empty cells, data in wrong format, wrong data, duplicates
def is_data_null(df):
    if(df.isnull().sum().sum() == 0): #first sum gives number for one column two sum for all columns total
        print("there are no empty cells in this data")
    else:
        for index, row in df.iterrows(): #index is the row number itterrows lets us go row by row
            null_cols = row[row.isnull()].index.tolist() #find empty cells and converts them to list
            if null_cols:
                print(f"Row {index} has empty cells in columns: {null_cols}")
    

def is_data_duplicate(df):
        duplicates = df[df.duplicated()]
        if len(duplicates) == 0:
             print("no duplicate")
        else:
             print("duplicates in data")
             df.drop_duplicates(inplace=True)

def find_empty_cells_in_columns(df):
     missing_columns = df.isnull().sum()
     print("EMPTY CELLS FOR EVERY COLUMN: \n")
     print(missing_columns.to_string())

special_fill = {
    'Alley': 'NA',
    'Bsmt Qual': 'NA',
    'Bsmt Cond': 'NA',
    'Bsmt Exposure': 'NA',
    'BsmtFin Type 1': 'NA',
    'BsmtFin Type 2': 'NA',
    'Fireplace Qu': 'NA',
    'Garage Type': 'NA',
    'Garage Finish': 'NA',
    'Garage Qual': 'NA',
    'Garage Cond': 'NA',
    'Pool QC': 'NA',
    'Fence': 'NA',
    'Misc Feature': 'NA'
}
df.fillna(special_fill, inplace=True)


def filling_empty_cells(df):
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna("None")
     
is_data_null(df)
is_data_duplicate(df)
find_empty_cells_in_columns(df)
filling_empty_cells(df)
print("AFTER FILLING EMPTY CELLS: \n")
find_empty_cells_in_columns(df)



#DATATYPE FIXING
#we should convery object types to category type because objects are textes and category is integers and it is better for machine learning
#ml models prefer numbers not texts
for col in df.columns:
     if df[col].dtype == 'object':
        df[col] = df[col].astype('category')

#check for numeric columns too. if all numeric columns really contains numbers
#sometimes a numeric column is stored as object because of empty strings or special characters
#ensure no hidden bad data in numerical columns

obj_cols = df.select_dtypes(include=['object']).columns #find object columns
for col in obj_cols:
    converted = pd.to_numeric(df[col], errors='coerce') #convert to numeric for objects fill with NaN
    non_numeric = df[converted.isnull() & df[col].notnull()] #find cant converted value
    if not non_numeric.empty:
        print(f"Column {col} has non-numeric values:")

print("DATA TYPES FOR EACH COLUMN")
print(df.dtypes.to_string())
print("ARE THERE ANY EMPTY CELLS? \n")
is_data_null(df)
print("ARE THERE ANY DUPLICATES? \n")
is_data_duplicate(df)
df.to_csv("cleaned_data.csv")

