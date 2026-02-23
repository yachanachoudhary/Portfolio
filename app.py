import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Yachana Choudhary | Portfolio", layout="wide")

# 2. Professional High-Contrast CSS (No Emojis)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .metric-container {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
    }
    h1, h2, h3 { color: #58a6ff !important; font-family: 'Segoe UI', sans-serif; }
    .stExpander { border: 1px solid #30363d !important; background-color: #0d1117 !important; }
    .project-tag {
        background-color: rgba(88, 166, 255, 0.1);
        color: #58a6ff;
        padding: 2px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
        border: 1px solid rgba(88, 166, 255, 0.2);
        margin-right: 5px;
    }
    .hero-section {
        background-color: rgba(88, 166, 255, 0.05); 
        padding: 25px; 
        border-radius: 10px; 
        border-left: 5px solid #58a6ff;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
st.sidebar.title("Yachana Choudhary")
st.sidebar.markdown("**Data Scientist & Analyst**")
st.sidebar.markdown("M.Sc. Data Science & Analytics")
st.sidebar.markdown("Jain University")
st.sidebar.write("---")

page = st.sidebar.radio("Navigation", ["Overview Dashboard", "Technical Projects", "Research & Certifications"])

st.sidebar.write("---")
st.sidebar.markdown("### Professional Links")
st.sidebar.markdown("[LinkedIn Profile](https://www.linkedin.com/in/yachana-choudhary/)")
st.sidebar.markdown("[GitHub Repository](https://github.com/yachanachoudhary)")
st.sidebar.info("Contact: 24msrds063@jainuniversity.ac.in")

# --- PAGE 1: OVERVIEW DASHBOARD ---
if page == "Overview Dashboard":
    st.title("Professional Profile Dashboard")
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="metric-container"><h3>8.38 CGPA</h3><p>Academic Excellence</p></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-container"><h3>Class Representative</h3><p>M.Sc. DSA Leadership</p></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-container"><h3> Technical Projects</h3><p>Full-Stack Capability</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    
    st.subheader("Technical Competency Analysis")
    skills_df = pd.DataFrame({
        "Skill": ["Python", "SQL", "Power BI", "GenAI / RAG", "Time Series", "SAS"],
        "Level": [95, 92, 90, 85, 88, 80]
    })
    fig = px.line_polar(skills_df, r='Level', theta='Skill', line_close=True, template="plotly_dark")
    fig.update_traces(fill='toself', line_color='#58a6ff')
    st.plotly_chart(fig, use_container_width=True)

    st.header("Executive Summary")
    st.markdown("""
    <div class="hero-section">
        <p style="font-size:18px; line-height:1.6;">
        I approach Data Science with the precision of a <strong>Physicist</strong> and the vision of a <strong>Product Strategist</strong>. 
        Currently completing my Master’s at <strong>Jain University</strong>, I engineer solutions that turn complex signals into clear, actionable business decisions.
        <br><br>
        As a <strong>Class Representative</strong>, I thrive at the intersection of technical excellence and human communication. 
        Whether I am deploying <strong>RAG-based Generative AI</strong> or designing <strong>Power BI dashboards</strong>, my goal is to ensure data drives impact.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- PAGE 2: PROJECT PORTFOLIO ---
elif page == "Technical Projects":
    st.title("Technical Case Studies")

    # 1. GenAI Enterprise Knowledge Assistant
    with st.expander("1. GenAI Enterprise Knowledge Assistant", expanded=True):
        st.markdown("<span class='project-tag'>GenAI</span> <span class='project-tag'>RAG</span> <span class='project-tag'>FAISS</span>", unsafe_allow_html=True)
        st.write("**Objective:** Developed an AI tool to interpret and comprehend company PDFs to provide immediate answers to intricate inquiries.")
        st.write("**Technical Detail:** Employed a dedicated vector database (FAISS) for rapid retrieval of pertinent information from hundreds of pages.")
        st.write("**Outcome:** Designed for zero-hallucination by relying exclusively on unique local files for responses.")
        

    # 2. Bias-Aware AI Resume Screening
    with st.expander("2. Bias-Aware AI Resume Screening & Ranking"):
        st.markdown("<span class='project-tag'>NLP</span> <span class='project-tag'>AI Ethics</span> <span class='project-tag'>Machine Learning</span>", unsafe_allow_html=True)
        st.write("**Objective:** Created an AI-based resume evaluation system to prioritize candidates according to suitability.")
        st.write("**Technical Detail:** Utilized NLP methods for extracting skills and identified gender and education bias via statistical fairness measures.")
        st.write("**Outcome:** Enhanced ethical AI choices through the creation of bias-corrected rankings.")

    # 3. Walmart Store Sales Forecasting
    with st.expander("3. Walmart Store Sales Analysis & Forecasting"):
        st.markdown("<span class='project-tag'>Prophet</span> <span class='project-tag'>SARIMAX</span> <span class='project-tag'>Time Series</span>", unsafe_allow_html=True)
        st.write("**Data Engineering:** Analyzed Walmart weekly sales data utilizing Python (Pandas) and conducting feature engineering to identify seasonal patterns.")
        st.write("**Predictive Modeling:** Developed and assessed Prophet and SARIMAX time-series models to project future revenue with high precision.")
        st.write("**Visualization:** Examined the relationship between sales and economic indicators such as CPI, Unemployment, and Fuel Prices.")
        

    # 4. Programmatic Advertising Analytics
    with st.expander("4. Programmatic Advertising Performance Analytics"):
        st.markdown("<span class='project-tag'>SQL</span> <span class='project-tag'>Power BI</span> <span class='project-tag'>Analytics</span>", unsafe_allow_html=True)
        st.write("**Objective:** Analyzed simulated ad performance data to evaluate CTR, ROI, CPC, and conversions.")
        st.write("**Technical Detail:** Used SQL to process large log-level datasets and identify high-impact campaigns.")
        st.write("**Outcome:** Built Power BI dashboards to support data-driven ad revenue optimization decisions.")

    # 5. Cancer Data Diagnostic Modeling
    with st.expander("5. Cancer Data Diagnostic Modeling"):
        st.markdown("<span class='project-tag'>Healthcare</span> <span class='project-tag'>Deep Learning</span> <span class='project-tag'>Python</span>", unsafe_allow_html=True)
        st.write("**Focus:** Application of Deep Learning and Machine Learning in healthcare diagnostics.")
        st.write("**Skills:** Classification, diagnostic analysis, and predictive modeling for medical datasets.")

    # 6. Database Management Interface
    with st.expander("6. Database Management Interface (Python UI)"):
        st.markdown("<span class='project-tag'>DBMS</span> <span class='project-tag'>Python</span> <span class='project-tag'>SQL</span>", unsafe_allow_html=True)
        st.write("**Technical Stack:** SQL and Python integration for efficient data management.")
        st.write("**Feature:** Built a functional interface to query and manage relational databases securely.")

    # 7. Zomato Multivariate Data Analysis
    with st.expander("7. Zomato Multivariate Data Analysis"):
        st.markdown("<span class='project-tag'>Statistics</span> <span class='project-tag'>Multivariate Analysis</span> <span class='project-tag'>Power BI</span>", unsafe_allow_html=True)
        st.write("**Analysis:** Used multivariate statistical techniques to identify restaurant success drivers.")
        st.write("**Skills:** Data cleaning, statistical quality control, and visual storytelling.")

    # 8. Fitness Data Decision Support
    with st.expander("8. Fitness Data Decision Support"):
        st.markdown("<span class='project-tag'>Internship</span> <span class='project-tag'>Decision Science</span>", unsafe_allow_html=True)
        st.write("**Context:** Internship project at MedTourEasy analyzing fitness metrics.")
        st.write("**Outcome:** Improved understanding of how data directly informs organizational decision-making and improved skills in team communication.")

# --- PAGE 3: RESEARCH & CERTIFICATIONS ---
elif page == "Research & Certifications":
    st.title("Research & Verified Credentials")
    
    st.subheader("Research Internship: Satellite Signal Correction")
    st.write("**Objective:** Engaged in academic research at Jain University involving satellite signal correction.")
    st.write("**Technical Detail:** Utilized Total Electron Content (TEC) modeling for GNSS/IRNSS receiver data to improve signal accuracy.")
    st.write("**Output:** Performed statistical analysis and data visualization using Python and contributed to technical documentation.")
    
    st.header("Verified Certifications")
    st.write("- **Google**: Data Analytics & R Programming")
    st.write("- **IBM**: Machine Learning with Python")
    st.write("- **University of Colorado**: Probability Foundations for Data Science and AI")
    st.write("- **UC Santa Cruz**: Bayesian Statistics: Concepts, Data Analysis, and Models")
    st.write("- **Jain University**: Big Data, SAS Programming, and Essentials of NLP")