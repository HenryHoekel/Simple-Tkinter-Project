import pandas as pd

def export_to_excel(root, frame):

    #self.root = root
    #self.frame = frame

    file_name = 'C:\\Users\\Hank\Documents\\Tkinter_export\\Simple-Tkinter-Project\\hello_world.xlsx'
    excel_writer = pd.ExcelWriter

    with excel_writer(file_name, options={'strings_to_numbers': True}) as writer:

        data_frame.to_excel(writer, sheet_name = 'Sheet1', engine = 'xlsxwriter', float_format ="%.6f")

    excel.visible = True

    print('exported')

#end export_to_excel
