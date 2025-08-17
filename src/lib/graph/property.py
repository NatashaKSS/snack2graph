from pydantic import BaseModel, Field


class Property(BaseModel):
    """Represents a property where the key is the name and the value can be anything arbitrary."""

    key: str = Field(description="Name of the property.")
    value: str | int | float = Field(description="Value for this property.")

    def __repr__(self):
        return f"Property(key={self.key!r}, value={self.value!r})"
