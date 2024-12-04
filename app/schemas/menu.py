from pydantic import BaseModel


class MenuResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True


class MenuCreate(BaseModel):
    name: str
    description: str
