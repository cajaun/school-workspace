"""build the assignment report from executed notebook results"""

from __future__ import annotations

import ast
import csv
from collections import Counter
from pathlib import Path

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parent
FONT = "Times New Roman"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream))


def set_font(run, size: float = 12, bold: bool | None = None, underline: bool | None = None) -> None:
    run.font.name = FONT
    run._element.rPr.rFonts.set(qn("w:ascii"), FONT)
    run._element.rPr.rFonts.set(qn("w:hAnsi"), FONT)
    run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if underline is not None:
        run.underline = underline
    run.font.color.rgb = RGBColor(0, 0, 0)


def set_table_borders(table) -> None:
    for row in table.rows:
        for cell in row.cells:
            properties = cell._tc.get_or_add_tcPr()
            borders = properties.first_child_found_in("w:tcBorders")
            if borders is None:
                borders = OxmlElement("w:tcBorders")
                properties.append(borders)
            for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
                element = borders.find(qn("w:" + edge))
                if element is None:
                    element = OxmlElement("w:" + edge)
                    borders.append(element)
                element.set(qn("w:val"), "single")
                element.set(qn("w:sz"), "8")
                element.set(qn("w:space"), "0")
                element.set(qn("w:color"), "000000")


def set_cell_text(cell, text: str) -> None:
    cell.text = ""
    paragraph = cell.paragraphs[0]
    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
    paragraph.paragraph_format.line_spacing = 1.0
    paragraph.paragraph_format.space_after = Pt(0)
    run = paragraph.add_run(str(text))
    set_font(run)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER


def add_table(document: Document, headers: list[str], rows: list[list[str]], widths: list[float]) -> None:
    table = document.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    for index, header in enumerate(headers):
        cell = table.rows[0].cells[index]
        cell.width = Inches(widths[index])
        set_cell_text(cell, header)
    for row in rows:
        cells = table.add_row().cells
        for index, value in enumerate(row):
            cells[index].width = Inches(widths[index])
            set_cell_text(cells[index], value)
    set_table_borders(table)
    document.add_paragraph().paragraph_format.space_after = Pt(0)


def add_title(document: Document, text: str) -> None:
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.paragraph_format.line_spacing = 1.0
    paragraph.paragraph_format.space_after = Pt(22)
    run = paragraph.add_run(text)
    set_font(run, size=20, bold=True, underline=True)


def add_major_heading(document: Document, text: str) -> None:
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.paragraph_format.line_spacing = 1.0
    paragraph.paragraph_format.space_before = Pt(16)
    paragraph.paragraph_format.space_after = Pt(8)
    paragraph.paragraph_format.keep_with_next = True
    run = paragraph.add_run(text)
    set_font(run, size=20, bold=True, underline=True)


def add_subheading(document: Document, text: str) -> None:
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
    paragraph.paragraph_format.line_spacing = 1.0
    paragraph.paragraph_format.space_before = Pt(10)
    paragraph.paragraph_format.space_after = Pt(4)
    paragraph.paragraph_format.keep_with_next = True
    run = paragraph.add_run(text)
    set_font(run, size=14, bold=True)


def add_body(document: Document, text: str) -> None:
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
    paragraph.paragraph_format.first_line_indent = Inches(0.5)
    paragraph.paragraph_format.line_spacing = 1.5
    paragraph.paragraph_format.space_after = Pt(0)
    run = paragraph.add_run(text)
    set_font(run)


def add_note(document: Document, text: str) -> None:
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
    paragraph.paragraph_format.line_spacing = 1.5
    paragraph.paragraph_format.space_after = Pt(0)
    run = paragraph.add_run(text)
    set_font(run)


def format_metric(value: str) -> str:
    return f"{float(value):.3f}"


def format_parameters(value: str) -> str:
    parameters = ast.literal_eval(value)
    return ", ".join(f"{key.removeprefix('model__')}={item}" for key, item in parameters.items())


def build_report() -> None:
    train_rows = read_csv(ROOT / "data" / "heart_train.csv")
    test_rows = read_csv(ROOT / "data" / "heart_test.csv")
    baseline = read_csv(ROOT / "baseline_metrics.csv")
    tuned = read_csv(ROOT / "tuned_metrics.csv")
    grid = read_csv(ROOT / "grid_search_results.csv")

    target_counts = Counter(row["HeartDisease"] for row in train_rows)
    train_duplicates = len(train_rows) - len({tuple(row.items()) for row in train_rows})
    test_duplicates = len(test_rows) - len({tuple(row.items()) for row in test_rows})
    resting_bp_zeros = sum(row["RestingBP"] == "0" for row in train_rows)
    cholesterol_zeros = sum(row["Cholesterol"] == "0" for row in train_rows)
    best_tuned = next(row for row in tuned if row["model"] == "random forest")
    best_grid = next(row for row in grid if row["model"] == "random forest")
    simple_nn = next(row for row in baseline if row["model"] == "simple neural network")
    large_nn = next(row for row in baseline if row["model"] == "larger neural network")

    document = Document()
    properties = document.core_properties
    properties.title = ""
    properties.subject = ""
    properties.author = ""
    properties.keywords = ""
    properties.comments = ""
    properties.last_modified_by = ""
    properties.category = ""
    section = document.sections[0]
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

    normal = document.styles["Normal"]
    normal.font.name = FONT
    normal._element.rPr.rFonts.set(qn("w:ascii"), FONT)
    normal._element.rPr.rFonts.set(qn("w:hAnsi"), FONT)
    normal.font.size = Pt(12)

    add_title(document, "Heart Disease Prediction Results and Analysis")
    add_note(document, "COMP3220 Assignment 4")
    add_note(document, "Student ID: 620169526")

    add_major_heading(document, "Data Preparation")
    add_subheading(document, "Data Audit")
    add_table(
        document,
        ["Dataset", "Rows", "Columns", "Missing values", "Duplicate rows"],
        [
            ["Training", len(train_rows), 13, 0, train_duplicates],
            ["Competition", len(test_rows), 12, 0, test_duplicates],
        ],
        [1.35, 0.85, 0.95, 1.35, 1.25],
    )
    add_body(document, f"The training file contains {len(train_rows)} labeled patients, while the competition file contains {len(test_rows)} unlabeled patients. The audit found no missing fields and no duplicate rows in either file. The target contains {target_counts['1']} positive cases and {target_counts['0']} negative cases, giving a minority-to-majority ratio of {min(target_counts.values()) / max(target_counts.values()):.3f}. Accuracy remains interpretable because neither class dominates, but F1, precision, recall, and the confusion matrix provide the evidence needed to see which errors the model makes.")
    add_body(document, f"RestingBP contains {resting_bp_zeros} zero value and Cholesterol contains {cholesterol_zeros} zero values. A zero blood-pressure or cholesterol measurement cannot represent a valid physiological reading in this dataset, so the pipeline treats those values as missing before median imputation. FastingBS and Oldpeak retain their zero values because zero is valid for those variables. This decision changes missing-value markers without discarding patient rows.")

    add_subheading(document, "Preprocessing Decisions")
    add_table(
        document,
        ["Feature group", "Treatment", "Reason"],
        [
            ["PatientId", "Excluded from X", "Identifies a row rather than a clinical measurement"],
            ["Numeric features", "Median imputation and standardization", "Removes invalid sentinels and aligns feature scales"],
            ["Categorical features", "Most-frequent imputation and one-hot encoding", "Preserves category information in numeric form"],
            ["HeartDisease", "Binary target y", "Separates the label from the input features"],
        ],
        [1.25, 2.05, 2.55],
    )
    add_body(document, "PatientId cannot explain disease status, so including it would give the models an identifier with no clinical meaning. The feature pipeline fits its imputer, encoder, and scaler on each training fold. That order prevents the validation data from influencing feature statistics before evaluation. Stratified splitting preserves the observed target ratio in the holdout set and in each cross-validation fold.")

    add_major_heading(document, "Model Performance")
    add_subheading(document, "Baseline Results")
    baseline_order = ["logistic regression", "simple neural network", "larger neural network", "svm", "random forest", "knn"]
    baseline_by_name = {row["model"]: row for row in baseline}
    add_table(
        document,
        ["Model", "Accuracy", "Precision", "Recall", "F1"],
        [[name.title(), format_metric(baseline_by_name[name]["accuracy"]), format_metric(baseline_by_name[name]["precision"]), format_metric(baseline_by_name[name]["recall"]), format_metric(baseline_by_name[name]["f1"])] for name in baseline_order],
        [2.25, 0.9, 0.95, 0.8, 0.5],
    )
    add_subheading(document, "Analysis")
    add_body(document, "The baseline SVM produced the strongest holdout F1 at 0.900 and the highest recall at 0.910. Standardization placed the numeric variables on comparable scales, and the SVM then separated the encoded feature patterns with a margin. Random Forest and the small neural network followed with F1 scores of 0.891 and 0.889. Their similar results suggest that the dataset contains enough structured signal for several model families to perform well.")
    add_body(document, f"The larger neural network fell to {format_metric(large_nn['f1'])} F1, compared with {format_metric(simple_nn['f1'])} for the small network. The larger network has far more parameters than the 818-row training set can constrain from one split, so it can fit variation that does not repeat in the holdout data. KNN reached {format_metric(baseline_by_name['knn']['f1'])} F1, which suggests that local distance relationships became less reliable after one-hot encoding the categorical variables. These comparisons describe this split and support model selection, not a claim that one algorithm will dominate on every sample.")

    tuned_break = document.add_paragraph()
    tuned_break.paragraph_format.page_break_before = True
    add_subheading(document, "Tuned Results")
    tuned_by_name = {row["model"]: row for row in tuned}
    tuned_order = ["logistic regression", "svm", "random forest", "knn"]
    add_table(
        document,
        ["Model", "Accuracy", "Precision", "Recall", "F1", "CV F1"],
        [[name.title(), format_metric(tuned_by_name[name]["accuracy"]), format_metric(tuned_by_name[name]["precision"]), format_metric(tuned_by_name[name]["recall"]), format_metric(tuned_by_name[name]["f1"]), format_metric(tuned_by_name[name]["best_cv_f1"])] for name in tuned_order],
        [1.75, 0.8, 0.9, 0.75, 0.5, 0.65],
    )
    add_subheading(document, "Analysis")
    add_body(document, f"The five-fold search selected Random Forest with {format_parameters(best_grid['best_parameters'])}. Its cross-validation F1 of {format_metric(best_grid['best_cv_f1'])} exceeded SVM at {format_metric(next(row for row in grid if row['model'] == 'svm')['best_cv_f1'])}, Logistic Regression at {format_metric(next(row for row in grid if row['model'] == 'logistic regression')['best_cv_f1'])}, and KNN at {format_metric(next(row for row in grid if row['model'] == 'knn')['best_cv_f1'])}. Selecting from cross-validation limits the risk of choosing a model because of one favorable holdout result.")
    add_body(document, f"The tuned Random Forest reached {format_metric(best_tuned['f1'])} holdout F1, improving on the baseline forest's {format_metric(baseline_by_name['random forest']['f1'])}. The balanced class weight increased attention to the smaller class even though the target distribution was close to balanced. Its precision of {format_metric(best_tuned['precision'])} and recall of {format_metric(best_tuned['recall'])} show a controlled trade-off: the model identifies most positive cases while keeping false alarms below the number of correct positive predictions.")

    add_subheading(document, "Confusion Matrix")
    add_table(
        document,
        ["Actual / predicted", "0", "1"],
        [["0", 67, 8], ["1", 10, 79]],
        [2.3, 1.0, 1.0],
    )
    add_body(document, "The tuned Random Forest classified 67 negative cases and 79 positive cases correctly. It produced eight false positives and ten false negatives. The false-negative count explains why recall remains below one even though the overall accuracy is high. If the application placed a higher cost on missed disease cases, threshold selection or stronger class weighting would deserve a separate experiment. The assignment evaluates prediction metrics rather than clinical decisions, so this result does not support medical use.")

    add_major_heading(document, "Discussion")
    add_subheading(document, "Scaling")
    add_body(document, "Standardization subtracts the training mean from each numeric feature and divides by its training standard deviation. Without that step, Cholesterol and RestingBP would enter optimization with values in the hundreds, while FastingBS would remain between zero and one. Logistic Regression and neural networks use those values in coefficient updates and weight adjustments, so the larger raw units could influence the search more than the feature's predictive value justifies. Scaling puts the numeric evidence on a comparable basis. Random Forest does not depend on distance or gradient magnitude in the same way, but the shared pipeline keeps the comparison consistent.")

    add_subheading(document, "Neural Network Size")
    add_body(document, "The small network achieved 0.878 accuracy and 0.889 F1, while the network with two 100-neuron layers achieved 0.823 accuracy and 0.834 F1. The larger network added capacity without adding more independent patients or stronger evidence. Its lower holdout scores therefore fit a high-variance explanation: the model learned patterns from the training sample that did not transfer to the held-out sample. Repeated cross-validation, early stopping, and stronger regularization would test that explanation, but the assignment's comparison already shows that additional neurons did not improve this run.")

    add_subheading(document, "Class Imbalance")
    add_body(document, "This dataset does not show severe class imbalance because the positive and negative counts are 446 and 372. The workflow still uses stratification and reports F1, precision, recall, and the confusion matrix so a change in class distribution would not hide poor minority-class performance behind accuracy. For a more imbalanced dataset, class weights, threshold adjustment, or resampling could increase minority-class recall. Resampling would need to occur inside each training fold. Applying it before cross-validation would leak duplicated or removed observations into validation data.")

    add_subheading(document, "Limitations")
    add_body(document, "The comparison uses one stratified 80/20 holdout split, so small changes in the split could change the ranking. Five-fold cross-validation reduces that dependence during model selection, but it does not replace an external validation set. The competition labels remain hidden, so the local holdout metrics cannot predict the Kaggle score with certainty. The analysis also tests a limited parameter grid and treats all errors as equally costly. Those constraints define the scope of the conclusion: the tuned Random Forest is the strongest choice among the tested pipelines for this dataset and evaluation design.")

    document.save(ROOT / "report.docx")


if __name__ == "__main__":
    build_report()
