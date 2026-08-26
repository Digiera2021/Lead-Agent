from crewai import Task

def create_company_research_task(agent):

    return Task(

        description="""
        Research companies in:

        Country:
        {country}

        Industry:
        {industry}

        Optional Lead Criteria:
        {lead_criteria}

        Find approximately 5-10 relevant companies.

        For every company identify:

        1. Company name
        2. Website
        3. Country
        4. Industry
        5. Headquarters
        6. Company description
        7. Products/services
        8. Company size if available
        9. Recent business or technology initiatives
        10. Potential AI opportunities
        11. Sources

        Do not invent information.

        Prefer official company websites and reliable business
        sources.

        Return clear structured research.
        """,

        expected_output="""
        A research report containing 5-10 relevant companies
        with evidence and source URLs.
        """,

        agent=agent
    )


def create_decision_maker_task(agent):

    return Task(

        description="""
        Using the companies identified in the previous research,
        identify likely decision makers.

        Look specifically for:

        - CEO
        - Founder
        - COO
        - CIO
        - CTO
        - CDO
        - VP
        - Director
        - Head of Digital
        - Head of AI
        - Head of Technology
        - Head of Operations
        - Procurement leadership

        For every person provide:

        Company
        Name
        Job title
        LinkedIn URL if publicly available
        Evidence/source

        Never invent a person's name or position.
        If a decision maker cannot be verified, state that.
        """,

        expected_output="""
        A company-by-company list of verified or clearly
        identified potential decision makers with sources.
        """,

        agent=agent
    )


def create_business_analysis_task(agent):

    return Task(

        description="""
        Analyze the researched companies.

        For each company determine:

        - Business model
        - Main products/services
        - Target customers
        - Technology maturity
        - Digital transformation signals
        - AI adoption signals
        - Potential business problems
        - Potential AI use cases
        - Why this company could be a relevant lead
        - Evidence supporting the analysis

        Separate verified facts from reasonable inference.
        """,

        expected_output="""
        A business intelligence analysis for each researched
        company.
        """,

        agent=agent
    )


def create_qualification_task(agent):

    return Task(

        description="""
        Qualify each researched company against the following:

        Country:
        {country}

        Industry:
        {industry}

        Lead Criteria:
        {lead_criteria}

        Determine:

        1. Strong Fit
        2. Moderate Fit
        3. Weak Fit

        Explain the qualification decision.

        Consider:

        - Country fit
        - Industry fit
        - Company relevance
        - Business need
        - AI opportunity
        - Technology maturity
        - Decision-maker availability
        """,

        expected_output="""
        A qualification assessment for every company with
        clear reasoning.
        """,

        agent=agent
    )


def create_scoring_task(agent):

    return Task(

        description="""
        Score each company from 0 to 100.

        Use this scoring framework:

        Industry Fit       = 20 points
        Country Fit        = 10 points
        Company Fit        = 15 points
        Business Need      = 20 points
        AI Opportunity     = 15 points
        Decision Maker     = 10 points
        Evidence Quality   = 10 points

        Total = 100 points.

        Provide:

        Company
        Individual scores
        Total score
        Score explanation
        Priority

        Priority rules:

        80-100 = High
        60-79  = Medium
        Below 60 = Low
        """,

        expected_output="""
        A scored lead list with transparent scoring logic.
        """,

        agent=agent
    )


def create_summary_task(agent):

    return Task(

        description="""
        Create a final sales-ready lead summary.

        For each company provide:

        Company
        Website
        Industry
        Company description
        Key business problem
        AI opportunity
        Decision makers
        Relevance score
        Priority
        Why this is a good lead
        Recommended outreach angle
        Sources

        Keep the summary concise but useful.

        Do not invent information.
        """,

        expected_output="""
        A final structured lead intelligence report suitable
        for display in a Streamlit application.
        """,

        agent=agent
    )
