"""
Verification script for Submission_Workbook.xlsx
Tests both dynamic formulas (data_only=False) and cached values (data_only=True)
for all 300 questions, 20 pages, 30 citations, and exceptional criteria.
"""
import openpyxl

print("==================================================")
print("VERIFYING SUBMISSION WORKBOOK (Formulas Mode)")
print("==================================================")
wb = openpyxl.load_workbook('Submission_Workbook.xlsx', data_only=False)

# 00_START
ws00 = wb['00_START']
print('=== 00_START ===')
print('Candidate Name:', ws00['B5'].value)
print('Declaration Accepted:', ws00['B21'].value)
print('Declaration formula B26:', ws00['B26'].value)
print('Ready to submit formula B27:', ws00['B27'].value)

# 01_INSIGHT
ws01 = wb['01_INSIGHT']
obs_cnt = sum(1 for r in range(6, 11) if ws01[f'B{r}'].value)
opp_cnt = sum(1 for r in range(14, 17) if ws01[f'B{r}'].value)
print(f'\n=== 01_INSIGHT ===\nObservations: {obs_cnt}/5 | Opportunities: {opp_cnt}/3')

# 02_QUESTIONS
ws02 = wb['02_QUESTIONS']
q_count = sum(1 for r in range(5, 305) if ws02[f'B{r}'].value)
print(f'\n=== 02_QUESTIONS ===\nTotal Questions: {q_count}/300')

# Check duplicates and completeness across all 300
q_set = set()
duplicates = 0
incomplete = 0
for r in range(5, 305):
    q = ws02[f'B{r}'].value
    if q in q_set:
        duplicates += 1
    q_set.add(q)
    mandatory = [ws02[f'{col}{r}'].value for col in ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'O', 'P', 'R']]
    if not all(val is not None and str(val).strip() != '' for val in mandatory):
        incomplete += 1
print(f'Duplicate questions: {duplicates} (Expected: 0)')
print(f'Incomplete questions: {incomplete} (Expected: 0)')

# 02b_FIXES
ws02b = wb['02b_FIXES']
fixes_cnt = sum(1 for r in range(5, 25) if ws02b[f'B{r}'].value)
validated_cnt = sum(1 for r in range(5, 25) if ws02b[f'H{r}'].value == 'Yes')
print(f'\n=== 02b_FIXES ===\nTotal Fixes: {fixes_cnt}/20 | Validated: {validated_cnt}/20')

# 02c_PAGES_CITATIONS
ws02c = wb['02c_PAGES_CITATIONS']
pages_count = sum(1 for r in range(5, 85) if ws02c[f'B{r}'].value == 'Page')
pages_ready = sum(1 for r in range(5, 85) if ws02c[f'B{r}'].value == 'Page' and ws02c[f'I{r}'].value == 'Ready')
citations_count = sum(1 for r in range(5, 85) if ws02c[f'B{r}'].value == 'Citation target')
print(f'\n=== 02c_PAGES_CITATIONS ===\nPages count: {pages_count} (Ready: {pages_ready}) | Citations count: {citations_count}')

# 04_SELF_CHECK
ws04 = wb['04_SELF_CHECK']
print('\n=== 04_SELF_CHECK Minimums ===')
for r in range(6, 13):
    print(f"Row {r}: {ws04[f'A{r}'].value} | Req: {ws04[f'B{r}'].value} | Your Value: {ws04[f'C{r}'].value} | Formula: {ws04[f'D{r}'].value}")

print('\n=== 04_SELF_CHECK Exceptional Criteria ===')
for r in range(17, 21):
    print(f"Row {r}: Claim: {ws04[f'B{r}'].value} | Value: {ws04[f'C{r}'].value} | Evidence: {str(ws04[f'E{r}'].value)[:60]}...")

print('\n=== 04_SELF_CHECK Self-Score ===')
for r in range(24, 29):
    print(f"Row {r}: {ws04[f'A{r}'].value} = {ws04[f'C{r}'].value}")
print('Formula Total C29:', ws04['C29'].value)

print("\n==================================================")
print("VERIFYING SUBMISSION WORKBOOK (Data-Only Cached Mode)")
print("==================================================")
wb_data = openpyxl.load_workbook('Submission_Workbook.xlsx', data_only=True)
ws00_d = wb_data['00_START']
print('00_START Minimums Met (B24):', ws00_d['B24'].value)
print('00_START Score (B25):', ws00_d['B25'].value)
print('00_START Declaration (B26):', ws00_d['B26'].value)
print('00_START Ready to Submit (B27):', ws00_d['B27'].value)

ws04_d = wb_data['04_SELF_CHECK']
print('\n04_SELF_CHECK Calculated Columns D & F:')
for r in range(6, 13):
    print(f"Row {r}: Req={ws04_d[f'B{r}'].value} | Your={ws04_d[f'C{r}'].value} | Calc D={ws04_d[f'D{r}'].value} | Status F={ws04_d[f'F{r}'].value}")

print('04_SELF_CHECK Cached Total Score (C29):', ws04_d['C29'].value)
print("==================================================")
