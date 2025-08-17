from typing import List

from pydantic import BaseModel

from .entity import Entity
from .relationship import Relationship


class KnowledgeGraph(BaseModel):
    entities: List[Entity]
    relationships: List[Relationship]
