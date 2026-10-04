# Week 4 — Lab 1: Delivery-stop delay exploration

**Assessment:** one individual submission, 5%
**Topic:** univariate exploration
**Business case:** Redwood Delivery Co. wants to describe routine delivery-stop
delays accurately before changing how it communicates service performance.

## Before you start

This is one individual graded lab worth 5%. Complete all requirements in this
one folder, then make **one** D2L submission.

1. Clone or pull the Graded Labs repository.
2. Copy `week-04/lab-01-delivery-delay-exploration` into your private AIDA 2156
   repository. Keep the folder name unchanged.
3. Open the copied folder in VS Code.
4. Run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py analysis/starter.py
```

5. Complete the starter, save all required outputs in `output/`, and complete
   the decision note required by the rubric.
6. Do not push to this instructor repository.

## Your question

Use the supplied fictional data to answer:

> What does the distribution of delivery-stop delay tell the dispatch manager,
> and which records need review before routine performance is reported?

One row is one completed delivery stop. This is exploratory observational data:
you may identify a pattern and recommend a next step, but you must not claim a
cause.

## Dataset

`data/delivery_delays.csv` contains fictional records.

| Column | Type | Meaning |
| --- | --- | --- |
| `delivery_id` | text | Unique fictional delivery-stop identifier. |
| `delivery_window` | category | Morning, afternoon, or evening service window. |
| `route_type` | category | Urban, suburban, or rural route. |
| `delay_minutes` | numeric | Minutes later than the planned arrival time; one value is missing. |
| `package_weight_kg` | numeric | Total package weight for the stop. |

## Start here

1. Copy this entire folder into your assigned private AIDA 2156 repository.
2. In a terminal at the copied folder, install the requirements:

   ```text
   python -m pip install -r requirements.txt
   ```

3. Run the starter file:

   ```text
   python analysis/starter.py
   ```

4. Confirm that `output/starter_profile.csv` was created.
5. Complete the required analysis in `analysis/starter.py` or in a clearly named
   notebook in the `analysis/` folder. Do not delete the supplied validation
   checks.

## Guided analysis section

Complete these small steps for `delay_minutes`:

1. Read the data and state the dataset grain.
2. Verify that `delivery_id` is present and unique.
3. Convert `delay_minutes` to numeric and count missing values.
4. Create a summary with usable-row count, mean, median, minimum, maximum,
   Q1, Q3, and IQR.
5. Calculate an IQR upper fence and create a table of possible high-delay
   records. Keep the records; flagging is not deletion.
6. Create a labelled histogram and box plot for delivery-stop delay.
7. Write a 100–150 word plain-language interpretation. It must state the
   typical delay, distribution shape, whether the mean and median differ, and
   a limitation.

## Independent application section

Apply the same univariate workflow to **one** additional supplied variable:

- `delivery_window`, or
- `package_weight_kg`.

Your work must include:

1. a justified choice of summary and visualization;
2. a labelled output saved in `output/`;
3. a 75–125 word finding for the dispatch manager; and
4. one practical next step and one limitation.

Do not compare groups or claim that one variable caused another outcome. This is
a univariate exploration lab.

## Required deliverables

Keep all work in this one lab folder and include:

- your completed `analysis/starter.py` or notebook;
- `output/delay_summary.csv`;
- `output/possible_high_delays.csv`;
- `output/delay_charts.png`;
- one independent-analysis output in `output/`;
- `decision_note.md`, containing the guided and independent interpretations;
- a short `README.md` update that states how to run your work.

## Submission

This is **one 5% lab submission**. Make meaningful commits, push the completed
lab folder to your assigned private AIDA 2156 repository, and submit **one**
private repository link in D2L. Do not push to an instructor repository.

```powershell
git add .
git commit -m "Complete AIDA 2156 Lab 1"
git push
```

The guided and independent sections are assessed within the one lab rubric;
they are not separate submissions.

## How to run this lab

From this folder in a terminal, run:

```powershell
python -m pip install -r requirements.txt
python analysis/starter.py
```

This creates the starter profile, the required delay outputs, the independent
analysis output, and the decision note in the project folder.

## Academic and data-use reminder

The dataset is fictional. Do not add personal, employer, or confidential data.
If you use permitted AI assistance, follow the course AI-disclosure directions
and verify every result you submit.
