import ast
import os
import traceback
import argparse
# In the Future we may need to do something with this
# from docstring_parser import parse


class parseXAPI:
    """
        This class will take the XAPI SDK and parse the API files and create the base classes for the framework
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Generation script to take the XAPI SDK and generated the base class files for the AutoIQ framework')
        self.parser.add_argument('-x',
                                 '--xapi_sdk_directory',
                                 help='The api directory for the XAPI SDK (ExtremeCloudIQ-SDK-Python/extremecloudiq/api/)',
                                 required=True
                                 )
        self.args = self.parser.parse_args()
        self.base_generated_directory = os.path.join(os.getcwd(), 'keywords', 'xapi_base')
        self.directory = self.args.xapi_sdk_directory
        self.python_types = ['int', 'string', 'bool']
        self.tab = '    '
        self.based_comment_break = '=========================================\n'
        self.base_common_file_generation = '\n#' + self.tab + self.based_comment_break + \
                                           '#'+ self.tab +'WARNING: This file is generated code by the file: /tools/xapi/GenerateXApiBaseKeywords.py\n' \
                                           '#'+ self.tab +'DO NOT EDIT THIS FILE\n#'+ self.tab + self.based_comment_break + '\n\n'

        # The template dict will allow different templates to be used for different function, class combinations
        # enter in the key as <function><class> and the value is the template name to be used.
        self.templateDict = dict()
        self.templateDict['loginAuthenticationApi'] = os.path.join(os.getcwd(), 'tools', 'xapi', 'base_login_function_template.txt')

    def process_info(self, functionNode, xapi_class_name):
        """
            Process the AST function and gather the data to write the framework functions
        :param functionNode: the function ast object
        :param xapi_class_name: the class name
        :return: File contents for the new function
        """
        print("Function name:", functionNode.name)
        if functionNode.name != '__init__' and 'with_http_info' not in functionNode.name:
            doc_string = ast.get_docstring(functionNode)

            # Add in the Robot / Pytest Examples
            self.doc_base_generated_directory = self.base_generated_directory.replace(os.getcwd(), '')[1:]
            general_comment = "**Note - The kwargs options are explained in the :param section below.\n" \
                              "These can be placed in the kwargs dict as key / values pairs or \n" \
                              "passed into the function as key / value pairs as separate arguments.\n\n"
            robot_import = f'{self.tab}Library    ' + self.doc_base_generated_directory + f'/XapiBase{xapi_class_name}.py\n\n'
            robot_example = f'Robot ->\n\n{robot_import}{self.tab}{functionNode.name.replace("_"," ")}{self.tab}**kwargs\n'
            pytest_import = f'{self.tab}from ' + self.doc_base_generated_directory.replace('/',".") + f'.XapiBase{xapi_class_name} import XapiBase{xapi_class_name}\n\n'
            pytest_class = f'{self.tab}xapiBase{xapi_class_name} = XapiBase{xapi_class_name}()\n'
            pytest_example = f'\nPytest ->\n\n{pytest_import}{pytest_class}{self.tab}xapiBase{xapi_class_name}.{functionNode.name}(**kwargs)\n\n'

            # Add the examples before the 1st :param or :return
            param_search = doc_string.index(':param')
            if param_search:
                doc_string = doc_string[:param_search] + general_comment + robot_example + pytest_example + doc_string[param_search:]
            else:
                return_search = doc_string.index(':return')
                if return_search:
                    doc_string = doc_string[:return_search] + general_comment + robot_example + pytest_example + doc_string[return_search:]
                else:
                    doc_string = doc_string + general_comment + robot_example + pytest_example

            doc_string_lines = doc_string.splitlines()
            doc_string_new = ''
            for line in doc_string_lines:
                doc_string_new = doc_string_new + self.tab + self.tab + self.tab + line + '\n'
            doc_string = '"""\n' + doc_string_new + '\n' + self.tab + self.tab + self.tab + self.tab + self.tab + '-1 if there is a error (fault)\n'+ self.tab + self.tab + '"""\n'

            # Read in the function definition template
            file_name = os.path.join(os.getcwd(), 'tools', 'xapi', 'base_generated_function_template.txt')
            custom_file_name = self.templateDict.get(functionNode.name + xapi_class_name, None)
            if custom_file_name:
                file_name = custom_file_name
            with open(file_name) as file:
                file_contents = file.read()
                file_contents = file_contents.replace('{FUNCTION_NAME}', 'xapi_base_' + functionNode.name)
                file_contents = file_contents.replace('{COMMENT_HEADER}', doc_string )
                file_contents = file_contents.replace('{XAPI_API_CLASS}', xapi_class_name)
                file_contents = file_contents.replace('{XAPI_API_FUNCTION}', functionNode.name)
            return file_contents

            # In the Future we may need to do something with this
            # parsed_doc_string = parse(doc_string)
            # print("Args:")
            # for param in parsed_doc_string.params:
            #     name = param.args[1]
            #     # Bug in the doc string to get the parameters
            #     if name in self.python_types and len(param.args) > 2:
            #         name = param.args[2]
            #     print(f"{self.tab}Parameter name:", name)


    def parseFiles(self):
        """"
            Based on the directory passed into the class we can generate the new files based on parsing the XAPI SDK api files
        """
        self.directory = self.directory.strip()
        for filename in os.listdir(self.directory):
            file_and_directory = os.path.join(self.directory, filename)
            # checking if it is a file
            if os.path.isfile(file_and_directory):
                with open(file_and_directory) as file:
                    file_contents = file.read()
                    node = ast.parse(file_contents)
                classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
                for class_ in classes:
                    print("Class name:", class_.name)
                    new_class_file = self.base_generated_directory + "/XapiBase" + class_.name + ".py"
                    if os.path.exists(new_class_file):
                        os.remove(new_class_file)
                    class_file = open(new_class_file, "a")
                    class_file.write(self.base_common_file_generation)
                    class_file.write('\nfrom tools.xapi.XapiHelper import XapiHelper\n\n\nclass XapiBase' + class_.name +'(XapiHelper):\n\n'+ self.tab + 'def __init__(self):\n' + self.tab + self.tab + 'super().__init__()\n\n')
                    methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
                    for method in methods:
                        function_contents = self.process_info(method, class_.name)
                        if function_contents:
                            class_file.write(function_contents + "\n\n")
                    class_file.close()


    def checkForErrors(self):
        """
            This function will compile the generated code to ensure that it is correctly
            formatted.
            :return: None
        """
        for filename in os.listdir(self.base_generated_directory):
            file_and_directory = os.path.join(self.base_generated_directory, filename)
            if file_and_directory.endswith('.py') and file_and_directory != '__init__.py':
                print(f'Open and compile file: {file_and_directory}')
                with open(file_and_directory) as f:
                    source = f.read()
                    try:
                        ast.parse(source)
                    except SyntaxError:
                        traceback.print_exc()
        # Flake 8 check
        return_code = os.system(f'flake8 --color=always --statistics {self.base_generated_directory}')
        if return_code != 0:
            raise Exception('Flake8 has failed!')


if __name__ == "__main__":
    parser = parseXAPI()
    parser.parseFiles()
    parser.checkForErrors()