"""Data Preprocessing Pipeline Module.

This module provides reusable, dataset-agnostic functions designed to:
1. Ingest tabular CSV data safely with comprehensive error handling[cite: 2].
2. Decouple pipeline configuration by dynamically removing unwanted features[cite: 2].
3. Generate structural data-quality audit reports with transposed views[cite: 2].
"""

from typing import List
import pandas as pd


def Read_data_file(file_path: str) -> pd.DataFrame:
    """Read a CSV file safely and return its contents as a pandas DataFrame[cite: 2].

    This function encapsulates standard file-reading logic and implements
    graceful error handling to intercept missing files, zero-byte (empty) files,
    and corrupted/malformed text rows without causing the entire application to crash[cite: 2].

    Parameters
    ----------
    file_path : str
        The absolute or relative system path targeting the CSV file[cite: 2].

    Returns
    -------
    Optional[pd.DataFrame]
        A pandas DataFrame populated with the tabular data if ingestion succeeds;
        returns `None` if an input/output or parsing error is encountered[cite: 2].

    Raises
    ------
    None
        All standard I/O and pandas-specific parser errors are caught internally
        and communicated via structured console error messages[cite: 2].

    Examples
    --------
    >>> df = Read_data_file("data/raw/titanic.csv")
    >>> if df is not None:
    ...     print(df.shape)
    """
    try:
        dataframe = pd.read_csv(file_path)
        return dataframe
    except FileNotFoundError:
        print(
            f"[Error: File Ingestion Failed] The file at path '{file_path}' does not exist[cite: 2]."
        )
        return None
    except pd.errors.EmptyDataError:
        print(
            f"[Error: Empty Dataset] The file at path '{file_path}' contains no data or columns[cite: 2]."
        )
        return None
    except pd.errors.ParserError as parse_err:
        print(
            f"[Error: Parsing Failure] Failed to parse file content. Details: {parse_err}"
        )
        return None
    except Exception as unexpected_err:
        print(
            f"[Error: Unexpected Failure] An unexpected error occurred while reading '{file_path}': {unexpected_err}[cite: 2]"
        )
        return None


def Drop_unnecessary_features(
    df: pd.DataFrame, cols_to_drop: List[str]
) -> pd.DataFrame:
    """Remove a specified collection of feature columns from a given DataFrame[cite: 2].

    This function contains zero hard-coded domain knowledge of any specific
    dataset (such as Titanic-specific identifiers)[cite: 2]. Instead, it receives the
    exclusion target list dynamically from an external configuration source[cite: 2].

    Parameters
    ----------
    df : pd.DataFrame
        The source DataFrame prior to column pruning. If None is supplied,
        the function safely aborts without attempting matrix operations.
    cols_to_drop : List[str]
        A list containing the exact string labels of the columns to exclude[cite: 2].
        Any non-existent columns provided in this list are quietly ignored
        without raising runtime key errors.

    Returns
    -------
    pd.DataFrame
        A newly created DataFrame containing only the retained features.

    Examples
    --------
    >>> target_exclusions = ["PassengerId", "Name", "Ticket", "Cabin"]
    >>> cleaned_df = Drop_unnecessary_features(df, target_exclusions)
    """
    if df is None:
        print(
            "[Warning: Transformation Skipped] Cannot drop columns from a NoneType object."
        )
        return None

    # errors='ignore' ensures non-existent keys in cols_to_drop will not halt the script
    pruned_df = df.drop(columns=cols_to_drop, errors="ignore")
    return pruned_df


def Check_data_type(df: pd.DataFrame) -> pd.DataFrame:
    """Generate a transposed data-quality summary report for structural auditing[cite: 2].

    Computes critical column metadata to allow quick inspection of features:
    - Column data types (`dtypes`)[cite: 2]
    - Count of distinct/unique values (`nunique()`)[cite: 2]
    - Count of missing/null values (`isnull().sum()`)
    - Percentage of missing data relative to total rows

    The output matrix is transposed (`.T`) so each column in the original dataset
    is represented as a horizontal row in the report, facilitating quick visual
    identification of categorical candidates vs numerical variables[cite: 2].

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame whose schema and health are being audited.

    Returns
    -------
  
        A transposed pandas DataFrame containing the computed quality metrics,
        or None if an empty/invalid DataFrame was passed.

  
    """
    if df is None:
        print("[Warning: Inspection Skipped] Provided DataFrame is None.")
        return None

    quality_summary = pd.DataFrame(
        {
            "Datatype": df.dtypes.astype(str),
            "Unique_Values": df.nunique(),
            "Missing_Values": df.isnull().sum(),
            "Missing_Ratio(%)": ((df.isnull().sum() / len(df)) * 100).round(2),
        }
    )

    # Transpose so columns become horizontal keys for scanning
    return quality_summary.T