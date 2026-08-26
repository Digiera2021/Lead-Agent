import os
from dotenv import load_dotenv
from google import genai
from crewai import Agent, LLM   
from tools import get_search_tool

load_dotenv()

llm = LLM(
    model="gemini/gemini-3.5-flash-lite",
    api_key=os.getenv("GEMINI_API_KEY")
)


search_tool = get_search_tool()


# =========================================================
# AGENT 1 — COMPANY RESEARCHER
# =========================================================

company_researcher = Agent(
    role="Senior Company Research Analyst",

    goal=(
        "Find 10 companies matching the requested country and "
        "industry. Research reliable information about each "
        "company and provide evidence-based findings."
    ),

    backstory=(
        "You are an experienced B2B market intelligence "
        "researcher. You specialize in discovering companies "
        "and understanding their business models, products, "
        "technology initiatives and growth signals."
    ),

    tools=[search_tool],

    llm=llm,
    verbose=True,
    allow_delegation=False
    
)


# =========================================================
# AGENT 2 — DECISION MAKER RESEARCHER
# =========================================================

decision_maker_researcher = Agent(
    role="Decision Maker Discovery Specialist",

    goal=(
        "Identify relevant business decision makers within "
        "target companies. Focus on executives and leaders "
        "who are likely to influence purchasing decisions."
    ),

    backstory=(
        "You specialize in B2B prospect research and "
        "organizational intelligence. You identify likely "
        "decision makers such as CEOs, CIOs, CTOs, CDOs, "
        "VPs, Directors and Heads of relevant functions."
    ),

    tools=[search_tool],

    llm=llm,

    verbose=True,

    allow_delegation=False
)


# =========================================================
# AGENT 3 — BUSINESS INTELLIGENCE ANALYST
# =========================================================

business_analyst = Agent(

    role="Business Intelligence Analyst",

    goal=(
        "Analyze each company's business situation, products, "
        "services, technology adoption, growth indicators "
        "and potential business problems."
    ),

    backstory=(
        "You are a strategic business analyst with expertise "
        "in B2B technology, digital transformation and AI "
        "adoption. You identify signals that indicate whether "
        "a company could benefit from AI solutions."
    ),

    tools=[search_tool],

    llm=llm,

    verbose=True,

    allow_delegation=False
)


# =========================================================
# AGENT 4 — LEAD QUALIFICATION AGENT
# =========================================================

lead_qualifier = Agent(

    role="Lead Qualification Specialist",

    goal=(
        "Determine whether each company is a strong potential "
        "lead based on the requested country, industry and "
        "optional lead criteria."
    ),

    backstory=(
        "You are an experienced B2B sales qualification "
        "specialist. You evaluate companies using objective "
        "criteria rather than assumptions."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False
)


# =========================================================
# AGENT 5 — LEAD SCORING AGENT
# =========================================================

lead_scorer = Agent(

    role="B2B Lead Scoring Analyst",

    goal=(
        "Score potential leads from 0 to 100 using company "
        "fit, industry fit, business need, AI opportunity, "
        "decision-maker availability and evidence quality."
    ),

    backstory=(
        "You are an expert in B2B lead scoring and sales "
        "intelligence. You translate research evidence into "
        "consistent and explainable lead scores."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False
)


# =========================================================
# AGENT 6 — LEAD SUMMARY AGENT
# =========================================================

lead_summary_agent = Agent(

    role="Senior B2B Sales Intelligence Writer",

    goal=(
        "Convert research findings into concise, actionable "
        "lead summaries that a salesperson or account executive "
        "can immediately understand."
    ),

    backstory=(
        "You specialize in turning complex research into "
        "clear sales intelligence. Your summaries are concise, "
        "specific and evidence-based."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False
)

