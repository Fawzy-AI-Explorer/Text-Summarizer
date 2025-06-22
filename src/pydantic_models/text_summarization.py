"""Pydantic models for text summarization tasks."""

from pydantic import BaseModel, Field

class TextSummarization(BaseModel):
    """Request model for text summarization.
    Attributes:
        summarized_text (str): The text to be summarized.
    """

    summarized_text: str = Field(
        ...,
        description="summarized text.",
        max_length=300,
        min_length=10
    )
