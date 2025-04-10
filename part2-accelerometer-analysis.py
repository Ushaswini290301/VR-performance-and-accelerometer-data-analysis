# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def read_file(name):
    # Importing appropriate packages (.5 point)
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Reading the patients.csv file (.5 point)
    patient_df = pd.read_csv(r'C:\Users\KeerthikaSunchu\Downloads\patients.csv')
    index = patient_df['patient']

    M2_affected = [0 for i in range(len(index))]
    M2_index = 0

    for i in index:
        message_a = "Reading participant #" + str(i)
        print(message_a)

        # Reading the affected side of data for participant # (1 point)
        affected_side = patient_df.loc[patient_df['patient'] == i, 'affected'].values[0]

        message_b = "- Reading the affected arm"
        print(message_b)

        # Concatenating strings to make the appropriate path + filename (1 point)
        base_path = r'C:\Users\ramya\Downloads\log_scores'
        if affected_side.lower() == 'right':
            tmp_affected_file = f'{base_path}\\{i}\\LOG_Right.csv'
        elif affected_side.lower() == 'left':
            tmp_affected_file = f'{base_path}\\{i}\\LOG_Left.csv'
        print(f"Full path to the affected arm data file: {tmp_affected_file}")
        participant_data = pd.read_csv(tmp_affected_file, skiprows=6)
        participant_data.columns = participant_data.columns.str.strip()

        # Extracting appropriate columns (1 point)
        affected_acc_x = np.array(participant_data['Accelerometer x'])
        affected_acc_y = np.array(participant_data['Accelerometer y'])
        affected_acc_z = np.array(participant_data['Accelerometer z'])

        # Computing M2 for the affected arm (1 point)

        affected_acc_mag = np.sqrt(affected_acc_x ** 2 + affected_acc_y ** 2 + affected_acc_z ** 2) - 9.8
        tmp_affected_M2 = np.mean(np.abs(affected_acc_mag))  # Taking the mean of absolute values as M2
        M2_affected[M2_index] = tmp_affected_M2

        M2_index = M2_index + 1

    print(M2_affected)
    # Producing a scatter plot (1 point)
    plt.scatter(patient_df['MAL amount'], M2_affected, label='Data Point')

    # Add labels and title
    plt.xlabel('Therapist-Assessed MAL Scores')
    plt.ylabel('M2 Values')
    plt.title('M2 vs. Therapist-Assessed MAL Scores')

    # Linear fitting using the therapist-assessed MAL scores and the M2 values (1 point)
    coefficients = np.polyfit(patient_df['MAL amount'], M2_affected, 1)
    linear_fit = np.poly1d(coefficients)

    # Add the fitted line to the produced scatter plot (1 point)
    plt.plot(patient_df['MAL amount'], linear_fit(patient_df['MAL amount']), color='red', linestyle='--',
             label='Linear Fit')
    plt.legend()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_file('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
