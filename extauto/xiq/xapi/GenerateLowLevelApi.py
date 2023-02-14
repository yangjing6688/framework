import ast
import os
import traceback
from docstring_parser import parse


class parseXAPI:
    """
        This class will take the XAPI SDK and parse the API files and create the base classes for the framework
    """

    def __init__(self, directory):
        self.directory = directory
        self.python_types = ['int', 'string', 'bool']
        self.output_file_directory = 'base'
        self.tab = '    '

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
            robot_import = f'{self.tab}{self.tab}Library     extauto/xiq/xapi/base/XapiBase{xapi_class_name}.py\n\n'
            robot_example = f'{self.tab}Robot:\n{robot_import}{self.tab}{self.tab}{functionNode.name.replace("_"," ")}{self.tab}**kwargs\n'
            pytest_import = f'{self.tab}{self.tab}from extauto.xiq.xapi.base.XapiBase{xapi_class_name} import XapiBase{xapi_class_name}\n\n'
            pytest_class = f'{self.tab}{self.tab}xapiBase{xapi_class_name} = XapiBase{xapi_class_name}()\n'
            pytest_example = f'{self.tab}Pytest:\n{pytest_import}{pytest_class}{self.tab}{self.tab}xapiBase{xapi_class_name}.{functionNode.name}(**kwargs)\n\n'

            # Add the examples before the 1st :param or :return
            param_search = doc_string.index(':param')
            if param_search:
                doc_string = doc_string[:param_search] + robot_example + pytest_example + doc_string[param_search:]
            else:
                return_search = doc_string.index(':return')
                if return_search:
                    doc_string = doc_string[:return_search] + robot_example + pytest_example + doc_string[return_search:]
                else:
                    doc_string = doc_string + robot_example + pytest_example

            doc_string = '"""\n' + self.tab + self.tab + doc_string.replace('\n', '\n' + self.tab + self.tab) + '\n'+ self.tab + self.tab + '"""\n'

            # Read in the function definition file
            with open('base_generated_function_definition.txt') as file:
                file_contents = file.read()
                file_contents = file_contents.replace('{FUNCTION_NAME}', 'xapi_base_' + functionNode.name)
                file_contents = file_contents.replace('{COMMMENT_HEADER}', doc_string )
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
            #     print("\tParameter name:", name)


    def parseFiles(self):
        """"
            Based on the directory passed into the class we can generate the new files based on parsing the XAPI SDK api files
        """
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
                    new_class_file = self.output_file_directory + "/XapiBase" + class_.name + ".py"
                    if os.path.exists(new_class_file):
                        os.remove(new_class_file)
                    class_file = open(new_class_file, "a")
                    class_file.write('\nfrom extauto.xiq.xapi.XapiBase import XapiBase\n\n\nclass XapiBase' + class_.name +'(XapiBase):\n\n'+ self.tab + 'def __init__(self):\n' + self.tab + self.tab + 'super().__init__()\n\n')
                    methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
                    for method in methods:
                        function_contents = self.process_info(method, class_.name)
                        if function_contents:
                            class_file.write(function_contents + "\n\n")
                    class_file.close()

    def checkForErrors(self):
        for filename in os.listdir(self.output_file_directory):
            file_and_directory = os.path.join(self.output_file_directory, filename)
            if file_and_directory.endswith('.py') and file_and_directory != '__init__.py':
                print(f'Open and comple file: {file_and_directory}')
                with open(file_and_directory) as f:
                    source = f.read()
                    try:
                        ast.parse(source)
                    except SyntaxError:
                        traceback.print_exc()  # Remove to silence any errros

if __name__ == "__main__":
    parser = parseXAPI('/automation/tests/ExtremeCloudIQ-SDK-Python/extremecloudiq/api/')
    parser.parseFiles()
    parser.checkForErrors()
