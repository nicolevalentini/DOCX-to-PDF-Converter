import os
from docx2pdf import convert

#Define input and output folders
input_folder = os.path.expanduser("~/Desktop/examplefilename")
output_folder = os.path.expanduser("~/Desktop/examplefilenamepdf")

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Convert all .docx files in the input folder to PDF
for filename in os.listdir(input_folder):
    if filename.endswith('.docx'):
        docx_path = os.path.join(input_folder, filename)
        pdf_path = os.path.join(output_folder, filename.replace('.docx', '.pdf'))

        # Convert to PDF
        convert(docx_path, pdf_path)
        print(f'Converted: {filename} to {os.path.basename(pdf_path)}')

print("Conversion completed.")
