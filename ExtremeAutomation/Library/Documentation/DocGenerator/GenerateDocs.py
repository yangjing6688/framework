import DocGenerator

print('Generating documentation...')
dg = DocGenerator.DocGenerator()
dg.generate_docs()
dg.convert_to_html_and_commit_to_db(dg.get_doc_root())
dg.tally_keyword_counts(dg.get_kw_list())
print('Done')
