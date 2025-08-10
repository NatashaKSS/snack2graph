from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class Relationship(BaseModel):
    """Represents a relationship in the knowledge graph."""

    source: str = Field(description="Source entity name.")
    target: str = Field(description="Target entity name.")
    relation: str = Field(
        description="The type of this relationship, e.g. 'used_by', 'owns', typically used in the context of '<Source><Relationship Type><Target>'."
    )
    properties: Optional[Dict[str, Any]] = Field(
        description="The distinct properties that describe this relationship."
    )

    def __repr__(self):
        return f"Relationship(from={self.source!r}, to={self.target!r}, relation={self.relation!r}, properties={self.properties!r})"
