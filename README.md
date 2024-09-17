# KEGGAPItest

chatbot_test.ipynb - This the framework for the KEGG retriever. It uses GPT to look at a question using entity recognition, use the entities to generate a RESTful API endpoint into KEGG, retrieve the KEGG entry, and response with an answer using the question and retrieved entry. It will eventually be tested with the questions from QA_test.ipynb. 

QA_test.ipynb - If you have the API key for GPT, you can use this to generate questions and answers to related to PMIDs of entries on KEGG. This specifically looks at KEGG pathway entires, but
you can just change "pathways", or add to "pathways" if you want to generate QA for other entry types.
