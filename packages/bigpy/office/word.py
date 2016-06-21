import docx
import pandas as pd

def Word(filepath_or_buffer=None):
    """
    Extends docx.document.Document
    """
    doc = docx.Document(filepath_or_buffer)
    docx.document.Document.extract_text = extract_text
    docx.document.Document.extract_table = extract_table
    return doc

def extract_text(self):
    return '\n'.join([p.text for p in self.paragraphs])

def extract_table(self):
    table_frame_list = []
    for table in self.tables:
        table_data = []
        for row in table.rows:
            row_data = []
            for cell in row.cells:
                cell_text = ''
                for p in cell.paragraphs:
                    cell_text += p.text
                #print(cell_text, end=' ')
                row_data.append(cell_text)
            #print()
            table_data.append(row_data)

        table_frame = pd.DataFrame(table_data)
        table_frame_list.append(table_frame)

    return table_frame_list if len(table_frame_list) > 1 else table_frame_list[0]
