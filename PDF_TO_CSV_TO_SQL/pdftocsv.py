import pandas as pd
import fitz


def pdf_to_csv(file_path, output_file_name):
    file = fitz.open(file_path)


    combined_table = pd.DataFrame()
    page = file.load_page(0)
    table_object = page.find_tables()
    tab = table_object[0]
    combined_table =  tab.to_pandas()


    for i in range(1,len(file)):
        page = file.load_page(i)
        table_object = page.find_tables()
        tab = table_object[0]

        table_DF =  tab.to_pandas()
        
        combined_table = pd.concat([combined_table, table_DF], axis = 0)


    combined_table.to_csv(output_file_name+".csv", index = False)


pdf_to_csv(r"purchased_bonds_data.pdf", "purchased_bonds_data")
pdf_to_csv(r"encashed_bonds_data.pdf", "encashed_bonds_data")





