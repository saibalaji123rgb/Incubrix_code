"""
IncuBrix Growth Engineer Assessment - Complete Dataset & Workbook Populator
Generates all required baseline data, technical fixes, publish-ready pages,
citation targets, raw answers, visibility.csv, SQLite database, and populates
the official Submission_Workbook.xlsx.
"""

import os
import sys
import json
import csv
import sqlite3
import datetime
import openpyxl

from pathlib import Path
WORKSPACE_DIR = str(Path(__file__).resolve().parent)
MAIN_OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "Main_Output")
RAW_ANSWERS_DIR = os.path.join(MAIN_OUTPUT_DIR, "raw_answers")
DAY1_DIR = os.path.join(RAW_ANSWERS_DIR, "day1")
DAY2_DIR = os.path.join(RAW_ANSWERS_DIR, "day2")
SCREENSHOTS_DIR = os.path.join(MAIN_OUTPUT_DIR, "screenshots")
FIXES_DIR = os.path.join(MAIN_OUTPUT_DIR, "technical_fixes")
PAGES_DIR = os.path.join(MAIN_OUTPUT_DIR, "10_pages")
CITATIONS_DIR = os.path.join(MAIN_OUTPUT_DIR, "citation_plan")
DB_PATH = os.path.join(WORKSPACE_DIR, "Engine", "data", "incubrix_visibility.db")
WORKBOOK_PATH = os.path.join(WORKSPACE_DIR, "Submission_Workbook.xlsx")

# Ensure all target directories exist
for d in [MAIN_OUTPUT_DIR, RAW_ANSWERS_DIR, DAY1_DIR, DAY2_DIR, SCREENSHOTS_DIR, FIXES_DIR, PAGES_DIR, CITATIONS_DIR, os.path.dirname(DB_PATH)]:
    os.makedirs(d, exist_ok=True)

print("Directories verified.")
