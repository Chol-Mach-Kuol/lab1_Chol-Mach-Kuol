import csv
import sys
import os


def load_csv_data():
    """Prompts for a CSV filename, validates it exists and is non-empty,
    then parses each row into a list of assignment dictionaries."""
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ").strip()

    # Exit early if the file doesn't exist on disk
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert score and weight to floats for arithmetic
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

    # Guard against an empty CSV (e.g., freshly reset by organizer.sh)
    if not assignments:
        print("Error: The CSV file is empty. No grades to process.")
        sys.exit(1)

    return assignments


def evaluate_grades(data):
    """Validates grades and weights, calculates GPA, determines pass/fail,
    and identifies formative assignments eligible for resubmission."""
    print("\n--- Processing Grades ---")

    # a) Every score must be a valid percentage between 0 and 100
    for a in data:
        if not (0 <= a['score'] <= 100):
            print(f"Error: Score {a['score']} for '{a['assignment']}' is out of range (0-100).")
            sys.exit(1)

    # b) Split assignments by group for separate weight and score tracking
    formative = [a for a in data if a['group'].strip().lower() == 'formative']
    summative = [a for a in data if a['group'].strip().lower() == 'summative']

    total_weight     = sum(a['weight'] for a in data)
    formative_weight = sum(a['weight'] for a in formative)
    summative_weight = sum(a['weight'] for a in summative)

    # Enforce the required 60/40 weight split and 100% total
    if total_weight != 100:
        print(f"Error: Total weights sum to {total_weight}, expected 100.")
        sys.exit(1)
    if formative_weight != 60:
        print(f"Error: Formative weights sum to {formative_weight}, expected 60.")
        sys.exit(1)
    if summative_weight != 40:
        print(f"Error: Summative weights sum to {summative_weight}, expected 40.")
        sys.exit(1)

    # c) Weighted score = (score * weight) / 100; sum gives the overall grade out of 100
    total_grade = sum((a['score'] * a['weight']) / 100 for a in data)
    gpa = (total_grade / 100) * 5.0  # Scale to 5.0 GPA

    # Category scores are normalised to their own weight totals (out of 100%)
    formative_score = sum((a['score'] * a['weight']) / formative_weight for a in formative)
    summative_score = sum((a['score'] * a['weight']) / summative_weight for a in summative)

    # d) Student passes only if BOTH category scores are at least 50%
    passed = formative_score >= 50 and summative_score >= 50

    # e) Identify failed formative assignments (score < 50%) for resubmission.
    #    Only the one(s) carrying the highest weight among failures are eligible.
    failed_formative = [a for a in formative if a['score'] < 50]
    resubmit = []
    if failed_formative:
        max_weight = max(a['weight'] for a in failed_formative)
        resubmit = [a for a in failed_formative if a['weight'] == max_weight]

    # f) Print the full grade table
    print(f"\n{'Assignment':<40} {'Group':<12} {'Score':>6} {'Weight':>7} {'Weighted':>9}")
    print("-" * 78)
    for a in data:
        weighted = (a['score'] * a['weight']) / 100
        print(f"{a['assignment']:<40} {a['group']:<12} {a['score']:>6.1f} {a['weight']:>7.1f} {weighted:>9.2f}")

    # Print summary statistics and final decision
    print("-" * 78)
    print(f"\nFormative Score : {formative_score:.2f}% (pass >= 50%)")
    print(f"Summative Score : {summative_score:.2f}% (pass >= 50%)")
    print(f"Total Grade     : {total_grade:.2f}%")
    print(f"GPA             : {gpa:.2f} / 5.0")
    print(f"\nFinal Status    : {'PASSED' if passed else 'FAILED'}")

    # Only show resubmission options when the student has failed
    if not passed and resubmit:
        print("\nEligible for Resubmission (highest-weight failed formative):")
        for a in resubmit:
            print(f"  - {a['assignment']} (Weight: {a['weight']}, Score: {a['score']})")


if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)
