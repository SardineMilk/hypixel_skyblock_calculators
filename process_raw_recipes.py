import pandas as pd
import re

df = pd.read_csv('raw_fusion_recipes.csv')

def parse_entry(entry):
    if pd.isna(entry) or not isinstance(entry, str) or entry.strip() == "":
        return "", "", ""
    
    parts = entry.split("x ", 1)
    if len(parts) != 2:
        return "", "", ""

    qty = parts[0].strip()
    rest = parts[1].strip()

    name_end = rest.rfind(" (")
    if name_end == -1:
        return qty, rest, ""  # Assume no ID

    name = rest[:name_end].strip()
    id_start = rest.find("(", name_end)
    id_end = rest.find(")", id_start)
    
    if id_start != -1 and id_end != -1:
        cid = rest[id_start + 1:id_end].strip()
    else:
        cid = ""

    return qty, name, cid
    
processed_rows = []

for _, row in df.iterrows():
    processed_row = []
    for col in df.columns:
        qty, name, cid = parse_entry(row[col])
        processed_row.extend([qty, name, cid])
    processed_rows.append(processed_row)


new_columns = []
for col in df.columns:
    base = col.replace(" ", "").replace("#", "")
    new_columns.extend([f"{base}_Quantity", f"{base}_Name", f"{base}_ID"])


processed_recipes = pd.DataFrame(processed_rows, columns=new_columns)

processed_recipes.to_csv("fusion_recipes.csv", index=False)