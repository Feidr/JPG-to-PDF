from PIL import Image
from reportlab.pdfgen import canvas
import os

def convert_jpg_to_pdf(jpg_files, output_pdf):
    # Create PDF canvas and set the size of each page
    c = canvas.Canvas(output_pdf, pagesize=(600, 850))

    for jpg_file in jpg_files:
        try:
            # Open image file
            img = Image.open(jpg_file)
            # Convert to RGB if it's not
            if img.mode == 'RGBA':
                img = img.convert('RGB')

            # Save the image to a temp jpg file
            temp_file = "temp.jpg"
            img.save(temp_file)

            # Draw image on PDF, dimensions can be changed
            c.drawImage(temp_file, 100, 600, width=400, height=200)

            # Next page
            c.showPage()

            # Remove temp jpg file
            os.remove(temp_file)
        except Exception as e:
            print(f"An error occurred while processing {jpg_file}: {e}")

    # Save PDF
    c.save()

def main():
    print("Enter the names of the JPG files to convert and the name of the output PDF file.")
    jpg_files = input("JPG files (comma-separated, no spaces): ").split(',')
    output_pdf = input("Output PDF file name: ")

    # Ensure the output PDF has the correct extension
    if not output_pdf.endswith('.pdf'):
        output_pdf += '.pdf'

    try:
        convert_jpg_to_pdf(jpg_files, output_pdf)
        print(f"JPG files were converted to {output_pdf} successfully.")
    except FileNotFoundError:
        print("Error: One or more files were not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    input("Press enter to close.")

if __name__ == "__main__":
    main()