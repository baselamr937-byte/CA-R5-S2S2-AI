"""Project Configuration Module.

Centralizes dataset locations, environment constants, and feature selection rules[cite: 2].
Decoupling these parameters from the preprocessing logic allows changing models
or datasets without refactoring function code[cite: 2].
"""

from typing import List

# File Path Settings
DATA_PATH = "D:/Courses/رواد مصر الرقمية/Techanical/python/CA-R5-S2S2-AI/src/DA_workshop/assignment/project/data/raw/titanic.csv"

# Feature Selection Settings
# Columns that provide high cardinality noise or excessive nulls[cite: 2]
DROP_COLUMNS: List[str] = ["PassengerId", "Name", "Ticket", "Cabin"]