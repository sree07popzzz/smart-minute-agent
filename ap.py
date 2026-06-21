import streamlit as st
import streamlit.components.v1 as components
import time
# Import the clean backend function from agent.py
from agent import process_transcript

# =====================================================================
# 1. MANDATORY FIRST LINE FOR STREAMLIT
# =====================================================================
st.set_page_config(
    page_title="Smart-Minute Agent Dashboard",
    page_icon="🤖",
    layout="wide"
)

# =====================================================================
# 2. HIGH-TECH DARK CYBER THEME (CSS INJECTION - DOWNLOAD BUTTON FIX)
# =====================================================================
custom_cyber_theme = """
<style>
    /* Force main application background and global text color */
    .stApp {
        background-color: #0d1117 !important;
        color: #ffffff !important;
    }
    
    /* Style all main headers and subheaders globally to vibrant Teal Green */
    h1, h2, h3, h4, h5, h6, 
    [data-testid="stMarkdownContainer"] h1, 
    [data-testid="stMarkdownContainer"] h2, 
    [data-testid="stMarkdownContainer"] h3 {
        color: #00f0c2 !important;
        font-family: 'Courier New', Courier, monospace !important;
        font-weight: bold !important;
    }

    /* Style regular paragraph and labels to white for dark mode readability */
    p, span, label, [data-testid="stWidgetLabel"] p {
        color: #ffffff !important;
    }

    /* Force text inputs/text areas to have dark backgrounds and clear white text */
    textarea, [data-testid="stTextArea"] div div div textarea {
        background-color: #161b22 !important;
        color: #ffffff !important;
        border: 2px solid #30363d !important;
    }
    
    /* Highlight the text input border on focus */
    textarea:focus {
        border-color: #00f0c2 !important;
    }

    /* Make the placeholder text ("Speaker 1:...") explicitly visible */
    textarea::placeholder {
        color: #8b949e !important;
        opacity: 1 !important;
    }
    
    /* Style Streamlit's informational alert boxes (st.info) for high contrast */
    [data-testid="stAlert"] {
        background-color: #161b22 !important;
        border: 1px solid #00f0c2 !important;
    }
    [data-testid="stAlert"] div {
        color: #00f0c2 !important;
        font-weight: bold !important;
    }
    [data-testid="stAlert"] p {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* Primary Processing Button styling (Solid neon-teal) */
    .stButton > button {
        background-color: #00f0c2 !important;
        color: #0d1117 !important;
        font-weight: bold !important;
        font-size: 16px !important;
        border: 2px solid #00f0c2 !important;
        border-radius: 8px !important;
    }
    .stButton > button:hover, .stButton > button:focus {
        background-color: #00f0c2 !important;
        color: #0d1117 !important;
        box-shadow: 0 0 12px #00f0c2 !important;
    }

    /* FIX: Download Button Styling - Crisp Dark Text on an Elegant White/Silver Background */
    [data-testid="stDownloadButton"] > button {
        background-color: #ffffff !important;
        color: #0d1117 !important;
        font-weight: bold !important;
        font-size: 15px !important;
        border: 2px solid #ffffff !important;
        border-radius: 8px !important;
    }
    [data-testid="stDownloadButton"] > button:hover {
        background-color: #00f0c2 !important;
        border-color: #00f0c2 !important;
        color: #0d1117 !important;
        box-shadow: 0 0 12px #00f0c2 !important;
    }
    /* Fix internal icon or button text elements for download buttons */
    [data-testid="stDownloadButton"] p {
        color: #0d1117 !important;
        font-weight: bold !important;
    }

    /* Style the Sidebar container background */
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 2px solid #00f0c2 !important;
    }
    
    /* Style the multi-tabs to match the dark cyber look */
    button[data-baseweb="tab"] {
        background-color: transparent !important;
        font-weight: bold !important;
    }
    button[data-baseweb="tab"] p {
        color: #8b949e !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        border-bottom-color: #00f0c2 !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] p {
        color: #00f0c2 !important;
    }
</style>
"""
st.markdown(custom_cyber_theme, unsafe_allow_html=True)

# =====================================================================
# 3. SIDEBAR NAVIGATION
# =====================================================================
with st.sidebar:
    st.title("🤖 Smart-Minute Agent")
    st.markdown("### Autonomous Administrative Layer")
    st.write("Converts unstructured meeting audio transcripts into structured enterprise assets.")
    st.divider()
    st.caption("🚀 System Status: Operational")
    st.caption("💻 Environment: Cross-Platform Verified (Ubuntu & Windows 11)")

# =====================================================================
# 4. MAIN INTERFACE WORKSPACE
# =====================================================================
st.title("💼 Executive Meeting Dashboard")
st.write("Mapping raw speech logs into structured enterprise work products.")
st.divider()

col1, col2 = st.columns([1, 1.2])

# --- LEFT COLUMN: INPUT STREAM ---
with col1:
    st.subheader("📥 Raw Input Stream")
    raw_transcript_input = st.text_area(
        "Paste Conversation Log Below:", 
        placeholder="Speaker 1: Let's finalize the testing metrics by 2 PM.\nSpeaker 2: Sounds good, I'll review it on Windows to check cross-platform capability...",
        height=400,
        key="main_transcript_input"
    )
    process_button = st.button("⚡ Process and Structure Data", use_container_width=True)

# --- RIGHT COLUMN: STRUCTURED OUTPUT ---
with col2:
    st.subheader("📤 Structured Output Assets")
    
    if process_button and raw_transcript_input:
        with st.spinner("🤖 Extracting semantic intent and validating type schemas..."):
            time.sleep(1) # Pacing effect for presentation
            try:
                # Call our clean backend function from agent.py
                response_data = process_transcript(raw_transcript_input)
            except Exception as e:
                st.error(f"Processing Error: {str(e)}")
                response_data = None

        if response_data:
            tab1, tab2, tab3 = st.tabs(["📝 Executive Minutes", "📋 Task Allocations", "📧 Broadcast Email"])
            
            with tab1:
                st.markdown("### Executive Summary")
                st.write(response_data["summary"])
                st.divider()
                
                # Report compilation logic
                task_txt = "\n".join([f"- {t['owner']}: {t['task']} (Due: {t['deadline']})" for t in response_data["tasks"]])
                full_report_content = f"SUMMARY:\n{response_data['summary']}\n\nACTION ITEMS:\n{task_txt}"
                
                # UTILITY 1: DOWNLOAD REPORT BUTTON (FIXED THEME VISIBILITY)
                st.download_button(
                    label="📥 Download Complete Minutes Report (.txt)",
                    data=full_report_content,
                    file_name="Smart_Minute_Executive_Report.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                
            with tab2:
                st.markdown("### Localized Project Tracking Grid")
                md_table = "| Owner | Task Description | Deadline |\n| :--- | :--- | :--- |\n"
                for item in response_data["tasks"]:
                    md_table += f"| **{item['owner']}** | {item['task']} | `{item['deadline']}` |\n"
                st.markdown(md_table)
                
            with tab3:
                st.markdown("### Broadcast-Ready Notification")
                email_text = response_data["email"]
                st.text_area("Drafted Content:", email_text, height=220, key="email_box")
                
                # UTILITY 2: CUSTOM STYLIZED CYBER COPY BUTTON (JS INJECTION)
                escaped_email = email_text.replace("`", "\\`").replace("'", "\\'").replace('"', '\\"')
                copy_button_html = f"""
                <button id="copy-btn" style="
                    width: 100%; 
                    background-color: #00f0c2; 
                    color: #0d1117; 
                    border: none; 
                    padding: 12px; 
                    border-radius: 8px; 
                    cursor: pointer; 
                    font-weight: bold;
                    font-size: 14px;
                    transition: all 0.2s ease;">
                    📋 Copy Email to Clipboard
                </button>
                <script>
                document.getElementById('copy-btn').addEventListener('click', function() {{
                    navigator.clipboard.writeText(`{escaped_email}`).then(function() {{
                        const btn = document.getElementById('copy-btn');
                        btn.innerText = '✅ Copied to Clipboard!';
                        btn.style.backgroundColor = '#24a0ed';
                        btn.style.color = '#ffffff';
                        setTimeout(function() {{
                            btn.innerText = '📋 Copy Email to Clipboard';
                            btn.style.backgroundColor = '#00f0c2';
                            btn.style.color = '#0d1117';
                        }}, 2000);
                    }});
                }});
                </script>
                """
                components.html(copy_button_html, height=60)
    else:
        st.info("👈 Enter a conversation log and click process to generate the administrative layer.")
