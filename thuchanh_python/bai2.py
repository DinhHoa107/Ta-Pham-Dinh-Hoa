import pandas as pd

# Đọc file Excel
df = pd.read_excel("data.xlsx")

# Lọc dữ liệu: vpv1 ≠ 0, pCharge ≠ 0, SOC > 8%
filtered_df = df[(df['vpv1'] != 0) & (df['pCharge'] != 0) & (df['SOC'] > 8)]

# Tính tổng các cột ppv1, ppv2, ppv3
filtered_df['Sum_PPV'] = filtered_df[['ppv1', 'ppv2', 'ppv3']].sum(axis=1)

# Ghi kết quả ra file CSV
filtered_df.to_csv("Data_new.csv", index=False)

print("Hoàn thành. File kết quả: Data_new.csv")