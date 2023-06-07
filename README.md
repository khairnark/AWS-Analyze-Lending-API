# AWS-Analyze-Lending-API
Analyze Lending API for single pdf file and Multiple pdf file
Mortgage companies often need to process large volumes of diverse document types to extract business-critical data. Today, lenders are faced with the challenge of managing a manual, slow, and expensive process to extract data and insights from documents. To help address the issue, Amazon Textract Analyze Lending improves business process efficiency through automation and accuracy, reducing loan processing costs and providing the ability to scale quickly based on changing demand.
When you submit a document to the Analyze Lending workflow, the document is split apart into individual pages and the pages are classified. The individual pages are then sent to the appropriate Amazon Textract operation for further analysis, depending on their classification. Amazon Textract analyzes the data and returns the relevant information extracted from the documents, such as detected signatures, identity information, forms, expense values, and queries data.
The results for the analysis of individual pages follow one general structure, regardless of the class of the document. The response from GetLendingAnalysis contains information regarding the page number and page classification, along with the information extracted by one of Amazon Textract ’s analysis operations.
