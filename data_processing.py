import csv
import os

data_directory = './data'

with open('data/daily_sales_formatted.csv', mode='w', newline='') as csv_file:
    fieldnames = ['sales', 'date', 'region']
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(fieldnames)

    for file_name in os.listdir(data_directory):
        if file_name.startswith('daily_sales_data') and file_name.endswith('.csv'):
            file_path = os.path.join(data_directory, file_name)

            with open(file_path, mode='r') as input_file:
                csv_reader = csv.DictReader(input_file)

                for row in csv_reader:
                    if row['product'] == 'pink morsel':
                        price = float(row['price'].replace('$', ''))
                        quantity = int(row['quantity'])
                        sales = price * quantity
                        csv_writer.writerow([sales, row['date'], row['region']])







