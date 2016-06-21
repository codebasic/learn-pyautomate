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
    table_list = []
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

        try:
            import pandas as pd
            table_frame = pd.DataFrame(table_data)
            table_list.append(table_frame)
        except ImportError:
            # TODO: pandas가 없는 경우 텍스트로 출력
            pass

    return table_list if len(table_list) > 1 else table_list[0]
