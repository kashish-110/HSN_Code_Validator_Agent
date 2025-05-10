import pandas as pd

def load_hsn_data(file_path: str) -> pd.DataFrame:
    hsn_data = pd.read_excel(file_path)
    hsn_data.columns = [col.strip() for col in hsn_data.columns]
    if 'HSNCode' not in hsn_data.columns:
        raise ValueError("Column 'HSNCode' not found.")
    hsn_data['HSNCode'] = hsn_data['HSNCode'].astype(str)
    return hsn_data

def is_valid_format(hsn_code: str) -> bool:
    return hsn_code.isdigit() and len(hsn_code) in [2, 4, 6, 8]

def validate_hsn_code(hsn_code: str, hsn_data: pd.DataFrame) -> dict:
    if not is_valid_format(hsn_code):
        return {"status": "error", "error_message": "Invalid format: must be numeric and 2/4/6/8 digits long."}
    
    row = hsn_data[hsn_data['HSNCode'] == hsn_code]
    if not row.empty:
        return {"status": "success", "report": f"{hsn_code}: {row.iloc[0]['Description']}"}
    return {"status": "error", "error_message": f"HSN code '{hsn_code}' not found."}

def validate_hsn_codes(hsn_codes: list, hsn_data: pd.DataFrame) -> dict:
    return {
        "status": "success",
        "results": [{**validate_hsn_code(code, hsn_data), "code": code} for code in hsn_codes]
    }

def get_parent_codes(hsn_code: str) -> list:
    return [hsn_code[:i] for i in [2, 4, 6] if i < len(hsn_code)]

def validate_hsn_hierarchy(hsn_code: str, hsn_data: pd.DataFrame) -> dict:
    result = validate_hsn_code(hsn_code, hsn_data)
    parents = get_parent_codes(hsn_code)
    existing = [p for p in parents if p in hsn_data['HSNCode'].values]
    result["parent_codes"] = parents
    result["valid_parents"] = existing
    if len(existing) != len(parents):
        missing = list(set(parents) - set(existing))
        result["hierarchy_warning"] = f"Missing parent codes: {missing}"
    return result
