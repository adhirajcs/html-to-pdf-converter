# html-to-pdf-converter

This project demonstrates a Python script to convert an HTML file to a PDF using `wkhtmltopdf`.

### Requirements
- Python 3.x
- wkhtmltopdf installed and accessible (version 0.12.5 or later)
- pdfkit Python library (`pip install pdfkit`)

### Setup Instructions
1. **Install Dependencies:**
   - Install `wkhtmltopdf` from [wkhtmltopdf.org](https://wkhtmltopdf.org/) or type `sudo apt install wkhtmltopdf` in your terminal if you are using Ubuntu/Debian based Linux.
   - Install Python dependencies using `pip install pdfkit`.

2. **Environment Variables:**
   - Set `XDG_RUNTIME_DIR` to `/tmp/runtime-codespace` before running the script.

3. **Running the Script:**
   - Adjust paths in `convert_html_to_pdf.py` as needed.
   - Execute the script: `python convert_html_to_pdf.py`.

### Notes
- Ensure all resources (HTML, images, CSS) are referenced locally.
- Verify `wkhtmltopdf` version and configuration (`path_to_wkhtmltopdf` in the script).
- Handle exceptions and errors gracefully during conversion.

### License
This project is licensed under the [Apache License 2.0](LICENSE).
