# Author - Vivek Dilip Kulkarni

# Import packages
import pandas as pd
import os

# global variables
dir_name = os.getcwd()
base_filename = 'input_data'
suffix = 'json'


def calc_bmi_and_new_cols():
    user_input = None
    df = None
    """
    This function will take input data json file, convert it to dataframe,
    create new columns and return the final dataframe
    """
    # First we will initialize the lists
    print("Initializing empty lists \n ")
    new_bmi = []
    bmi_category = []
    bmi_range = []
    health_risk = []
    print("Initializing empty lists done \n ")

    # read the data file
    print("now reading the data file.. \n ")
    print(f"directory path is {dir_name}, file name is {base_filename} with suffix as {suffix}")
    try:
        user_input = pd.read_json(os.path.join(dir_name, base_filename + "." + suffix))
    except Exception as e:
        print(F"Error reading data file {e} \n ")
    else:
        print("Successfully read data file \n ")
    print("Now converting the user input to dataframe \n ")

    # convert the data to pandas dataframe
    try:
        df = pd.DataFrame(user_input)
    except Exception as e:
        print(f"Error converting to dataframe {e} \n ")
    else:
        print("Successfully converted to dataframe \n ")

    # first things first, we will calculate the bmi
    print("Calculating BMI and creating new column \n ")
    for i, j in df.iterrows():
        x, y = j['HeightCm'], j['WeightKg']
        meter = x / 100
        bmi = round(y / (meter ** 2), 2)
        new_bmi.append(bmi)

    # let's create new column called as new_bmi
    df['new_bmi'] = new_bmi
    print("new column bmi successfully created \n ")

    # now we will loop over the column values and create three new columns
    print("Now we will create three new columns \n ")
    try:
        for i, j in enumerate(df['new_bmi'].values):
            if j <= 18.4:
                bmi_category.append('Underweight')
                bmi_range.append('18.4 and below')
                health_risk.append('Malnutrition risk')
            elif 18.5 <= j <= 24.9:
                bmi_category.append('Normal Weight')
                bmi_range.append('18.5 - 24.9')
                health_risk.append('Low risk')
            elif 25 <= j <= 29.9:
                bmi_category.append('Overweight')
                bmi_range.append('25 - 29.9')
                health_risk.append('Enhanced risk')
            elif 30 <= j <= 34.9:
                bmi_category.append('Moderately obese')
                bmi_range.append('30 - 34.9')
                health_risk.append('Medium risk')
            elif 35 <= j <= 39.9:
                bmi_category.append('Severely obese')
                bmi_range.append('35 - 39.9')
                health_risk.append('High risk')
            elif j >= 40:
                bmi_category.append('Very Severely obese')
                bmi_range.append('40 and above')
                health_risk.append('Very High risk')
    except Exception as e:
        print(f"Exception occurred, could not calculate three new columns {e} \n ")
    else:
        print("No error occurred while creating the three columns, therefore proceed with the next step \n ")

    # create three new columns here

    df[['new_bmi', 'bmi_category', 'bmi_range', 'health_risk']] = pd.DataFrame(
        list(zip(new_bmi, bmi_category, bmi_range, health_risk)),
        columns=['new_bmi', 'bmi_category', 'bmi_range', 'health_risk'])
    print("we have successfully created the new columns, here is the final output \n")

    # we will return the final dataframe here
    return print(df)


if __name__ == '__main__':
    print(" \n This program will calculate BMI and create three new columns \n")
    calc_bmi_and_new_cols()
    print(" \n Finish")
