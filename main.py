import streamlit as st
from pypdf import PdfReader, PdfWriter
import io
import re

# --- Page Configuration ---
st.set_page_config(page_title="PDF Merger Pro", page_icon="📄")

st.title("📄 PDF Document Merger")
st.write("Upload your PDFs and drag to reorder before merging.")

# --- 1. File Uploader ---
uploaded_files = st.file_uploader(
    "Choose PDF files",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:
    # --- 2. Display and Reorder PDFs ---
    st.subheader("Selected Documents (Drag to reorder)")

    # Extract names and store UploadedFile objects
    pdf_list = [{"name": file.name, "file": file} for file in uploaded_files]

    # Show reorderable list using Streamlit's experimental container
    reordered_names = st.multiselect(
        "Drag to reorder (top = first page):",
        options=[p["name"] for p in pdf_list],
        default=[p["name"] for p in pdf_list]
    )

    # Map reordered names back to files
    ordered_files = []
    for name in reordered_names:
        for p in pdf_list:
            if p["name"] == name:
                ordered_files.append(p["file"])
                break

    # Display page counts
    for file in ordered_files:
        reader = PdfReader(file)
        page_count = len(reader.pages)
        st.info(f"**{file.name}** — `{page_count} pages`")

    # --- 3. Merge Button ---
    if st.button("Merge Documents"):
        merger = PdfWriter()

        with st.spinner("Merging your files..."):
            try:
                # Append PDFs in custom order
                for pdf in ordered_files:
                    reader = PdfReader(pdf)
                    merger.append(reader)

                # Save merged PDF to memory
                output_buffer = io.BytesIO()
                merger.write(output_buffer)

                # --- 4. Safe Filename ---
                safe_names = [re.sub(r'\W+', '', pdf.name.replace(".pdf", "")) for pdf in ordered_files]
                unique_name = f"merged_{'_'.join(safe_names)}.pdf"

                st.success("✅ Files merged successfully!")

                # --- 5. Download Button ---
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
