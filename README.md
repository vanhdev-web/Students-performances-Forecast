# Students Performance Forecast

welcome to my project! this is a machine learning web app that predicts students’ academic performance, especially their writing scores. by applying different regression models, the app provides useful insights and forecasts to help understand and improve student outcomes.

## Table of Contents

- [Dataset Overview](#Dataset_Overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Dataset_Overview
**Dataset statistics**  

![](https://drive.google.com/uc?export=view&id=1f9qdjHMVF-tbdKbNCGn728UreVfTFai6)

**Scatter Plot of Age vs. Pregnancies**  

![](https://drive.google.com/uc?export=view&id=1YXjqOkZktYRPoxRkPf12NqjvKTIdANf1)

**Correlation Matrix**  

![](https://drive.google.com/uc?export=view&id=16TpAAuthxkbfhU6yFMrQ8moQTfVXqdpy)
![](https://drive.google.com/uc?id=1_-k403cGOjBnas2bzTxseujZuJo3BPB2)

**Sample**  

![](https://drive.google.com/uc?id=1Nj2OQKTT3apMXPzQgNTQBKBudF24Tjhx)
## Features

## Features

This project includes the following core functionalities:

*   **Data Loading**: Loads student performance data from an Excel/CSV file (`StudentScore.xls`).
*   **Data Splitting**: Splits the dataset into training and testing sets for robust model development and validation.
*   **Comprehensive Data Preprocessing**: Implements robust data preprocessing steps including handling missing values (using `SimpleImputer`), encoding categorical features (using `OrdinalEncoder` and `OneHotEncoder`), and scaling numerical features (using `StandardScaler`). These steps are orchestrated using `ColumnTransformer` and `Pipeline` for efficiency.
*   **Multiple Model Training**: Trains and evaluates various traditional regression models, including Linear Regression, Decision Tree Regressor, and Random Forest Regressor.
*   **Rapid Model Prototyping**: Utilizes `lazypredict` for rapid prototyping and comparison of a wide array of regression algorithms to quickly identify promising models.
*   **Performance Evaluation**: Calculates and reports key regression performance metrics such as Mean Squared Error (MSE), Mean Absolute Error (MAE), and R2 Score to assess model accuracy.
*   **Reporting**: Generates an HTML report (`student_score_report.html`) summarizing the model's performance and findings.

## Installation

To get started with this project, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vanhdev-web/Students-performances-Forecast.git
    cd Students-performances-Forecast
    ```

2.  **Install the required dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install numpy pandas scikit-learn lazypredict openpyxl
    ```
    *Note: `openpyxl` is required for pandas to read `.xls` files.*

## Usage

To run the student performance forecasting script:

1.  **Ensure Data Availability**: Make sure the `StudentScore.xls` file is located in the same directory as `students_scores.py`. If it's located elsewhere, you will need to update the file path within the `students_scores.py` script.

2.  **Execute the script**:
    ```bash
    python students_scores.py
    ```

3.  **Review Results**: After execution, the script will generate an `student_score_report.html` file in the same directory, which contains a summary of the model's performance and findings.

## Tech Stack

The project is built using the following technologies:

*   **Language**: Python
*   **Libraries/Frameworks**:
    *   `numpy`: Fundamental package for numerical computation.
    *   `pandas`: For data manipulation and analysis.
    *   `scikit-learn`: Comprehensive machine learning library for model building and evaluation.
    *   `lazypredict`: For quick prototyping and comparison of multiple machine learning models.
    *   `openpyxl`: For reading Excel files (`.xls`).

## Project Structure

The repository has a straightforward structure:

```
Students-performances-Forecast/
├── students_scores.py           # Main script for data processing, model training, and evaluation
├── StudentScore.xls             # Dataset containing student performance information
└── student_score_report.html    # Generated HTML report summarizing model results
```

## Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature`).
6.  Open a Pull Request.

## License

This project is open-source and available under the [MIT License](LICENSE).
