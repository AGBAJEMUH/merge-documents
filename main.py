import streamlit as st
from pypdf import PdfReader, PdfWriter
import io
import re

# --- Page Configuration ---
st.set_page_config(page_title="PDF Merger Pro", page_icon="📄")

st.title("📄 PDF Document Merger")
st.write("Upload your PDFs in the order you want them merged.")

# --- 1. File Uploader ---
uploaded_files = st.file_uploader(
    "Choose PDF files",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:
    st.subheader("Selected Documents")

    # Track file names for merged PDF
    pdf_names = []

    # Display each file with page count
    for pdf in uploaded_files:
        reader = PdfReader(pdf)
        page_count = len(reader.pages)
        pdf_names.append(pdf.name.replace(".pdf", ""))
        st.info(f"**{pdf.name}** — `{page_count} pages`")

    # --- 2. Merge Button ---
    if st.button("Merge Documents"):
        merger = PdfWriter()

        with st.spinner("Merging your files..."):
            try:
                # Append PDFs
                for pdf in uploaded_files:
                    reader = PdfReader(pdf)
                    merger.append(reader)

                # Save merged PDF to memory
                output_buffer = io.BytesIO()
                merger.write(output_buffer)

                # --- 3. Create Safe Filename ---
                safe_names = [re.sub(r'\W+', '', name) for name in pdf_names]
                unique_name = f"merged_{'_'.join(safe_names)}.pdf"

                st.success("✅ Files merged successfully!")

                # --- 4. Download Button ---
                st.download_button(
                    label="Download Merged PDF",
                    data=output_buffer.getvalue(),
                    file_name=unique_name,
                    mime="application/pdf"
                )

            except Exception as e:
                st.error(f"An error occurred: {e}")

else:
    st.info("Please upload one or more PDF files to begin.")            try:
                # Append PDFs
                for pdf in uploaded_files:
                    reader = PdfReader(pdf)
                    merger.append(reader)
                
                # Save merged PDF to memory
                output_buffer = io.BytesIO()
                merger.write(output_buffer)
                
                # --- 3. Create Safe Filename ---
                safe_names = [re.sub(r'\W+', '', name) for name in pdf_names]
                unique_name = f"merged_{'_'.join(safe_names)}.pdf"
                
                st.success("✅ Files merged successfully!")
                
                # --- 4. Download Button ---
                st.download_button(
                    label="Download Merged PDF",
                    data=output_buffer.getvalue(),
                    file_name=unique_name,
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
else:
    st.info("Please upload one or more PDF files to begin.")                for pdf in uploaded_files:
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
  
