import streamlit as st
from agent import process_transcript

st.set_page_config(page_title="Smart-Minute Agent", layout="wide")

st.title("👔 Smart-Minute Workflow Agent")
st.caption("Transform chaotic meeting transcripts into structured actions instantly.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Stream")
    transcript_input = st.text_area(
        "Paste your raw meeting transcript or notes here:",
        height=450,
        placeholder="Example:\nJohn: We need the backend API completed by Friday.\nSarah: I can handle that..."
    )
    generate_btn = st.button("Analyze & Automate Workflow", type="primary", use_container_width=True)

with col2:
    st.subheader("Automated Execution Matrix")
    
    if generate_btn and transcript_input.strip():
        with st.spinner("Autonomous agent processing context..."):
            result = process_transcript(transcript_input)
            
            if "error" in result:
                st.error(result["error"])
            else:
                tab1, tab2, tab3 = st.tabs(["📋 Executive Minutes", "✅ Task Allocation Table", "✉️ Email Broadcast Draft"])
                
                with tab1:
                    st.markdown(result["minutes"])
                with tab2:
                    st.markdown(result["tasks"])
                with tab3:
                    st.markdown("### Actionable Email Template")
                    st.text_area("Ready to Copy & Distribute:", value=result["email"], height=350)
    elif generate_btn:
        st.warning("Input text stream cannot be empty.")
    else:
        st.info("System idling. Insert raw contextual notes on the left to activate agent tasks.")
