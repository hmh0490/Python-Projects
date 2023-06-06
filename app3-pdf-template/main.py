from fpdf import FPDF
import pandas as pd

# Portrait vs Landscape
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0) # for the footer

df = pd.read_csv("topics.csv")

# add text via cell method (w=width=0 - cell expands until the end,
# ln=0 - no break line, add the next text right after the cell,
# it should be ln=1 so it goes to next line, h=height should be = size

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100) # RGB
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1) # border=1

    for j in range(20, 298, 10):
        pdf.line(10, j, 200, j) # coordinates of starting and end point in mm

    # break line of 278 mm, height of page, add footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


    for i in range(row["Pages"]-1):
        pdf.add_page()

        for j in range(20, 298, 10):
            pdf.line(10, j, 200, j)

        # starts from the top of the page, add the height of text (12)
        # of the previous page
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")



pdf.output('output.pdf')