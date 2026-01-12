# Purpose:
# Create and save a realistic dataset with known ground truth.

import numpy as np
import pandas as pd


def generate_student_dataset(
    n: int = 4000,
    random_state: int = 42,
    save_path: str | None = None
) -> pd.DataFrame:
    """
    Generate a synthetic student performance dataset suitable for
    hypothesis testing, ANOVA, and regression analysis.

    Parameters
    ----------
    n : int
        Number of samples.
    random_state : int
        Random seed for reproducibility.
    save_path : str or None
        Optional path to save the dataset as CSV.

    Returns
    -------
    pd.DataFrame
        Generated dataset.
    """
    np.random.seed(random_state)

    gender = np.random.choice(["M", "F"], size=n)
    teaching_method = np.random.choice(["A", "B", "C"], size=n, p=[0.3, 0.4, 0.3])
    school_type = np.random.choice(["Public", "Private"], size=n, p=[0.7, 0.3])

    study_hours = np.clip(np.random.normal(6, 2, n), 0, None)
    attendance_rate = np.clip(np.random.normal(80, 10, n), 40, 100)
    previous_gpa = np.clip(np.random.normal(3.0, 0.4, n), 1.5, 4.0)

    method_effect = {"A": 2, "B": 5, "C": -1}
    method_bonus = np.array([method_effect[m] for m in teaching_method])

    gender_effect = np.where(gender == "F", 1.5, 0)

    score = (
        50
        + 3 * study_hours
        + 0.25 * attendance_rate
        + 4 * previous_gpa
        + method_bonus
        + gender_effect
        + np.random.normal(0, 8, n)
    )

    score = np.clip(score, 0, 100)
    passed = (score >= 50).astype(int)

    df = pd.DataFrame({
        "score": score,
        "study_hours": study_hours,
        "attendance_rate": attendance_rate,
        "previous_gpa": previous_gpa,
        "gender": gender,
        "teaching_method": teaching_method,
        "school_type": school_type,
        "passed": passed,
    })

    if save_path is not None:
        df.to_csv(save_path, index=False)

    return df


if __name__ == "__main__":
    df = generate_student_dataset(
        n=4000,
        save_path="../data/student_performance.csv"
    )
    print(df.head())
