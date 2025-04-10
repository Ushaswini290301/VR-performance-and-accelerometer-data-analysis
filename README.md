# Cognitive Function and Movement Measures Analysis

## Project Overview

This project investigates the correlation between cognitive function (Block Design Scores) and VR task completion times, as well as the movement measures (M2) derived from accelerometer data. The analysis is divided into two parts:

- **Part 1**: Evaluating the weak correlation between cognitive function and VR task completion times, and introducing new metrics like average time per step and the number of pauses.
- **Part 2**: Comparing movement measures (M2) with traditional clinical assessments like the Fugl-Meyer Assessment (FMA), using accelerometer data to provide clinically meaningful insights.

---

## Key Insights

### Part 1:
- Weak correlation between cognitive function (Block Design Scores) and VR task completion times.
- New Metrics:
  - **Average time per step**
  - **Number of pauses** (significantly correlating with cognitive function)

### Part 2:
- Movement measures (M2) derived from accelerometer data provide clinically meaningful insights compared to conventional approaches.
- **Scatter plots** and **regression analysis** highlight differences between movement measures and traditional assessments like FMA.

---

## Tools and Technologies

- **Programming**: Python, Jupyter Notebook
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, SciPy
- **Environment**: PyCharm CE
- **Data Formats**: CSV, Excel, ZIP

---

## How to Run

### Part 1: Cognitive Function and VR Task Analysis
1. Open the `part1-assignment-analysis.ipynb` file in Jupyter Notebook.
2. Ensure that all CSV and Excel datasets are placed in the same directory.
3. Run all cells to generate statistical results and visualizations.

### Part 2: Accelerometer Data Analysis
1. Run the `part2-accelerometer-analysis.py` script using PyCharm CE or any compatible Python IDE.
2. Place `patients.csv` and any ZIP files in the project directory.
3. Analyze the generated scatter plots and regression outputs.

---

## Project Files

- **`part1-assignment-analysis.ipynb`**: Jupyter Notebook for analyzing cognitive function and VR task completion times.
- **`part2-accelerometer-analysis.py`**: Python script for analyzing accelerometer data and movement measures.
- **`patients.csv`**: Dataset with patient information used in Part 2.
- **Additional datasets**: Any other data files (e.g., `.csv`, `.xlsx`, `.zip`) used in the analysis.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
