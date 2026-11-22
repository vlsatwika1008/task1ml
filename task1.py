import pandas as pd
data = pd.read_csv(
    'cardata.csv',
    names=['buying', 'maint', 'doors', 'persons',
           'lug_boot', 'safety', 'class']
)
print(data)
Cars = {
    'Brand': ['Honda Civic', 'Toyota Corolla',
              'Ford Focus', 'Audi A4'],
    'Price': [32000, 35000, 37000, 45000]
}
df = pd.DataFrame(Cars, columns=['Brand', 'Price'])
df.to_excel('export_dataframe.xlsx',
            index=False, header=True)
