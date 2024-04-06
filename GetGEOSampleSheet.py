import GEOparse
import pandas as pd
import os

if __name__ == '__main__':

    idat_folder = "idats"

    geo_identifier = input("Enter the GEO identifier: ")

    characteristics_identifier = input("Enter the identifier of characteristics: ")

    file_mapping = {}

    for f in os.listdir(idat_folder):
        if f.endswith('.idat'):
            print("idat file found: ", f)
            file_mapping[f.split('_')[0]] = f

    if not file_mapping:
        print("No idat files found in the directory")
        exit()

    gse = GEOparse.get_GEO(geo=f"GSE{geo_identifier}", destdir="./")

    sample_sheet = pd.DataFrame()

    for _, gsm in gse.gsms.items():
        gsm_name = gsm.name
        basket = {}
        basket['Sample_Name'] = ''
        basket['Sample_Plate'] = ''
        basket['Pool_ID'] = ''
        char_dict = {key: value for item in gsm.metadata['characteristics_ch1'] for key, value in [item.split(': ')]}
        basket['Sample_Group'] = char_dict[characteristics_identifier]
        if gsm_name in file_mapping:
            print(f"Found {gsm_name} in selected idat files")
            basket['Sentrix_ID'] = file_mapping[gsm_name].split('_')[1]
            basket['Sentrix_Position'] = file_mapping[gsm_name].split('_')[2]
            sample_sheet = pd.concat([sample_sheet, pd.DataFrame([basket])], ignore_index=True)
            sample_sheet = pd.concat([sample_sheet, pd.DataFrame([basket])], ignore_index=True)

    sample_sheet.sort_values(by=['Sample_Group', 'Sentrix_ID', 'Sentrix_Position'], inplace=True)
    sample_sheet.reset_index(drop=True, inplace=True)
    sample_sheet['Sample_Name'] = sample_sheet.index + 1
    if not os.path.exists('output'):
        os.makedirs('output')
    sample_sheet.to_csv("output/sample_sheet.csv", index=False)
    print("Sample sheet saved to output/sample_sheet.csv")
