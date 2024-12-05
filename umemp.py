import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "C:/Users/p.ammu/Desktop/UNEMPLOYMENT/Unemployment/Unemployment in India.csv"
data = pd.read_csv(file_path)

data.columns = data.columns.str.strip()

print("Cleaned Column Names in Dataset:")
print(data.columns)

if 'Date' not in data.columns:
    print("\nError: The column 'Date' does not exist. Please verify the column names.")
else:
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True, errors='coerce')

    data = data.dropna(subset=['Date'])

    data['Estimated Unemployment Rate (%)'] = pd.to_numeric(data['Estimated Unemployment Rate (%)'], errors='coerce')
    data['Estimated Employed'] = pd.to_numeric(data['Estimated Employed'], errors='coerce')

    data = data.dropna(subset=['Estimated Unemployment Rate (%)', 'Estimated Employed'])

    plt.figure(figsize=(12, 6))

    sns.lineplot(data=data, x='Date', y='Estimated Unemployment Rate (%)', marker='o', label='Unemployment Rate (%)')

    sns.lineplot(data=data, x='Date', y='Estimated Employed', marker='o', label='Estimated Employed')

    plt.title('Unemployment Rate and Estimated Employed Over Time')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    plt.grid()

    plt.legend()

    plt.tight_layout()
    plt.savefig("unemployment_rate_and_employed_over_time.png", dpi=300)

    plt.show()
