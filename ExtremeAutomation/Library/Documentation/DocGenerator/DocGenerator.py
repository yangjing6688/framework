import os
import platform
import MySQLdb
from os import walk, path
from ExtremeAutomation.Library.Utils.FileUtils import FileUtils
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Documentation.KeywordStatisticObj import KeywordStatisticObj
import json
import time
import re


class DocGenerator:

    host = 'extreme-networks-robot-rds.ce1yriuqod5n.us-east-1.rds.amazonaws.com'
    user = 'extreme_root'
    password = 'extreme_root'
    db = 'robot'

    def __init__(self):
        self.logger = Logger()
        self.logger.console_level = self.logger.ALL

        self.dir_prefix = os.path.expanduser("~")
        self.doc_keyword_path = os.pathsep + 'ExtremeAutomation' + os.pathsep + 'Keywords'
        self.test_kw_count_path = self.dir_prefix + os.pathsep + 'ExtremeAutomation' + os.pathsep + 'Tests'
        self.doc_keywords_destination_path = self.dir_prefix + os.pathsep + 'ExtremeAutomation' + \
            os.pathsep + 'Documentation' + os.pathsep + 'GeneratedDocs'
        self.low_level_keyword_path = os.pathsep + 'ExtremeAutomation' + os.pathsep + 'Keywords' + \
            os.pathsep + 'NetworkElementKeywords'
        self.low_level_keywords_destination_path = self.dir_prefix + os.pathsep + 'ExtremeAutomation' + \
            os.pathsep + 'Documentation' + os.pathsep + 'GeneratedDocs' + os.pathsep + 'LowLevelKeywords'
        self.user_defined_keyword_path = os.pathsep + 'ExtremeAutomation' + os.pathsep + 'Keywords' + \
            os.pathsep + 'UserDefinedKeywords'
        self.user_defined_keywords_destination_path = self.dir_prefix + os.pathsep + 'ExtremeAutomation' + \
            os.pathsep + 'Documentation' + os.pathsep + 'GeneratedDocs' + os.pathsep + \
            'UserDefinedKeywords'
        self.test_case_path = os.pathsep + 'ExtremeAutomation' + os.pathsep + 'Tests' + os.pathsep + \
            'Functional' + os.pathsep + 'NetworkElements'
        self.test_case_destination_path = self.dir_prefix + os.pathsep + 'ExtremeAutomation' + os.pathsep + \
            'Documentation' + os.pathsep + 'GeneratedDocs' + os.pathsep + 'TestCases'
        self.network_management_keyword_path = os.pathsep + 'ExtremeAutomation' + os.pathsep + 'Library' + \
            os.pathsep + 'NetworkManagement'
        self.network_management_keywords_destination_path = self.dir_prefix + os.pathsep + 'ExtremeAutomation' + \
            os.pathsep + 'Documentation' + os.pathsep + 'GeneratedDocs' + os.pathsep + \
            'NetworkManagement'
        self.upload_path = self.dir_prefix + os.pathsep + 'ExtremeAutomation' + os.pathsep + \
            'Documentation' + os.pathsep + 'GeneratedDocs'
        self.root_dir = ''
        if platform.system() == 'Windows':
            self.root_dir = 'C:\\TRM_DATA\\html_docs\\'
        else:
            self.root_dir = '/TRM_DATA/html_docs/'
        self.connection = None
        self.connect_to_database()

    def connect_to_database(self):
        """
        Connects to the AmazonWS cloud server's SQL database.
        """
        self.logger.log_info('Connecting to database...')
        try:
            self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
            self.logger.log_info('Connected.')
        except (MySQLdb.Error, MySQLdb.Warning) as err:
            self.logger.log_info("Something went wrong: {}".format(err))

    def get_doc_root(self):
        """
        Returns the Documentation root directory.
        """
        return self.upload_path

    def upload_docs(self):
        """
        Uploads the current version of the documentation
        """
        os.system('python -m rfdoc.upload ' + self.upload_path)

    @staticmethod
    def make_name_unique(gen_path):
        """
        Generates a unique name for the docs
        """
        spath = path.split('GeneratedDocs')[1]
        file_type = 'LowLevel'
        if 'UserDefined' in spath:
            file_type = 'UserDefined'
        if file_type == 'LowLevel':
            feature = path.split('LowLevelKeywords')[1].split(os.pathsep)[1]
        else:
            feature = path.split('UserDefinedKeywords')[1].split(os.pathsep)[1]
        gen_path = gen_path.replace('Utils', feature + 'Utils').replace('Common', feature + 'Common')
        spath = spath.split(os.pathsep)
        for file_item in spath:
            if file_item != '' and type not in file_item:
                gen_path = gen_path.replace(file_item, file_type + file_item)
        gen_path = gen_path.replace('LowLevelUtils', 'Utils').replace('UsedDefinedUtils', 'Utils').\
            replace('LowLevelCommon', 'Common').replace('UsedDefinedCommon', 'Common').\
            replace('UtilsUtils', file_type + 'Utils').replace('CommonCommon', file_type + 'Common')
        return gen_path

    def generate_llkw_docs(self):
        """
        Keyword Arguments:
        None.

        This will generate all of the documentation for the following categories:
           - Low level keywords
           - Test cases
        """
        file_list = []
        kw_filename = ""
        for dirpath, dirnames, filenames in os.walk(self.doc_keyword_path):
            for filename in [f for f in filenames if f.endswith('.py') and '__init__' not in f]:
                file_list.append(dirpath + os.pathsep + filename)
        for filename in file_list:
            try:
                fn = filename.split(os.pathsep)[-1]
                kw_path = "\\" + filename.replace(fn, '').split('\\Keywords\\')[1]
                kw_path = self.low_level_keywords_destination_path + kw_path
                kw_path = self.make_name_unique(kw_path)
                if not os.path.exists(kw_path):
                    os.makedirs(kw_path)
                    init = open(kw_path + os.pathsep + '__init__.py', 'a')
                    init.close()
                kw_filename = fn.replace('.py', '.xml')
                result = os.system('python -m robot.libdoc ' + filename + ' ' + kw_path + os.pathsep +
                                   'llkw' + kw_filename)
                self.logger.log_debug(result)
            except SystemError:
                self.logger.log_info('Error encountered processing: ' + filename + ' ' +
                                     self.low_level_keywords_destination_path + os.pathsep + kw_filename)
        self.logger.log_info('done')

    def generate_udkw_docs(self):
        """
        Keyword Arguments:
        None.

        This will generate all of the documentation for the following categories:
           - Low level keywords
           - Test cases
        """
        file_list = []
        kw_filename = ""
        for dirpath, dirnames, filenames in os.walk(self.dir_prefix + self.user_defined_keyword_path):
            for filename in [f for f in filenames if f.endswith('.robot') and '__init__' not in f]:
                file_list.append(dirpath + os.pathsep + filename)
        for filename in file_list:
            try:
                fn = filename.split(os.pathsep)[-1]
                kw_path = "\\" + filename.replace(fn, '').split('\\UserDefinedKeywords\\')[1]
                kw_path = self.user_defined_keywords_destination_path + kw_path
                kw_path = self.make_name_unique(kw_path)
                if not os.path.exists(kw_path):
                    os.makedirs(kw_path)
                    init = open(kw_path + os.pathsep + '__init__.py', 'a')
                    init.close()
                kw_filename = fn.replace('.robot', '.xml')
                result = os.system('python -m robot.libdoc ' + filename + ' ' + kw_path + os.pathsep + 'udkw' +
                                   kw_filename)
                self.logger.log_debug(result)
            except SystemError:
                self.logger.log_info('Error encountered processing: ' + filename + ' ' +
                                     self.low_level_keywords_destination_path + os.pathsep + kw_filename)
        self.logger.log_info('done')

    def generate_docs(self):
        """
        Keyword Arguments:
        None.

        This will generate all of the documentation for the following categories:
           - Low level keywords
           - User defined keywords
           - Test cases
        """
        self.test_case_path = self.dir_prefix + self.test_case_path
        self.doc_keyword_path = self.dir_prefix + self.doc_keyword_path
        self.generate_llkw_docs()
        self.generate_udkw_docs()
        self.generate_test_case_docs()
        self.logger.log_info('Doc Generation Completed')

    def generate_test_case_docs(self):
        """
        Keyword Arguments:
        None.

        This will generate all of the documentation for the Test cases
        """
        file_list = []
        kw_filename = ""
        for dirpath, dirnames, filenames in os.walk(self.test_case_path):
            for filename in [f for f in filenames if f.endswith('.robot') and '__init__' not in f]:
                file_list.append(dirpath + os.pathsep + filename)
        for filename in file_list:
            try:
                fn = filename.split(os.pathsep)[-1]
                kw_filepath = self.test_case_destination_path + filename.split('Functional')[1]
                kw_path = kw_filepath.replace(fn, '')
                if not os.path.exists(kw_path):
                    os.makedirs(kw_path)
                    init = open(kw_path + os.pathsep + '__init__.py', 'a')
                    init.close()
                kw_filename = kw_filepath.replace('.robot', '.html')
                result = os.system('python -m robot.testdoc -T ' + kw_filename.replace('.robot', '') + ' ' +
                                   filename + ' ' + kw_filename)
                self.logger.log_debug(result)
            except SystemError:
                self.logger.log_info('Error encountered processing: ' + filename + ' ' +
                                     self.test_case_destination_path + os.pathsep + kw_filename)
        self.logger.log_info('done')

    def generate_user_defined_keyword_docs(self):
        """
        Keyword Arguments:
        None.

        This will generate all of the documentation for the User defined keywords
        """
        file_list = []
        kw_path = ""
        kw_filename = ""
        for dirpath, dirnames, filenames in os.walk(self.user_defined_keyword_path):
            for filename in [f for f in filenames if f.endswith('.robot') and '__init__' not in f]:
                file_list.append(dirpath + os.pathsep + filename)
        for filename in file_list:
            try:
                fn = filename.split(os.pathsep)[-1]
                kw_path = filename.replace(fn, '').split('UserDefinedKeywords')[1]
                kw_path = self.user_defined_keywords_destination_path + kw_path
                if not os.path.exists(kw_path):
                    os.makedirs(kw_path)
                    init = open(kw_path + os.pathsep + '__init__.py', 'a')
                    init.close()
                kw_filename = fn.replace('.robot', '.xml')
                result = os.system('python -m robot.libdoc ' + filename + ' ' + kw_path + os.pathsep + kw_filename)
                self.logger.log_debug(result)
            except SystemError:
                self.logger.log_info('Error encountered processing: ' + filename + ' ' + kw_path + os.pathsep +
                                     kw_filename)
        self.logger.log_info('done')

    def generate_low_level_keyword_docs(self):
        """
        Keyword Arguments:
        None.

        This will generate all of the documentation for the Low level keywords (NetworkElementKeywords)
        """
        file_list = []
        kw_filename = ""
        for dirpath, dirnames, filenames in os.walk(self.low_level_keyword_path):
            for filename in [f for f in filenames if f.endswith('.py') and '__init__' not in f]:
                file_list.append(dirpath + os.pathsep + filename)
        for filename in file_list:
            try:
                fn = filename.split(os.pathsep)[-1]
                kw_path = filename.replace(fn, '').split('NetworkElementKeywords')[1]
                kw_path = self.low_level_keywords_destination_path + kw_path
                if not os.path.exists(kw_path):
                    os.makedirs(kw_path)
                    init = open(kw_path + os.pathsep + '__init__.py', 'a')
                    init.close()
                kw_filename = fn.replace('.py', '.xml')
                result = os.system('python -m robot.libdoc ' + filename + ' ' + kw_path + os.pathsep + kw_filename)
                self.logger.log_debug(result)
            except SystemError:
                self.logger.log_info('Error encountered processing: ' + filename + ' ' +
                                     self.low_level_keywords_destination_path + os.pathsep + kw_filename)
        self.logger.log_info('done')

    def generate_network_management_keyword_docs(self):
        """
        Keyword Arguments:
        None.

        This will generate all of the documentation for the User defined keywords
        """
        file_list = []
        kw_path = ""
        kw_filename = ""
        for dirpath, dirnames, filenames in os.walk(self.network_management_keyword_path):
            for filename in [f for f in filenames if f.endswith('.py') and '__init__' not in f]:
                file_list.append(dirpath + os.pathsep + filename)
        for filename in file_list:
            try:
                fn = filename.split(os.pathsep)[-1]
                kw_path = filename.replace(fn, '').split('NetworkManagement')[1]
                kw_path = self.network_management_keywords_destination_path + kw_path
                if not os.path.exists(kw_path):
                    os.makedirs(kw_path)
                    init = open(kw_path + os.pathsep + '__init__.py', 'a')
                    init.close()
                kw_filename = fn.replace('.py', '.xml')
                result = os.system('python -m robot.libdoc ' + filename + ' ' + kw_path + os.pathsep + kw_filename)
                self.logger.log_debug(result)
            except SystemError:
                self.logger.log_info('Error encountered processing: ' + filename + ' ' + kw_path + os.pathsep +
                                     kw_filename)
        self.logger.log_info('done')

    def convert_to_html_and_commit_to_db(self, filepath):
        """
        This method will convert the XML files generated by libdoc into html pages,
        and then store those pages (along with their respective paths) into the database.
        Currently the html files are written to TRM_DATA/html_docs

        Args:
            filepath:            The path to the root dir containing the generated XML files.
                                 Currently ExtremeAutomation/Documentation/GeneratedDocs
        """
        self.delete_existing_html_doc_rows()
        file_list = []
        filename = ""
        for dirpath, dirnames, filenames in os.walk(filepath):
            for filename in [f for f in filenames if f.endswith('.xml') and '__init__' not in f]:
                file_list.append(dirpath + os.pathsep + filename)
        for file_item in file_list:
            split_filename = file_item.split('\\')
            file_name = split_filename[len(split_filename) - 1]
            dest_dir = file_item.replace(file_name, '').split("GeneratedDocs\\")[1]
            if not os.path.exists(self.root_dir + dest_dir):
                os.makedirs(self.root_dir + dest_dir)
            os.system('python -m robot.libdoc -f html ' + file_item + ' ' + self.root_dir + dest_dir +
                      file_name.replace('.xml', '.html'))
            page = FileUtils.read_file_to_str(self.root_dir + dest_dir + file_name.replace('.xml', '.html'))
            self.insert_htmldoc_into_database(self.root_dir + dest_dir, filename, page)

    def insert_libraries_into_database(self, filepath):
        """
        This method will store generated keyword library html pages (along with their respective paths) into the
        database.

        Args:
            filepath:            The path to the root dir containing the generated XML files.
                                 Currently ExtremeAutomation/Documentation/GeneratedDocs
        """
        self.delete_existing_html_doc_rows()
        file_list = []
        for dirpath, dirnames, filenames in os.walk(filepath):
            for filename in [f for f in filenames if f.endswith('.html') and '__init__' not in f]:
                file_list.append(dirpath + os.pathsep + filename)
        key = 0
        for file_item in file_list:
            split_filename = file_item.split('\\')
            file_name = split_filename[len(split_filename) - 1]
            dest_dir = file_item.replace(file_name, '').split("GeneratedDocs\\")[1]
            if not os.path.exists(self.root_dir + dest_dir):
                os.makedirs(self.root_dir + dest_dir)
            self.insert_htmldoc_into_database(self.root_dir + dest_dir, file_name.replace('.xml', '.html'), str(key))

    def delete_existing_html_doc_rows(self):
        """
        This method deletes all existing entries in the robot.html_docs table, in preparation to insert the
        latest copies after a new set of docs have been generated
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute('''DELETE FROM html_docs''')
            self.connection.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as err:
            self.logger.log_info("Something went wrong: {}".format(err))
            self.logger.log_info('Failure!')
            self.connection.rollback()

    def delete_existing_keyword_statistics_rows(self):
        """
        This method deletes all existing entries in the robot.keyword_statistics table, in preparation to insert the
        latest copies after a new set of stats have been generated
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute('''DELETE FROM keyword_statistics''')
            self.connection.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as err:
            self.logger.log_info("Something went wrong: {}".format(err))
            self.logger.log_info('Failure!')
            self.connection.rollback()

    @staticmethod
    def clean_filepath(file_path):
        """
        This method will convert the html doc path from (for example) TRM_DATA/html_docs/NetworkElement or
        TRM_DATA/html_docs/NetworkElement into TRM_DATA.html_docs.NetworkElement

        This platform neutral path is not meant to be used as an actual filepath, it is stored in the database
        along with the accompanying keyword library html page for use in determining what the doc webpage's
        keyword tree should look like

        Args:
            file_path:            The path to the html doc being processed
        """
        file_path = file_path.replace('\\', '.').replace('/', '.').replace('C:.TRM_DATA.html_docs', 'ROOT')
        file_path = file_path[0:-1]
        return file_path

    def insert_htmldoc_into_database(self, file_path, doc, file_key):
        """
        This method inserts html keyword libraries into the database, along with their respective paths

        Args:
            file_path:          The path to the html doc (generated using the clean_filepath method
            file_key:           The key
            doc:                The html doc itself
        """
        file_type = 'llkw'
        if 'UserDefined' in file_path:
            file_type = 'udkw'
        file_path = self.clean_filepath(file_path)
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO html_docs(path, html, html_key, kw_type) VALUES (%s,%s,%s,%s)"
            args = (file_path, doc, file_key, file_type)
            cursor.execute(query, args)
            self.connection.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as err:
            self.logger.log_info("Something went wrong: {}".format(err))
            self.logger.log_info('Failed to insert entry into database!')
            self.connection.rollback()

    def insert_keyword_statistics_into_database(self):
        """
        This method generates a list of the keyword methods in each library, and inserts that list into the database for
        use in the keyword statistics code
        """
        kwjson = self.get_kw_list()
        kw_counts = self.tally_keyword_counts(kwjson)
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO html_docs(path, html, html_key, kw_type) VALUES (%s,%s,%s,%s)"
            args = (self.root_dir, json.dumps(kw_counts), 'kwmethodlist')
            cursor.execute(query, args)
            self.connection.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as err:
            self.logger.log_info("Something went wrong: {}".format(err))
            self.logger.log_info('Failed to insert entry into database!')
            self.connection.rollback()

    def get_kw_list(self):
        """
        This method generates a list of the keyword methods in each library
        """
        kw_json = {}
        file_list = []
        lib_name = ''
        for dirpath, dirnames, filenames in os.walk(self.doc_keywords_destination_path):
            for filename in [f for f in filenames if f.endswith('.xml') and '__init__' not in f]:
                file_list.append(dirpath + os.pathsep + filename)
        for file_item in file_list:
            method_list = []
            file_type = 'llkw'
            if 'UserDefined' in file_item:
                file_type = 'udkw'
            with open(file_item) as current_lib:
                kw_content = current_lib.readlines()
                for line in kw_content:
                    if 'kw name=' in line:
                        pathlist = file_item.split(os.pathsep)
                        lib_name = pathlist[len(pathlist) - 1].replace('.xml', '')
                        method_name = line.split('=')[1].replace('>\n', '').replace('"', '').replace('\'', '')
                        method_list.append(method_name)
            if len(method_list) >= 1:
                method_list.append(file_type)
                kw_json[lib_name] = method_list
        return kw_json

    def tally_keyword_counts(self, kw_json):
        """
        This method scans through all the test cases and determines the keyword usage count for every
        keyword in every library

        Args:
            kw_json:               The keyword dictionary (generated by get_kw_list())
        """
        keyword_object_list = []
        start_time = int(round(time.time() * 1000))
        file_list = []
        for dirpath, dirnames, filenames in os.walk(self.test_kw_count_path):
            for filename in [f for f in filenames if f.endswith('.robot') and '__init__' not in f]:
                file_list.append(dirpath + os.pathsep + filename)
        for lib in kw_json.keys():
            count_list = []
            kw_list = kw_json[lib]
            file_type = kw_list.pop(-1)
            for kw in kw_list:
                # Gather the usage count for each kw lib method
                usage_count = 0
                usage_list = []
                keyword_obj = KeywordStatisticObj()
                for file_item in file_list:
                    try:
                        with open(file_item, 'r') as current_test:
                            test_content = current_test.read()
                            count = len(re.findall('(?=' + kw + ')', test_content))
                            usage_count = usage_count + count
                            if count > 0:
                                usage_list.append(file_item)
                    except OSError as e:
                        self.logger.log_info("Exception: {}".format(e))
                        self.logger.log_info('Hit exception opening file ' + file_item + ', continuing...')
                count_list.append(kw + '[' + str(usage_count) + ']')
                keyword_obj.keyword_name = kw
                keyword_obj.keyword_parent = lib
                keyword_obj.keyword_count = usage_count
                keyword_obj.keyword_type = file_type
                for entry in usage_list:
                    entry = entry.split(os.pathsep)[len(entry.split(os.pathsep)) - 1]
                    keyword_obj.keyword_test_cases = entry
                keyword_object_list.append(keyword_obj)
        end_time = int(round(time.time() * 1000))
        self.insert_keyword_statistics_into_database_with_args(keyword_object_list)
        duration = self.convert_time(end_time - start_time)
        self.logger.log_info("Total usage search took: " + duration)

        return len(keyword_object_list)

    def insert_keyword_statistics_into_database_with_args(self, keyword_objects):
        """
        This method inserts html keyword statistic entries into the database, along with their respective parent
        libraries, usage count, and test case instances

        Args:
            keyword_objects:   The objects to insert
        """
        self.delete_existing_keyword_statistics_rows()
        cursor = self.connection.cursor()
        try:
            for obj in keyword_objects:
                query = "INSERT INTO keyword_statistics(keyword_name, parent_library, " \
                        "current_instances, instance_locations, kw_type) VALUES (%s,%s,%s,%s,%s)"
                keyword_name = obj.keyword_name
                parent_library = obj.keyword_parent
                current_instances = obj.keyword_count
                instance_locations = obj.keyword_Test_cases
                kw_type = obj.keyword_type
                args = (keyword_name, parent_library, current_instances, instance_locations, kw_type)
                cursor.execute(query, args)
                self.connection.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as err:
            self.logger.log_info("Something went wrong: {}".format(err))
            self.logger.log_info('Failed to insert entry into database!')
            self.connection.rollback()

    def insert_tree_into_database(self):
        """
        This method inserts html keyword libraries into the database, along with their respective paths

        Args:
        """
        jsontree = self.tree_to_json(self.root_dir)
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO html_docs(path, html, html_key) VALUES (%s,%s,%s)"
            args = (self.root_dir, jsontree, 'jsontree')
            cursor.execute(query, args)
            self.connection.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as err:
            self.logger.log_info("Something went wrong: {}".format(err))
            self.logger.log_info('Failed to insert entry into database!')
            self.connection.rollback()

    @staticmethod
    def file_to_dict(fpath):
        """
        Returns a dictionary of the file and path information.
        """
        return {'name': path.basename(fpath),
                'type': 'file',
                'path': fpath,
                'tag': 'org'}

    @staticmethod
    def folder_to_dict(rootpath):
        """
        Returns a dictionary of the folder and path information.
        """
        return {'name': path.basename(rootpath),
                'type': 'folder',
                'path': rootpath,
                'tag': 'org',
                'children': []}

    def tree_to_dict(self, rootpath):
        """
        Returns a dictionary of the files/folders in the given path.
        """
        root_dict = self.folder_to_dict(rootpath)
        root, folders, files = walk(rootpath).next()
        root_dict['children'] = [self.file_to_dict(path.sep.join([root, fpath])) for fpath in files]
        root_dict['children'] += [self.tree_to_dict(path.sep.join([root, folder])) for folder in folders]
        return root_dict

    def tree_to_json(self, rootdir, pretty_print=False):
        """
        Returns a JASON dict of the files/folders in the given path.
        [pretty_print] - Toggles formatting the JSON for log output
        """
        root, folders, files = walk(rootdir).next()
        root_dict = [self.tree_to_dict(path.sep.join([root, folder])) for folder in folders]
        root_dict += [self.file_to_dict(path.sep.join([root, fpath])) for fpath in files]
        if pretty_print:
            js = json.dumps(root_dict, indent=4, encoding='utf-8')
        else:
            js = json.dumps(root_dict, encoding='utf-8')
        return js

    def get_doc_tree(self):
        """
        Logs the current doc tree.
        """
        tree = []
        for root, directories, filenames in os.walk(self.doc_keywords_destination_path):
            for directory in directories:
                if 'TestCases' not in directory:
                    tree.extend(directory)
                    self.logger.log_info(os.path.join(root, directory))
            for filename in filenames:
                self.logger.log_info(os.path.join(root, filename))

    @staticmethod
    def convert_time(ms):
        """
        Returns the given milliseconds in hours, minutes, seconds.
        """
        ms = int(ms)
        seconds = (ms // 1000) % 60
        seconds = int(seconds)
        minutes = (ms // (1000 * 60)) % 60
        minutes = int(minutes)
        hours = (ms // (1000 * 60 * 60)) % 24
        return "%d hours %d minutes %d seconds" % (hours, minutes, seconds)
