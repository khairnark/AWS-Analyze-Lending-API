# AWS-Analyze-Lending-API
**Lending API Documentation**

---

Welcome to the Analyze Lending API documentation! With this API, you can analyze both single PDF files and multiple PDF files effortlessly.

**Why Analyze Lending?**

Mortgage companies frequently encounter the need to process a large variety of document types to extract vital business data. However, the conventional manual approach to data extraction from documents is slow, expensive, and prone to errors. Enter Analyze Lending by Amazon Textract - a solution designed to streamline this process, enhancing efficiency and accuracy while reducing costs associated with loan processing. Additionally, it offers scalability to adapt swiftly to fluctuating demands.

**How It Works**

When you submit a document to the Analyze Lending workflow, it undergoes a series of steps. Firstly, the document is segmented into individual pages, and each page is classified accordingly. Subsequently, the pages are routed to the appropriate Amazon Textract operation based on their classification. Amazon Textract meticulously analyzes the content and extracts pertinent information such as signatures, identity details, forms, expenses, and query data.

**Response Structure**

Regardless of the document class, the results of the analysis for individual pages adhere to a standardized format. Upon querying the GetLendingAnalysis operation, you'll receive details about the page number, classification, and the extracted information derived from Amazon Textract's analysis operations.

For detailed implementation guidance, refer to the [API Documentation](#) and [Examples](#).
