from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class Entity(BaseModel):
    """Represents an entity in the knowledge graph."""

    name: str = Field(
        description="The name of the entity, e.g. 'Singapore', 'Person', 'Salmon'."
    )
    properties: Optional[Dict[str, Any]] = Field(
        description="The distinct properties that describe this entity."
    )

    def __repr__(self):
        return f"Entity(name={self.name!r}, properties={self.properties!r})"
