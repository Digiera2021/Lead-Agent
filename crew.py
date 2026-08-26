from crewai import Crew, Process

from agents import (
    company_researcher,
    decision_maker_researcher,
    business_analyst,
    lead_qualifier,
    lead_scorer,
    lead_summary_agent
)

from tasks import (
    create_company_research_task,
    create_decision_maker_task,
    create_business_analysis_task,
    create_qualification_task,
    create_scoring_task,
    create_summary_task
)


def create_lead_crew():

    company_task = create_company_research_task(
        company_researcher
    )

    decision_task = create_decision_maker_task(
        decision_maker_researcher
    )

    business_task = create_business_analysis_task(
        business_analyst
    )

    qualification_task = create_qualification_task(
        lead_qualifier
    )

    scoring_task = create_scoring_task(
        lead_scorer
    )

    summary_task = create_summary_task(
        lead_summary_agent
    )


    crew = Crew(

        agents=[
            company_researcher,
            decision_maker_researcher,
            business_analyst,
            lead_qualifier,
            lead_scorer,
            lead_summary_agent
        ],

        tasks=[
            company_task,
            decision_task,
            business_task,
            qualification_task,
            scoring_task,
            summary_task
        ],

        process=Process.sequential,

        verbose=True
    )

    return crew
