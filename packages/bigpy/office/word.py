import docx
import pandas as pd

def Word(filepath_or_buffer=None):
    """
    Extends docx.document.Document
    """
    doc = docx.Document(filepath_or_buffer)
    docx.document.Document.extract_text = extract_text
    docx.document.Document.extract_tables = extract_tables
    docx.document.Document.tables_to_excel = tables_to_excel
    return doc

def extract_text(self):
    return '\n'.join([p.text for p in self.paragraphs])

def extract_tables(self):
    table_list = []
    for table in self.tables:
        table_data = []
        for row in table.rows:
            row_data = []
            for cell in row.cells:
                cell_text = ''
                for p in cell.paragraphs:
                    cell_text += p.text
                # if debug:
                #     print(cell_text, end=' ')
                row_data.append(cell_text)
            # if debug:
            #     print()
            table_data.append(row_data)

        try:
            import pandas as pd
            table_frame = pd.DataFrame(table_data)
            table_list.append(table_frame)
        except ImportError:
            # TODO: pandas가 없는 경우 텍스트로 출력
            pass

    return table_list[0] if len(table_list) == 1 else table_list

def tables_to_excel(self, filepath_or_buffer):
    table_list = self.extract_tables()

    excel_file = pd.ExcelWriter(filepath_or_buffer)
    for i, table_frame in enumerate(table_list):
        table_frame.to_excel(excel_file, 'Sheet{}'.format(i+1))
    excel_file.save()

    return filepath_or_buffer
