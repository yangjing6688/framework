# This file will generate the Keyword API documentation
import os
import webbrowser
from tempfile import mkstemp
from shutil import move, copymode, rmtree
from os import fdopen, remove

toc_title = dict(xapi_base='XAPI Base Keywords',
                 xapi='XAPI to GUI Keywords')
keyword_contents = dict(xapi_base='keywords.xapi\_base.')


def fileContainsPattern(file_path, pattern):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if pattern in content:
            return True
    return False

def replaceFileContents(file_path, pattern, subst, must_contain=None):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                if must_contain:
                    if must_contain in line:
                        new_file.write(line.replace(pattern, subst))
                    else:
                        new_file.write(line)
                else:
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
if not os.path.exists(docs_rst_files_directory):
    print(f'creating directory: {docs_rst_files_directory}')
    os.mkdir(docs_rst_files_directory)
else:
    print(f'removing directory: {docs_rst_files_directory}')
    rmtree(docs_rst_files_directory)
    print(f'creating directory: {docs_rst_files_directory}')
    os.mkdir(docs_rst_files_directory)

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

        # Replace the name for the TOC
        toc_replace_string = 'keywords.' + keyword_directory.replace('_', '\_') + ' package'
        keyword_file = os.path.join(docs_rst_files_directory,'keywords.' + keyword_directory + '.rst')

        # Adjust the name of the base files
        replaceFileContents(keyword_file, toc_replace_string, toc_title.get(keyword_directory,''))
        replaceFileContents(keyword_file, keyword_contents.get(keyword_directory,''), '')

        # This may be needed in the future when we have multiple directory levels
        # adjust the name for the sub directory files
        # keyword_file_base = keyword_file.replace('.rst', '')
        # for root, dirs, files in os.walk(entire_directory):
        #     for dir in dirs:
        #         if '__' not in dir:
        #             file_name = keyword_file_base + '.' + dir + '.rst'
        #             toc_dir_replace_string = keyword_file_base + '.' + dir + ' package'
        #             if os.path.isfile(file_name):
        #                 replaceFileContents(file_name,'keywords.' + keyword_directory + '.' + dir + '.', '', must_contain=' module')
        #                 replaceFileContents(file_name, ' module', '')
        #                 replaceFileContents(file_name, 'Submodules', '')
        #                 replaceFileContents(file_name, 'Module contents', '')
        #                 replaceFileContents(file_name, toc_dir_replace_string, dir)



# Generate the html
print('Generating HTML')
os.system("make html")
print('Completed')

# Debugging the page
url = "file:build/index.html"
# webbrowser.open(url,new=new)