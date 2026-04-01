# Lab1 - Grade Evaluator & Archiver

**Author:** Chol-Mach-Kuol  
**Course:** Introduction to Python Programming and Databases — BSE Year 1 Trimester 2

---

## Project Files
| File | Description |
|---|---|
| `grade-evaluator.py` | Python script that reads a grades CSV, validates data, calculates GPA, and determines pass/fail status |
| `organizer.sh` | Bash script that archives `grades.csv` with a timestamp and resets the workspace |

---

## 1. Running the Python Script

**Requirements:** Python 3.x

### Setup — Create a `grades.csv` file
Before running, create a `grades.csv` file in the same directory with this exact format:
```
assignment,group,score,weight
Quiz,Formative,85,20
Group Exercise,Formative,40,20
Functions and Debugging Lab,Formative,45,20
Midterm Project - Simple Calculator,Summative,70,20
Final Project - Text-Based Game,Summative,60,20
```

**Rules the CSV must follow:**
- `score` must be between 0 and 100
- All `Formative` weights must sum to exactly **60**
- All `Summative` weights must sum to exactly **40**
- Total of all weights must equal **100**

### Run
```bash
python3 grade-evaluator.py
```

When prompted, enter the filename:
```
Enter the name of the CSV file to process (e.g., grades.csv): grades.csv
```

### Expected Output
```
--- Processing Grades ---

Assignment                               Group         Score  Weight  Weighted
------------------------------------------------------------------------------
Quiz                                     Formative      85.0    20.0     17.00
Group Exercise                           Formative      40.0    20.0      8.00
Functions and Debugging Lab              Formative      45.0    20.0      9.00
Midterm Project - Simple Calculator      Summative      70.0    20.0     14.00
Final Project - Text-Based Game          Summative      60.0    20.0     12.00
------------------------------------------------------------------------------

Formative Score : 56.67% (pass >= 50%)
Summative Score : 65.00% (pass >= 50%)
Total Grade     : 60.00%
GPA             : 3.00 / 5.0

Final Status    : PASSED
```

### Error Handling
| Scenario | Behaviour |
|---|---|
| File not found | Prints error and exits |
| Empty CSV file | Prints error and exits |
| Score outside 0–100 | Prints which assignment failed and exits |
| Weights don't sum correctly | Prints expected vs actual and exits |

---

## 2. Running the Shell Script

**Requirements:** Bash (macOS/Linux)

```bash
chmod +x organizer.sh
./organizer.sh
```

### What it does
1. Creates an `archive/` directory if it doesn't exist
2. Moves `grades.csv` → `archive/grades_YYYYMMDD-HHMMSS.csv`
3. Creates a fresh empty `grades.csv` ready for the next batch
4. Appends a log entry to `organizer.log`

### Sample `organizer.log` entry
```
[20251105-170000] Original: grades.csv | Archived: archive/grades_20251105-170000.csv
```

> Note: Run `organizer.sh` **after** processing grades with `grade-evaluator.py` to archive the current batch.
