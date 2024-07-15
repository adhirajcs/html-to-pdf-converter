import pdfkit
import os


def html_to_pdf(input_html, output_pdf):
    """
    Convert an HTML file to a PDF file.

    :param input_html: Path to the input HTML file.
    :param output_pdf: Path to the output PDF file.
    """
    try:

        # Set the XDG_RUNTIME_DIR environment variable
        os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-codespace"

        # Configure path to wkhtmltopdf
        path_to_wkhtmltopdf = "/usr/bin/wkhtmltopdf"  # Note: Change this if wkhtmltopdf is installed elsewhere
        config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

        # Convert HTML to PDF
        pdfkit.from_file(input_html, output_pdf, configuration=config)
        print(f"\nSuccessfully converted {input_html} to {output_pdf}\n")
    except Exception as e:
        print(f"\nError converting {input_html} to {output_pdf}: {e}\n")


# Define directories
html_directory = "html-to-convert"
output_directory = "downloads"

# Ensure the HTML directory exists
if not os.path.exists(html_directory):
    print(f'\nError: The folder "{html_directory}" does not exist. Please create one.\n')
else:
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Find an HTML file in the directory
    html_files = [f for f in os.listdir(html_directory) if f.endswith(".html")]

    if not html_files:
        print(f'\nError: No HTML files found in the folder "{html_directory}"\n.')
    else:
        # Convert the first HTML file found
        input_html = os.path.join(html_directory, html_files[0])
        output_pdf = os.path.join(output_directory, "output.pdf")

        html_to_pdf(input_html, output_pdf)
