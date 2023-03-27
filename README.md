# filter_solutions
A panflute filter to selectively render solutions

Use the following command to apply the filter to the `test.md` file and render the corresponding `test.pdf` file:

`pandoc test.md --filter=./filter_solutions.py -o test.pdf --from markdown`
