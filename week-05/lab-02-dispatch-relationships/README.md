# Week 5 — Lab 2: Service-dispatch relationships

**AIDA 2156 | Individual | 5% total | One GitHub/D2L submission**

## Before you start

1. Clone or pull the Graded Labs repository.
2. Copy `week-05/lab-02-dispatch-relationships` into your private AIDA 2156
   repository. Keep the folder name unchanged.
3. Open the copied folder in VS Code and run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py analysis/analysis.py
```

4. Complete every task below and save your work in this same folder.
5. Do not push to this instructor repository.

## Scenario

Northstar Field Services wants to understand whether more difficult service calls require more technician time. Management also wants to know whether service region changes the pattern.

One row in `data/service_dispatches.csv` is one completed field-service dispatch. The dataset is fictional.

## Decision question

What relationship, if any, is visible between `job_difficulty_score` and `technician_hours`, and does `service_region` change the interpretation?

## Your tasks

1. Confirm the row grain and inspect missing values in the three fields used for analysis.
2. Create a scatter plot comparing `job_difficulty_score` and `technician_hours`.
3. Describe direction, form, strength, unusual observations, and any clusters.
4. Produce a grouped summary of technician hours by `service_region` including count, mean, and median.
5. Use region in your visual or comparison to determine whether it changes the apparent relationship.
6. Write a 150–250 word decision note for the operations manager. Include:
   - one evidence-based finding;
   - one practical next step;
   - one limitation or possible confounder;
   - a statement that does not claim causation from this exploratory analysis.

## Required files

Work in your assigned private AIDA 2156 repository. Create this folder there and include:

```text
week-05/lab-02-dispatch-relationships/
  analysis/analysis.py
  output/dispatch_relationships.png
  output/region_summary.csv
  output/decision_note.md
```

You may begin with `analysis/starter.py`, but rename or copy it to `analysis/analysis.py` before submitting.

## Submission

1. Make meaningful commits while completing the work.
2. Push the completed lab folder to your assigned private AIDA 2156 repository.
3. Submit **one link** to that repository through the Lab 2 D2L assignment.

Do not push work to the instructor Graded Labs repository.

```powershell
git add .
git commit -m "Complete AIDA 2156 Lab 2"
git push
```
