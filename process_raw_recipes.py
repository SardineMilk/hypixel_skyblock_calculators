import pandas as pd

df = pd.read_csv('raw_fusion_recipes.csv')

def parse_entry(entry):
    if pd.isna(entry) or not isinstance(entry, str) or entry.strip() == "":
        return "", "", ""
    
    parts = entry.split("x ", 1)
    if len(parts) != 2:
        return "", "", ""

    quantity = parts[0].strip()
    rest = parts[1].strip()

    name_end = rest.rfind(" (")
    if name_end == -1:
        return quantity, rest, ""  # Assume no ID

    name = rest[:name_end].strip()
    id_start = rest.find("(", name_end)
    id_end = rest.find(")", id_start)
    
    if id_start != -1 and id_end != -1:
        shard_id = rest[id_start + 1:id_end].strip()
    else:
        shard_id = ""

    return quantity, name, shard_id
    
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



outputs = []
# Loop through outputs 1 to 3
for i in range(1, 4):
    # Create a new recipe that is only that output
    subset = processed_recipes[['Input1_Quantity', 'Input1_Name', 'Input1_ID',
                 'Input2_Quantity', 'Input2_Name', 'Input2_ID',
                 f'Output{i}_Quantity', f'Output{i}_Name', f'Output{i}_ID']].copy()
    # Rename
    subset = subset.rename(columns={
        f'Output{i}_Quantity': 'Output_Quantity',
        f'Output{i}_Name': 'Output_Name',
        f'Output{i}_ID': 'Output_ID'
    })
    outputs.append(subset)

# Concatenate and drop empty outputs
final_processed_recipes = pd.concat(outputs)
final_processed_recipes = final_processed_recipes[final_processed_recipes['Output_Name'].notna() & (final_processed_recipes['Output_Name'] != '')]

# Reset index
final_processed_recipes = final_processed_recipes.reset_index(drop=True)


final_processed_recipes.to_csv("fusion_recipes.csv", index=False)