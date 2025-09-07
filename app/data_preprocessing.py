import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv('data/retail_sales_sample.csv', parse_dates=['date'])
    return df

def preprocess_data(df):
    # For this simple dataset, no missing values or categorical encoding needed
    df = df.sort_values('date')
    return df

def plot_sales(df):
    plt.figure(figsize=(10,5))
    plt.plot(df['date'], df['sales'])
    plt.title('Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.savefig('data/sales_over_time.png')
    plt.close()

if __name__ == '__main__':
    df = load_data()
    df = preprocess_data(df)
    plot_sales(df)
    print('Data loaded, preprocessed, and sales plot saved to data/sales_over_time.png')
