import streamlit as st
import pandas as pd
import os

from dotenv import load_dotenv

from crew import create_lead_crew


load_dotenv()


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(

    page_title="AI Lead Generation Agent",

    page_icon="🎯",

    layout="wide"
)


# =========================================================
# HEADER
# =========================================================

st.title("🎯 AI Lead Generation Agent")

'''st.markdown(
    """
    **Multi-Agent B2B Lead Research Platform**

    Powered by:

    - CrewAI
    - Google Gemini
    - Web Search
    - Streamlit
    """
)'''


st.divider()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("Lead Search")

    country = st.text_input(
        "Country",
        placeholder="Example: India"
    )

    industry = st.text_input(
        "Industry / Domain",
        placeholder="Example: Healthcare"
    )

    lead_criteria = st.text_area(

        "Optional Lead Criteria",

        placeholder=(
            "Example:\n"
            "Companies with 200+ employees\n"
            "Companies investing in AI\n"
            "Companies undergoing digital transformation"
        )
    )

    st.divider()

    st.info(
        "The agents will research companies, "
        "decision makers, business intelligence "
        "and lead relevance."
    )


# =========================================================
# VALIDATION
# =========================================================

if not country:

    st.warning(
        "Please enter a country."
    )

elif not industry:

    st.warning(
        "Please enter an industry."
    )


# =========================================================
# START RESEARCH
# =========================================================

if st.button(
    "🚀 Find Leads",
    type="primary",
    use_container_width=True
):

    if not country or not industry:

        st.error(
            "Country and Industry are required."
        )

        st.stop()


    inputs = {

        "country": country,

        "industry": industry,

        "lead_criteria":
            lead_criteria
            if lead_criteria
            else "No additional criteria."
    }


    # -----------------------------------------------------
    # Progress
    # -----------------------------------------------------

    progress = st.progress(0)

    status = st.empty()


    status.info(
        "🔎 Starting company research..."
    )

    progress.progress(10)


    try:

        crew = create_lead_crew()


        status.info(
            "🤖 AI agents are researching companies..."
        )

        progress.progress(25)


        result = crew.kickoff(
            inputs=inputs
        )


        progress.progress(100)

        status.success(
            "✅ Lead research completed."
        )


        # -------------------------------------------------
        # RESULT
        # -------------------------------------------------

        st.divider()

        st.header(
            "📊 Lead Intelligence Report"
        )


        st.markdown(
            result.raw
        )


        # -------------------------------------------------
        # DOWNLOAD
        # -------------------------------------------------

        st.download_button(

            label="📥 Download Report",

            data=result.raw,

            file_name="lead_research_report.txt",

            mime="text/plain"
        )


    except Exception as e:

        progress.empty()

        status.empty()

        st.error(
            f"An error occurred:\n\n{str(e)}"
        )

        st.exception(e)
