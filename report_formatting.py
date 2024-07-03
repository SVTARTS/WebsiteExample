
import os
import sys
import re
import time
import subprocess



def add_content(content_list):

    all_content = ''

    date = time.strftime("%m/%d/%Y")
    date = date.replace('/', '-')

    title = "Citi Rates Market Update: " 

    all_content = all_content + "\\documentclass{article}" + "\n"
    all_content = all_content + "\\usepackage{graphicx}" + "\n"
    all_content = all_content + f"\\title {{{title}}}" + "\n"

    #all_content = all_content + f"\\date{{{date}}}" + "\n"

    all_content = all_content + ("\\author{DOGE 9000}")  + "\n"

    all_content = all_content + "\\begin{document}"+ "\n"
    all_content = all_content + "\\maketitle" + "\n"
    
    preface  = "The Digital Omnipresent Generative Expert (DOGE) 9000 is an aritifical intelligence system created by \
    Matthew Covington.  This system autonomously parses hundreds of articles and produces daily market updates. \n"

    all_content = all_content + "\\noindent\\rule{\\textwidth}{1pt}"
    all_content = all_content + "\n"
    all_content = all_content + f"\n {preface}"
    all_content = all_content + "\n"
    all_content = all_content + "\\noindent\\rule{\\textwidth}{1pt}"
    all_content = all_content + "\n"

    all_content = all_content + "\n"

    # Dump content into catagories
    for topic, content in content_list.items():

        all_content = all_content + f"\\section{{{topic}}}"
        all_content = all_content + "\n"    
             
        all_content = all_content + content + '\n'

    all_content = all_content + "\\end{document}"

    # Write to a file
    tex_filename = date + "-DOGE9000-MarketUpdate"

    # Create a new .tex file with tex_filename and write all_content to it
    with open (f"{tex_filename}.tex", "w") as f:
        f.write(all_content)
    
    return tex_filename

def convert_tex_to_pdf(tex_filename):

    # Run pdflatex on the .tex file
    subprocess.run(["pdflatex", f"{tex_filename}.tex"])

    # Check for errors and return the error
    if os.path.exists(f"{tex_filename}.log"):
        with open(f"{tex_filename}.log", "r") as f:
            log = f.read()
            if "!" in log:
                print(log)
                return log

    # Remove the .log and .aux files
    os.remove(f"{tex_filename}.log")
    os.remove(f"{tex_filename}.aux")

    print(f"PDF file created: {tex_filename}.pdf")

    return "success"


def main():

    # Create a dictionary for content and article
    content = {'Credit':"This is my credit update", 'Rates':"This is my rates update", 'Equities':"This is my equities update", 'Geopolitics':"This is my geopollitics update", 'Forex':"This is my forex update"}

    tex_filename = add_content(content)
    
    output = convert_tex_to_pdf(tex_filename)

    if output != 'success':
        print(f"Error: {output}")
    else:
        print("Successfully Created File: " + tex_filename + ".pdf")


if __name__ == "__main__":

    main()
    # Theos
