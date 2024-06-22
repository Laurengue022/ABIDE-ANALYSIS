import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
file_path1 = 'C:\\Users\\laure\\OneDrive\\Documents\\DATAFUN\\ABIDE\\csv_files\\new_data_abide1.csv'
file_path2 = 'C:\\Users\\laure\\OneDrive\\Documents\\DATAFUN\\ABIDE\\csv_files\\new_data_abide2.csv'
df1 = pd.read_csv(file_path1, usecols=['participant_id', 'DX_GROUP', 'DSM_IV_TR'])
df2 = pd.read_csv(file_path2, usecols=['participant_id', 'DX_GROUP', 'PDD_DSM_IV_TR'])

# Remove NaN values
df1.dropna(inplace=True)
df2.dropna(inplace=True)

# Remove duplicates based on 'participant_id'
df1_unique = df1.drop_duplicates(subset=['participant_id'])
df2_unique = df2.drop_duplicates(subset=['participant_id'])

# Counting participants in each category
count_asd_1 = ((df1_unique['DX_GROUP'] == 1) & (df1_unique['DSM_IV_TR'] == 1)).sum()
count_aspergers_1 = ((df1_unique['DX_GROUP'] == 1) & (df1_unique['DSM_IV_TR'] == 2)).sum()
count_pdd_nos_1 = ((df1_unique['DX_GROUP'] == 1) & (df1_unique['DSM_IV_TR'] == 3)).sum()
count_both_2_3_1 = ((df1_unique['DX_GROUP'] == 1) & (df1_unique['DSM_IV_TR'] == 4)).sum()
count_neurotypical0_1 = ((df1_unique['DX_GROUP'] == 2) & (df1_unique['DSM_IV_TR'] == 0)).sum()


count_asd_2 = ((df2_unique['DX_GROUP'] == 1) & (df2_unique['PDD_DSM_IV_TR'] == 1)).sum()
count_aspergers_2 = ((df2_unique['DX_GROUP'] == 1) & (df2_unique['PDD_DSM_IV_TR'] == 2)).sum()
count_pdd_nos_2 = ((df2_unique['DX_GROUP'] == 1) & (df2_unique['PDD_DSM_IV_TR'] == 3)).sum()
count_both_2_3_2 = ((df2_unique['DX_GROUP'] == 1) & (df2_unique['PDD_DSM_IV_TR'] == 4)).sum()
count_neurotypical0_2 = ((df2_unique['DX_GROUP'] == 2) & (df2_unique['PDD_DSM_IV_TR'] == 0)).sum()

# Total counts for Autism and Neurotypical across both datasets
total_count_asd = count_asd_1 + count_asd_2
total_count_aspergers = count_aspergers_1 + count_aspergers_2
total_count_pdd_nos = count_pdd_nos_1 + count_pdd_nos_2
total_count_both_2_3 = count_both_2_3_1 + count_both_2_3_2
total_count_neurotypical = count_neurotypical0_1 + count_neurotypical0_2

# Display counts
print(f"Count of Autism participants in ABIDE I, Category 1: {count_asd_1}")
print(f"Count of Autism participants in ABIDE I, Category 2: {count_aspergers_1}")
print(f"Count of Autism participants in ABIDE I, Category 3: {count_pdd_nos_1}")
print(f"Count of Autism participants in ABIDE I, Category 4: {count_both_2_3_1}")
print(f"Count of Neurotypical participants in ABIDE I, Category 0: {count_neurotypical0_1}")

print(f"Count of Autism participants in ABIDE II, Category 1: {count_asd_2}")
print(f"Count of Autism participants in ABIDE II, Category 2: {count_aspergers_2}")
print(f"Count of Autism participants in ABIDE II, Category 3: {count_pdd_nos_2}")
print(f"Count of Autism participants in ABIDE II, Category 4: {count_both_2_3_2}")
print(f"Count of Neurotypical participants in ABIDE II, Category 0: {count_neurotypical0_2}")

print(f"Total Count of Autism participants: {total_count_asd}")
print(f"Total Count of Autism participants: {total_count_aspergers}")
print(f"Total Count of Autism participants: {total_count_pdd_nos}")
print(f"Total Count of Autism participants: {total_count_both_2_3}")
print(f"Total Count of Neurotypical participants: {total_count_neurotypical}")

# Pie chart
plt.figure(figsize=(8, 6))

# Data for pie chart
sizes = [total_count_asd, total_count_aspergers, total_count_pdd_nos, total_count_both_2_3, total_count_neurotypical]
labels = ["Autism", "Asperger's", "PDD-NOS", "Asperger's or PDD-NOS", "Neurotypical"]
colors = ['#ADD8E6', '#FFB6C1', '#90ee90', '#FFFF00', '#808080']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Total Participants by Category', fontsize=14)
plt.legend(loc='upper right', fontsize=9)

plt.show()
