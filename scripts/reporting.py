# scripts/reporting.py
print("Reporting Step: Generating report...")
try:
    with open("etl_output.txt", "r") as f:
        data = f.readlines()
    with open("report.txt", "w") as r:
        r.write("Total Records: " + str(len(data)) + "\n")
    print("Report generated: report.txt")
except FileNotFoundError:
    print("Report failed. etl_output.txt not found.")
