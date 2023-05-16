# This file will generate the Keyword API documentation
import os
from tempfile import mkstemp
from shutil import move, copymode, rmtree
from os import fdopen, remove

source_file_path, filename = os.path.split(os.path.abspath(__file__))
print(f'Running: {filename} in path: {source_file_path}')

toc_title = dict(xapi_base='XAPI Base Keywords',
                 xapi='XAPI to GUI Keywords')
keyword_contents = dict(xapi_base='keywords.xapi\_base.')


def fileContainsPattern(file_path, pattern):
    """
        This will check for the pattern in the file

        :param file_path -  The file path
        :param  pattern - The string pattern to look for

        :return True if the pattern was found and False if is wasn't found
    """
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if pattern in content:
            return True
    return False

def replaceFileContents(file_path, pattern, subst, must_contain=None):
    """
        This will replace the pattern with the subst string passed in if found

        :param file_path -  The file path
        :param pattern - The string pattern to look for
        :param subst - The substitute string 
        :param must_contain - If this is not none, the line must contain this string in order for the replacement to take place

        :return  - None

    """
    #Create temp file
    if os.path.exists(file_path):
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


def create_rst_for_directory(base_directory, docs_rst_files_directory):
    """
        This will create the rst sphinx files for the directory that was passed in and save them in the docs_rst_files_directory.

        :param base_directory - The directory to generate the rst files from
        :param docs_rst_files_directory - The directory to save the generated rst file to

        :return: None
    """
    # Create and modify the RST files
    for keyword_directory in os.listdir(base_directory):
        entire_directory = os.path.join(base_directory, keyword_directory)
        if os.path.isdir(entire_directory) and \
        not keyword_directory.startswith("__") and \
        not keyword_directory.endswith("__"):
            print(f'Creating documentation for: {entire_directory}')

            # Add the directory to the TOC
            partial_directory = entire_directory[entire_directory.index("../../")+6:]
            final_toc = "docs/" + partial_directory.replace('keywords/', '')

            if partial_directory == 'keywords/gui' or partial_directory == 'keywords/xapi_base':
                if not fileContainsPattern(toc_file, final_toc):
                    print(f'Adding {final_toc} to TOC')
                    replaceFileContents(toc_file, index_rst_toc, index_rst_toc  + "\n   " + final_toc)

                # Generate the doc files
                os.system("export SPHINX_APIDOC_OPTIONS=members,undoc-members && sphinx-apidoc -d 1 -M --tocfile " + keyword_directory + " -o " + docs_rst_files_directory + " " + os.path.join(base_directory, keyword_directory))

                # Replace the name for the TOC
                toc_replace_string = 'keywords.' + keyword_directory.replace('_', '\_') + ' package'
                keyword_file = os.path.join(docs_rst_files_directory,'keywords.' + keyword_directory + '.rst')

                # Check this directory for other directories
                create_rst_for_directory(entire_directory, docs_rst_files_directory)

# Remove all of the old files
docs_rst_files_directory = os.path.join(source_file_path, 'source','docs')
if not os.path.exists(docs_rst_files_directory):
    print(f'creating directory: {docs_rst_files_directory}')
    os.makedirs(docs_rst_files_directory)
else:
    print(f'removing directory: {docs_rst_files_directory}')
    rmtree(docs_rst_files_directory)
    print(f'creating directory: {docs_rst_files_directory}')
    os.makedirs(docs_rst_files_directory)

for rst_file in os.listdir(docs_rst_files_directory):
    print(f'Removing file: {os.path.join(docs_rst_files_directory, rst_file)}')
    os.remove(os.path.join(docs_rst_files_directory, rst_file))

# Generated the new files
print('Generating new rst files')
index_rst_toc = '   :caption: Table of Contents:\n'
toc_base = 'docs/keywords.'
base_directory = os.path.join(source_file_path,'..','..','keywords')
toc_file = os.path.join(source_file_path, 'source','index.rst')

create_rst_for_directory(base_directory, docs_rst_files_directory)


# Generate the html
print('Generating HTML')
os.chdir(source_file_path)
os.system("make html")
print('Completed')

# Debugging the page
# import webbrowser
# new = 2 # open in a new tab, if possible
# url = f"file:{source_file_path}/build/index.html"
# webbrowser.open(url,new=new)