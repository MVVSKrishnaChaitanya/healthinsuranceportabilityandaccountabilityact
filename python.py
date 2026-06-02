import pandas as pd

HIPAA_DIRECT_IDENTIFIERS = ['Name']
QUASI_IDENTIFIERS = ['Age', 'ZIP']


def load_sample_data() -> pd.DataFrame:
    """Return a sample medical dataset for HIPAA de-identification."""
    return pd.DataFrame(
        {
            'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
            'Age': [23, 29, 32, 38, 21],
            'ZIP': [10001, 10003, 90210, 90211, 10002],
            'Diagnosis': ['Flu', 'Cold', 'Flu', 'Diabetes', 'Cold'],
        }
    )


def remove_direct_identifiers(df: pd.DataFrame) -> pd.DataFrame:
    """Remove HIPAA direct identifiers from the dataset."""
    return df.drop(columns=[col for col in HIPAA_DIRECT_IDENTIFIERS if col in df.columns])


def generalize_quasi_identifiers(df: pd.DataFrame) -> pd.DataFrame:
    """Generalize quasi-identifiers to support k-anonymity while preserving sensitive data."""
    result = df.copy()

    if 'Age' in result.columns:
        result['Age_Group'] = pd.cut(
            result['Age'],
            bins=[0, 20, 30, 40, 50, 100],
            labels=['0-19', '20-29', '30-39', '40-49', '50+'],
            include_lowest=True,
        )

    if 'ZIP' in result.columns:
        result['ZIP_Prefix'] = result['ZIP'].astype(str).str[:3] + 'XX'

    return result


def deidentify_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Return a HIPAA de-identified dataset with generalized quasi-identifiers."""
    df = remove_direct_identifiers(df)
    df = generalize_quasi_identifiers(df)
    return df.drop(columns=[col for col in QUASI_IDENTIFIERS if col in df.columns])


def main() -> None:
    df = load_sample_data()
    deidentified = deidentify_dataset(df)
    print(deidentified)


if __name__ == '__main__':
    main()
