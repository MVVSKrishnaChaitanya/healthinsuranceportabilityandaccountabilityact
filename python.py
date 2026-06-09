import re

def apply_hipaa_safe_harbor(medical_note: str) -> str:
    # 1. Mask Names or specific text patterns (Simplified illustration)
    # 2. Mask Medical Record Numbers (MRN) or ID strings (e.g., 9-digit numbers)
    note_redacted = re.sub(r'\b\d{9}\b', '[REDACTED_ID]', medical_note)
    
    # 3. Mask exact dates (e.g., MM/DD/YYYY)
    note_redacted = re.sub(r'\b\d{2}/\d{2}/\d{4}\b', '[REDACTED_DATE]', note_redacted)
    
    return note_redacted

# Example Usage
raw_note = "Patient John Doe (ID 123456789) was admitted on 10/12/2023."
safe_note = apply_hipaa_safe_harbor(raw_note)

print(safe_note)
# Output: Patient John Doe (ID [REDACTED_ID]) was admitted on [REDACTED_DATE].

