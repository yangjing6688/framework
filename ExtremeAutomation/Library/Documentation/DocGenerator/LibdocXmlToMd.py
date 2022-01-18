import os
import sys
import shutil
from robot.libdoc import libdoc
from xml.etree import ElementTree
from io import StringIO
from ExtremeAutomation.Library.Logger.Logger import Logger


class LibdocXmlToMd(object):
    """
    This class converts robot keyword libraries into markdown formatted documentation files.
    """

    def __init__(self, inp_folder, out_folder, kw_extension=".py"):
        self.inp_folder = inp_folder
        self.out_folder = out_folder
        self.tmp_xml_file = os.path.join(self.out_folder, "temp.xml")
        self.kw_file_list = []
        self.md_file_list = []
        self.out_folder_list = []
        self.black_list = []
        self.failed_files = []
        self.kw_extension = kw_extension
        self.logger = Logger()

    def create_md_files(self):
        """
        This function creates the needed directories, coverts keyword files to XML,
        coverts the XML to MD, then removes the XML file.
        """
        self._clean_output_folder()
        self._find_keyword_libraries()

        for kw_file, out_folder, md_file in zip(self.kw_file_list, self.out_folder_list, self.md_file_list):
            xml_root = self._generate_xml(kw_file)
            if xml_root is not None:
                parsed_xml = self._parse_xml(xml_root)

                if parsed_xml is not None:
                    self._create_dirs(out_folder)
                    self._generate_md(parsed_xml, md_file)

            self._remove_xml(self.tmp_xml_file)

        if len(self.failed_files) > 0:
            self.logger.log_info("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            self.logger.log_info("Unable to generate MD files for the following libraries...")
            self.logger.log_info("\n".join([i for i in self.failed_files]))
            self.logger.log_info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        self.logger.log_info("DONE!\n")

    def add_file_to_black_list(self, *file_names):
        """
        Adds the given file to the black_list var.
        """
        for file_name in file_names:
            self.black_list.append(file_name.lower())

    def _clean_output_folder(self):
        """
        This function removes all files/folders in the output directory.
        After the files/folders are removed or if they did not exist create the top
        level output folder.
        """
        try:
            shutil.rmtree(self.out_folder)
        except OSError:
            pass
        try:
            os.makedirs(self.out_folder)
        except (OSError, FileExistsError):
            pass

    @staticmethod
    def _create_dirs(output_dirs):
        """
        This function creates all missing directories for a given path.
        """
        try:
            os.makedirs(os.path.join(output_dirs))
        except (OSError, FileExistsError):
            pass

    def _find_keyword_libraries(self):
        """
        This function scans through all files/folders in the input folder.
        If the filename does not start with "__", ends with self.kw_extension,
        and is not in the black list it is added to the list of keyword files.
        Then the folder to place the generated MD file is added, finally
        the full path of the MD file is added.
        """
        for dir_path, dir_names, file_names in os.walk(self.inp_folder):
            for file_name in file_names:
                if not file_name.lower() in self.black_list:
                    if not file_name.lower().startswith("__"):
                        if file_name.lower().endswith(self.kw_extension):
                            self.kw_file_list.append(os.path.join(dir_path, file_name))

                            out_folder = self.out_folder + dir_path.replace(self.inp_folder, "")

                            self.out_folder_list.append(out_folder)
                            self.md_file_list.append(os.path.join(out_folder, file_name.replace(self.kw_extension,
                                                                                                ".md")))

    def _generate_xml(self, source):
        """
        This function uses the libdoc module to generate an XML file from the
        keyword file. We set sys.stdout to devnull to suppress the console output from
        libdoc. We then parse the XML into a python object and return the resulting
        tree's root.
        """
        old_std_out = sys.stdout
        sys.stdout = output = StringIO()
        libdoc(source, self.tmp_xml_file, format="xml")
        sys.stdout = old_std_out
        if "Traceback" in output.getvalue():
            self.logger.log_info(output.getvalue())

        try:
            xml_root = ElementTree.parse(self.tmp_xml_file).getroot()

            self.logger.log_info("Generating temporary XML file from " + source.split(os.sep)[-1] + "...")

            return xml_root
        except IOError:
            self.failed_files.append(source.split(os.sep)[-1])
            return None

    @staticmethod
    def _parse_xml(xml_root):
        """
        This function parses the XML object created by ElementTree.
        It pulls all information from the child nodes that is needed and stores
        it in a dictionary.

        The dictionary format is as follows.

        {"name": <name>,
         "library_scope": <scope>,
         "named_args": <supported|not supported>,
         "description": <description>,
         "kw":
             [
                 {"name": <kw_name>,
                  "args": <kw_args>,
                  "doc_string": <kw_doc_string>
                  }
              ]
         }
        """
        parsed_xml = {"name": xml_root.attrib["name"]}

        for child in xml_root:
            if child.tag == "scope":
                parsed_xml["library_scope"] = child.text
                if parsed_xml["library_scope"] is None:
                    parsed_xml["library_scope"] = "N/A"
            elif child.tag == "namedargs":
                if child.text == "yes":
                    parsed_xml["named_args"] = "Supported"
                else:
                    parsed_xml["named_args"] = "Not Supported"
            elif child.tag == "doc":
                parsed_xml["description"] = child.text.replace("`", "")
            elif child.tag == "kw":
                if "kw" not in parsed_xml:
                    parsed_xml["kw"] = []

                kw_dict = {"name": child.attrib["name"],
                           "args": ", ".join([i.text if not i.text.endswith("=") else i.text + '\"\"'
                                              for i in child[0]
                                              if i.tag == "arg"]),
                           "doc_string": child[1].text if child[1].text is not None else ""
                           }

                parsed_xml["kw"].append(kw_dict)
                for keyword in parsed_xml["kw"]:
                    if "name" in keyword.keys():
                        baseclass_kws = ["Add Agent Kwarg", "Get Keyword Name", "Log Running Keyword",
                                         "Execute Config Keyword", "Execute Verification Keyword", "Format String",
                                         "Execute Keyword"]
                        if keyword["name"] in baseclass_kws:
                            parsed_xml["kw"].remove(keyword)

        if "kw" not in parsed_xml:
            return None

        return parsed_xml

    def _generate_md(self, parsed_xml, dest_file):
        """
        This function generates each section of the MD file then
        creates the MD file.
        """
        self.logger.log_info("Generating MD from " + parsed_xml["name"] + ".xml...")

        md_list = list()

        md_list += self._generate_md_header(parsed_xml)
        md_list += self._generate_md_kw_links(parsed_xml)
        md_list += self._generate_md_table(parsed_xml)
        md_list += self._generate_md_footer()

        with open(dest_file, "w") as md_file:
            md_file.writelines("\n".join(md_list))

    @staticmethod
    def _generate_md_header(parsed_xml):
        """
        This function generates the MD file header. The format is as follows.

        # FileManagementKeywords
        Library Scope: <library_scope><br>
        Named Arguments: <supported | not supported>

        ## Introduction
        <description_string>

        """
        md_header = list()

        md_header.append("# " + parsed_xml["name"])
        md_header.append("Library Scope: " + parsed_xml["library_scope"] + "<br>")
        md_header.append("Named Arguments: " + parsed_xml["named_args"])
        md_header.append("")
        md_header.append("## Introduction")
        md_header.append(parsed_xml["description"])
        md_header.append("")

        return md_header

    @staticmethod
    def _generate_md_kw_links(parsed_xml):
        """
        This function creates the link section of the MD. The format is as follows.

        ## Shortcuts
        [<link_text>](#<anchor>)
        ***

        """
        md_kw_links = list()

        md_kw_links.append("## Shortcuts")
        md_kw_links.append(" | ".join(["[" + i["name"] + "](#" + i["name"].replace(" ", "_") + ")"
                                       for i in parsed_xml["kw"]]))
        md_kw_links.append("***")
        md_kw_links.append("")

        return md_kw_links

    def _generate_md_table(self, parsed_xml):
        """
        This function generates the keyword table. The format is as follows.

        ## Keywords
        | Keyword | Arguments | Documentation |
        |---------|-----------|---------------|
        | <a name="<kw_name_with_underscores>"></a><kw_name> | <kw_args> | <kw_description> |
        """
        md_table = list()

        md_table.append("## Keywords")
        md_table.append("| Keyword | Arguments | Documentation |")
        md_table.append("|---------|-----------|---------------|")

        md_table += [self._generate_table_string(i) for i in parsed_xml["kw"]]

        return md_table

    @staticmethod
    def _generate_md_footer():
        """
        This function creates the MD file footer. The format is as follows.

        Currently the footer only appends a newline, if additional information is
        needed at the bottom of the MD file it can be added here.
        """
        md_footer = list()

        md_footer.append("")

        return md_footer

    @staticmethod
    def _generate_table_string(kw_dict):
        """
        This function generates the table row string. The string format is as follows.
        | <a name="<kw_name_with_underscores>"></a><kw_name> | <kw_args> | <kw_description> |
        """
        table_string = ("| <a name=\"" + kw_dict["name"].replace(" ", "_") + "\"></a>" + kw_dict["name"] + " | " +
                        kw_dict["args"] + " | " + kw_dict["doc_string"] + " |")
        return table_string.replace("\n", "<br>")

    def _remove_xml(self, xml_file):
        """
        This function removes the temporary XML file.
        """
        if os.path.isfile(xml_file):
            self.logger.log_info("Removing temporary XML file...")

            os.remove(xml_file)
