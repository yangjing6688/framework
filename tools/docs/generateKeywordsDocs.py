# This file will generate the Keyword API documentation
import os
import webbrowser
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove

def fileContainsPattern(file_path, pattern):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if pattern in content:
            return True
    return False

def replaceFileContents(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

new = 2 # open in a new tab, if possible

# Remove all of the old files
docs_rst_files_directory = 'source/docs'
for rst_file in os.listdir(docs_rst_files_directory):
    print(f'Removing file: {os.path.join(docs_rst_files_directory, rst_file)}')
    os.remove(os.path.join(docs_rst_files_directory, rst_file))

# Generated the new files
print('Generating new rst files')
index_rst_toc = '   :caption: Table of Contents:\n'
toc_base = 'docs/keywords.'
base_directory = "../../keywords"
toc_file = "source/index.rst"
for keyword_directory in os.listdir(base_directory):
    if not keyword_directory.startswith("__") and \
       not keyword_directory.endswith("__"):
        print(f'Creating documenation for: {keyword_directory}')
        entire_directory = os.path.join(base_directory, keyword_directory)
        # Add the directory to the TOC
        final_toc = toc_base +  keyword_directory
        if not fileContainsPattern(toc_file, final_toc):
            print(f'Adding {final_toc} to TOC')
            replaceFileContents(toc_file, index_rst_toc, index_rst_toc  + "\n   " + final_toc)
    os.system("sphinx-apidoc -o " + docs_rst_files_directory + " " + base_directory)

# Generate the html
print('Generating HTML')
os.system("make html")

url = "file:build/html/index.html"
webbrowser.open(url,new=new)