from typing import List

from entity import Entity
from pydantic import BaseModel
from relationship import Relationship


class KnowledgeGraph(BaseModel):
    entities: List[Entity]
    relationships: List[Relationship]
