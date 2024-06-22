import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
file_path1 = 'C:\\Users\\laure\\OneDrive\\Documents\\DATAFUN\\ABIDE\\csv_files\\new_data_abide1.csv'
file_path2 = 'C:\\Users\\laure\\OneDrive\\Documents\\DATAFUN\\ABIDE\\csv_files\\new_data_abide2.csv'
df1 = pd.read_csv(file_path1, usecols=['participant_id', 'DX_GROUP'])
df2 = pd.read_csv(file_path2, usecols=['participant_id', 'DX_GROUP'])

# Remove duplicates based on 'participant_id'
df1_unique = df1.drop_duplicates(subset=['participant_id'])
df2_unique = df2.drop_duplicates(subset=['participant_id'])

# Display first few rows to verify data loading
print(df1_unique.head())
print(df2_unique.head())

# Count for ABIDE I
count_asd_file1 = (df1_unique['DX_GROUP'] == 1).sum()
count_neurotypical_file1 = (df1_unique['DX_GROUP'] == 2).sum()

# Count for ABIDE II
count_asd_file2 = (df2_unique['DX_GROUP'] == 1).sum()
count_neurotypical_file2 = (df2_unique['DX_GROUP'] == 2).sum()

# Display counts
print(f"Count of Autism participants: {count_asd_file1}")
print(f"Count of Neurotypical participants: {count_neurotypical_file1}")
print(f"Count of Autism participants: {count_asd_file2}")
print(f"Count of Neurotypical participants: {count_neurotypical_file2}")

# Total counts across both datasets
total_count_autism = count_asd_file1 + count_asd_file2
total_count_neurotypical = count_neurotypical_file1 + count_neurotypical_file2

# Display total counts
print(f"Total Count of Autism participants: {total_count_autism}")
print(f"Total Count of Neurotypical participants: {total_count_neurotypical}")

# Define labels and counts
labels = ['Autism', 'Neurotypical']
counts = [total_count_autism, total_count_neurotypical]

# Plotting

# Customize colors and edge color
colors = ['#87CEEB', '#FFB6C1']
edge_colors = ['#000000', '#000000']

# Plotting
plt.bar(labels, counts, color=colors, edgecolor=edge_colors)
plt.xlabel('Participant Group', fontsize=11)
plt.ylabel('Number of Participants', fontsize=11)
plt.title('Total Number of Participants with Autism vs. Neurotypical', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)

# Data labels
for i, count in enumerate(counts):
    plt.text(i, count + 1, str(count), ha='center', va='bottom', fontsize=9)

plt.tight_layout()  # Adjustment to lay out to prevent clipping of labels
plt.show()
