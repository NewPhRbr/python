from datetime import date
from typing import Optional
from pydantic import BaseModel

from model import Sex, Event, Main_request, Deauville_score, Anat_request, Group, Protocol, Stage, Histologic, B_symptoms

class Name(BaseModel):
    id: int

    fio: Optional[str]
    
    class Config:
        from_attributes = True
        from_attributes = True

class Person(BaseModel):

    id: int
    early_toxicity: Optional[str]
    ray_therapy: Optional[str]
    ray_therapy_comp: Optional[str]
    sex: Optional[Sex]
    event: Optional[Event]
    main_request: Optional[Main_request]
    deauville_score: Optional[Deauville_score]
    anat_request: Optional[Anat_request]
    group: Optional[Group]
    protocol: Optional[Protocol]
    stage: Optional[Stage]
    histologic: Optional[Histologic]
    b_symptoms: Optional[B_symptoms]
    region: Optional[str]
    e_impact: Optional[str]
    bm_damage_myelogram: Optional[str]
    bm_damage_kt: Optional[str]
    request_pat: Optional[str]
    start_therapy_date: Optional[date]
    end_therapy_date: Optional[date]
    event_date: Optional[date]
    last_date: Optional[date]
    birth_date: Optional[date]
    leykocytes: Optional[int]
    hemoglobin: Optional[int]
    trombocytes: Optional[int]
    ldh: Optional[int]
    ebv: Optional[int]
    esr: Optional[int]
    init_val: Optional[int]
    tumor_val: Optional[int]

    class Config:
        from_attributes = True
        from_attributes = True