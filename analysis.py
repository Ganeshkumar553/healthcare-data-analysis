from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

engine = create_engine("mysql+mysqlconnector://root:Password@localhost/healthcare_analysis")
conn = engine.connect()

print("✅ Connected to MySQL successfully!")

df1 = pd.read_sql("SELECT department, COUNT(*) as total_patients FROM patients GROUP BY department", conn)
df2 = pd.read_sql("SELECT p.department, AVG(t.cost) as avg_cost FROM patients p JOIN treatments t ON p.patient_id = t.patient_id GROUP BY p.department", conn)
df3 = pd.read_sql("SELECT doctor_name, SUM(cost) as total_revenue FROM treatments GROUP BY doctor_name ORDER BY total_revenue DESC", conn)
df4 = pd.read_sql("SELECT gender, COUNT(*) as total FROM patients GROUP BY gender", conn)
df5 = pd.read_sql("SELECT MONTH(admission_date) as month, COUNT(*) as admissions FROM patients GROUP BY month ORDER BY month", conn)
df6 = pd.read_sql("SELECT city, COUNT(*) as total FROM patients GROUP BY city ORDER BY total DESC", conn)

print("\n📊 Patients by Department:")
print(df1)
print("\n💰 Average Cost by Department:")
print(df2)
print("\n👨‍⚕️ Doctor Revenue:")
print(df3)

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Healthcare Data Analysis Dashboard', fontsize=16, fontweight='bold')

axes[0, 0].bar(df1['department'], df1['total_patients'], color='steelblue')
axes[0, 0].set_title('Patients by Department')
axes[0, 0].set_xlabel('Department')
axes[0, 0].set_ylabel('Count')
axes[0, 0].tick_params(axis='x', rotation=45)

axes[0, 1].bar(df2['department'], df2['avg_cost'], color='orange')
axes[0, 1].set_title('Average Treatment Cost by Department')
axes[0, 1].set_xlabel('Department')
axes[0, 1].set_ylabel('Avg Cost (INR)')
axes[0, 1].tick_params(axis='x', rotation=45)

axes[0, 2].bar(df3['doctor_name'], df3['total_revenue'], color='green')
axes[0, 2].set_title('Revenue by Doctor')
axes[0, 2].set_xlabel('Doctor')
axes[0, 2].set_ylabel('Total Revenue (INR)')
axes[0, 2].tick_params(axis='x', rotation=45)

axes[1, 0].pie(df4['total'], labels=df4['gender'], autopct='%1.1f%%', colors=['lightblue', 'pink'])
axes[1, 0].set_title('Gender Distribution')

axes[1, 1].plot(df5['month'], df5['admissions'], marker='o', color='purple')
axes[1, 1].set_title('Monthly Admissions')
axes[1, 1].set_xlabel('Month')
axes[1, 1].set_ylabel('Admissions')

axes[1, 2].barh(df6['city'], df6['total'], color='coral')
axes[1, 2].set_title('Patients by City')
axes[1, 2].set_xlabel('Count')

plt.tight_layout()
plt.savefig('healthcare_dashboard.png', dpi=150)
print("\n✅ Dashboard saved as healthcare_dashboard.png!")

with pd.ExcelWriter('healthcare_report.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Dept_Summary', index=False)
    df2.to_excel(writer, sheet_name='Cost_Analysis', index=False)
    df3.to_excel(writer, sheet_name='Doctor_Revenue', index=False)
    df4.to_excel(writer, sheet_name='Gender_Distribution', index=False)
    df5.to_excel(writer, sheet_name='Monthly_Admissions', index=False)
    df6.to_excel(writer, sheet_name='City_Analysis', index=False)

print("✅ Excel report saved with 6 sheets!")
conn.close()