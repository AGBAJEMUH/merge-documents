import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

st.set_page_config(page_title="PDF Merger Pro", page_icon="📄")

st.title("📄 PDF Document Merger")
st.write("Upload your PDFs in the order you want them merged.")

# 1. File Uploader (Accepts multiple files)
uploaded_files = st.file_uploader(
    "Choose PDF files", 
    type="pdf", 
    accept_multiple_files=True
)

if uploaded_files:
    st.subheader("Selected Documents")
    
    # Track files and their names for the final filename
    pdf_names = []
    
    # Display table/list of files with page counts
    for file in uploaded_files:
        reader = PdfReader(file)
        page_count = len(reader.pages)
        pdf_names.append(file.name.replace(".pdf", ""))
        
        st.info(f"**{file.name}** — `{page_count} pages`")

    # 2. Merge Logic
    if st.button("Merge Documents"):
        merger = PdfWriter()
        
        with st.spinner("Merging your files..."):
            try:
                for pdf in uploaded_files:
                    merger.append(pdf)
                
                # Create a buffer to store the PDF in memory
                output_buffer = io.BytesIO()
                merger.write(output_buffer)
                merger.close()
                
                # 3. Create Unique Filename
                # Format: merged_doc1_doc2_doc3.pdf
                unique_name = f"merged_{'_'.join(pdf_names)}.pdf"
                
                st.success("✅ Files merged successfully!")
                
                # 4. Download Button
                st.download_button(
                    label="Download Merged PDF",
                    data=output_buffer.getvalue(),
                    file_name=unique_name,
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
else:
    st.info("Please upload one or more PDF files to begin.")
  
