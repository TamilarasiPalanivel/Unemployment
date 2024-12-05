import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:/Users/p.ammu/Desktop/UNEMPLOYMENT/Unemployment/Unemployment in India.csv"
data = pd.read_csv(file_path)

# Strip whitespace from column names
data.columns = data.columns.str.strip()

# Display the cleaned column names
print("Cleaned Column Names in Dataset:")
print(data.columns)

# Check if the 'Date' column exists
if 'Date' not in data.columns:
    print("\nError: The column 'Date' does not exist. Please verify the column names.")
else:
    # Convert the 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

    # Drop rows with invalid or missing dates
    data = data.dropna(subset=['Date'])

    # Plotting the unemployment rate
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x='Date', y='Estimated Unemployment Rate (%)', marker='o')
    plt.title('Unemployment Rate Over Time')
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.savefig("unemployment_rate_over_time.png", dpi=300)
    plt.show()
