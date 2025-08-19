# scripts/etl.py
print("ETL Step: Extracting and Transforming Data...")
with open("etl_output.txt", "w") as f:
    f.write("Alice,28\nBob,34\nCharlie,25\n")
print("ETL complete. File created: etl_output.txt")
