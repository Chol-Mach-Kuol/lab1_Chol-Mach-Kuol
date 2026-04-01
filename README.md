# Lab1 - Grade Evaluator & Archiver

## Files
- `grade-evaluator.py` — Calculates GPA, pass/fail status, and resubmission eligibility from a CSV of grades.
- `organizer.sh` — Archives `grades.csv` with a timestamp and resets the workspace.
- `grades.csv` — Sample grade data.

---

## Running the Python Script

**Requirements:** Python 3.x

```bash
python3 grade-evaluator.py
```

When prompted, enter the filename:
```
Enter the name of the CSV file to process (e.g., grades.csv): grades.csv
```

### Expected Output
- Validation of scores (0–100) and weights (Formative=60, Summative=40, Total=100)
- A grade table with weighted scores
- Formative and Summative category scores
- Total Grade and GPA (out of 5.0)
- Final status: `PASSED` or `FAILED`
- If failed: the formative assignment(s) eligible for resubmission

### CSV Format
The `grades.csv` file must have these columns:
```
assignment,group,score,weight
Quiz,Formative,85,20
...
```

---

## Running the Shell Script

**Requirements:** Bash (macOS/Linux)

```bash
chmod +x organizer.sh
./organizer.sh
```

### What it does
1. Creates an `archive/` directory if it doesn't exist.
2. Renames `grades.csv` to `grades_YYYYMMDD-HHMMSS.csv` and moves it to `archive/`.
3. Creates a new empty `grades.csv` in the current directory.
4. Appends a log entry to `organizer.log`.

### Sample log entry (`organizer.log`)
```
[20251105-170000] Original: grades.csv | Archived: archive/grades_20251105-170000.csv
```
