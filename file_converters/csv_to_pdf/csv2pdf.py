# cerner_2^5_2019

import pandas as pd
import pdfkit as pdf

csv_file = 'test.csv'
html_file = csv_file[:-3]+'html'
pdf_file = csv_file[:-3]+'pdf'

df = pd.read_csv(csv_file, sep=',')
df.to_html(html_file)
pdf.from_file(html_file, pdf_file)