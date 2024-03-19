import pandas as pd
import numpy as np
from prettytable import PrettyTable

def read_and_separate_data(file_path):
    df = pd.read_csv(file_path)

    global matclass1, matclass2, matclass3
    matclass1 = np.empty((0, df.shape[1] - 1))
    matclass2 = np.empty((0, df.shape[1] - 1))
    matclass3 = np.empty((0, df.shape[1] - 1))

    for _, row in df.iterrows():
        data = row.values[:-1].reshape(1, -1)

        if row.values[-1] == 1:
            matclass1 = np.vstack((matclass1, data))
        elif row.values[-1] == 2:
            matclass2 = np.vstack((matclass2, data))
        elif row.values[-1] == 3:
            matclass3 = np.vstack((matclass3, data))

def print_matrices():
    global matclass1, matclass2, matclass3

    def print_table(matrix, title):
        table = PrettyTable()
        table.title = title
        table.field_names = [f"Feature {i+1}" for i in range(matrix.shape[1])]
        for row in matrix:
            table.add_row(row)
        print(table)

    print_table(matclass1, "Matrix 1")
    print_table(matclass2, "Matrix 2")
    print_table(matclass3, "Matrix 3")

file_path = "data_with_classes.csv"
read_and_separate_data(file_path)
print_matrices()
 