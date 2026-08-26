from typing import List

from pydantic import BaseModel, Field

class DecisionMaker(BaseModel):
    name: str = ""
    title: str = ""
    linkedin_url: str = ""
    evidence: str = ""


class Lead(BaseModel):
    company_name: str
    website: str = ""
    country: str = ""
    industry: str = ""

    company_description: str = ""
    company_size: str = ""
    headquarters: str = ""

    products_services: List[str] = Field(default_factory=list)

    business_problem: str = ""
    ai_opportunity: str = ""

    decision_makers: List[DecisionMaker] = Field(
        default_factory=list
    )

    relevance_score: int = Field(
        default=0,
        ge=0,
        le=100
    )

    score_reason: str = ""

    lead_priority: str = ""

    lead_summary: str = ""

    sources: List[str] = Field(
        default_factory=list
    )
