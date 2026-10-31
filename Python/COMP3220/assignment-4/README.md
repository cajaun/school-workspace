# COMP3220 Heart Disease Prediction

This project trains supervised-learning models to predict the `HeartDisease` label in the COMP3220 heart-failure dataset.

## Run the notebook

Install the dependencies from this directory:

```bash
python3 -m pip install -r requirements.txt
```

Start Jupyter:

```bash
python3 -m jupyter notebook
```

Open `heart_failure_assignment.ipynb` and run every cell from top to bottom.

The notebook reads the three files in `data/` and writes the final Kaggle file to `predictions.csv`.

## Project files

- `heart_failure_assignment.ipynb` contains the full analysis and model workflow
- `data/heart_train.csv` contains labeled training examples
- `data/heart_test.csv` contains competition examples without labels
- `data/sample_submission.csv` shows the required prediction format
- `predictions.csv` contains the final predictions after the notebook runs
- `report.docx` contains the written assignment report

The notebook excludes `PatientId` from model features, replaces invalid zero sentinels in `RestingBP` and `Cholesterol`, encodes categorical values, scales numeric values, compares six models, tunes four model families with five-fold cross-validation, and fits the selected model on the full training set.
