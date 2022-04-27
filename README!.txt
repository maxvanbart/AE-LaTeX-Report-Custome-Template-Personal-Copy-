This template must be compiled with XeLaTex, which van be found in the menu in the top left of the overleaf page.

The amount of errors in the template is 8 with 1 contributed by an empty bibliography. This error will be removed once sources are added to the bibliography, thus you report should have 7 errors.
If there are more, there are errors that originated from the code that you added.

Code that can be used in the report can be found in the code for report tex file. Here you can find examples of all the basic code you may need. If there are any additions you think might be usefull please send them to me so I can add them.

Code for the bibliography can be found in the code for bibliography tex file. Make sure to read the provided notes and make sure to ALWAYS pick the most relevant source type and make sure to fill in all required fields. The code in this section is linked to the edited bst file and can thus not be easily customized. If there are any problems with the bibliography code (like missing entry fields), please let me know so I can fix it in the template.

In terms of file management, I would advise to discuss this with your group prior to any files being created to avoid unnecessary messes. I would also advise to discuss labelling prior to writing the report to easily find the label you are looking for.

Good luck with your report and I hope this template is useful,
Jeroen van Daelen

Ps. The cover image is 699x1048px


Change Log:

1-9-2020: 
    - Added SI stuff to CodeForReport.tex
    - Added easily adjustable front page title sizing (line 11 of 01_Cover.tex)

2-9-2020:
    - Edited line 2 of the CodeForBibliography.tex file to incorporate the necessity to remove the comments in the bibliography
    - Removed the optional tag from the year field of @misc in CodeForBibliography.tex as this is a mandatory field

3-9-2020:
    - Fixed the file refrence for the nomenclature tex file in report.tex
    - Added LaTeX plotting support using the pgfplots package, this consists of changes to the report.tex preamble (in the large usepackage list) and an added example to CodeForReport.tex, at the bottom of the report.

7-9-2020:
    - Added a online table generator link to CodeForReport.tex in the table section

9-9-2020:
    - Clarification: If you want to activate the pgfplots in a already existing overleaf file. Uncomment the pgfplots packages in the report.tex file and add the line: "\pgfplotsset{width=15cm,compat=1.9}" to the packages list.
    - If you prefere not to have pages that alternate being shifted to the left and right for easier printing. It is possible to eliminate this by changing line 20 and 24 in the tudelft-AE-report.cls, in these lines change "book" into report. You must also than comment the \frontmatter and \mainmatter lines in the report.tex file. (This procedure will increase the amount of erros slightly but should NOT couse any visible changes to the pdf.)
