from pydantic import BaseModel

class DicomPathDto(BaseModel):
    dicomPath: str  