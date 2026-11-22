import pandas as pd
from pandas import DataFrame

csv_data="""Alice,20,87
John,19,98
Grace,19,78
Mike,20,90"""

with open("students_data.csv",'w')as f:
  f.write(csv_data)


col_names=['Name','Age','Marks']
data=pd.read_csv('students_data.csv',names=col_names)
print("Imported Data")
print(data)
print("Data imported successfully")

car_data={
    'Brand':['Honda','Tata','Suzuki'],
    'Price':[700000,800000,900000]
}
df=DataFrame(car_data,columns=['Brand','Price'])
df.to_excel('car_data.xlsx',index=False,sheet_name='Sheet1')
print("Exported Data Succesfully")
