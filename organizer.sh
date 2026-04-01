#!/bin/bash
# organizer.sh — Archives grades.csv with a timestamp, resets the workspace,
# and appends a log entry to organizer.log on every run.

ARCHIVE_DIR="archive"
SOURCE_FILE="grades.csv"
LOG_FILE="organizer.log"

# Create the archive directory if it doesn't already exist
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "Created directory: $ARCHIVE_DIR"
fi

# Ensure grades.csv is present before attempting to archive it
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: '$SOURCE_FILE' not found. Nothing to archive."
    exit 1
fi

# Generate a timestamp in YYYYMMDD-HHMMSS format for unique filenames
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
ARCHIVED_NAME="grades_${TIMESTAMP}.csv"

# Rename and move grades.csv into the archive directory
mv "$SOURCE_FILE" "$ARCHIVE_DIR/$ARCHIVED_NAME"
echo "Archived '$SOURCE_FILE' as '$ARCHIVE_DIR/$ARCHIVED_NAME'"

# Create a fresh empty grades.csv so the workspace is ready for the next batch
touch "$SOURCE_FILE"
echo "Created new empty '$SOURCE_FILE'"

# Append one log line per run; the log accumulates across all runs
echo "[$TIMESTAMP] Original: $SOURCE_FILE | Archived: $ARCHIVE_DIR/$ARCHIVED_NAME" >> "$LOG_FILE"
echo "Log updated: $LOG_FILE"
