from enum import Enum
from typing import List

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base 

class Sex(Enum):
    male = "M"
    female = "F"
    unknown = "U"

class B_symptoms(Enum):
    sweating = "Потливость"
    fever = "Лихорадка"
    weight_loss = "Снижение массы тела" 

class Histologic(Enum):	
    nod_sclerosis = "Нодулярный склероз"
    mixed_cell = "Смешанно-клеточный вариант"
    lymphocytic_predominance = "Лимфоцитарное преобладание"
    lymphocytic_depletion = "Лимфоцитарное истощение"
    nos = "NOS"
    nod_type = "Нодулярный тип с лимфоцитарным преобладанием"

class Stage(Enum):	
    stage_1 = "I"
    stage_2 = "II"
    stage_3 = "III" 
    stage_4 = "IV"

class Protocol(Enum): 
    euroNet = "EuroNet-PHL-C1"
    dal_2002 = "DAL-GPOH-2002"
    dal_2003 = "DAL-GPOH-2003"
    dal_1995 = "DAL-HD-1995"
    no_protocol = "Непрограмная терапия"  

class Group(Enum):
    tg_1 = "TG-1"
    tg_2 = "TG-2"
    tg_3 = "TG-3"

class Anat_request(Enum):
    full_remission = "полная ремиссия"
    full_not_resp = "полная ремиссия неподтвержденная" 
    part_remission = "частичная ремиссия"
    not_change = "без изменений"
    progression = "прогрессия"

class Deauville_score(Enum):
    ds_1 = "DS=1"
    ds_2 = "DS=2"
    ds_3 = "DS=3"
    ds_4 = "DS=4"
    ds_5 = "DS=5"

class Main_request(Enum):	
    adequate = "Адекватный ответ" 
    inadequate = "Неадекватный ответ"

class Event(Enum):
    no = "Отсутствует"
    relapse = "Рецидив"
    progression = "Прогрессия"
    transform = "Трансформация"
    death = "Смерть"

class Name(Base):
    __tablename__ = "name"
    
    id: Mapped[int] = mapped_column(primary_key=True)

    fio  = mapped_column(sa.String())

    person_id: Mapped[int] = mapped_column(sa.ForeignKey("person.id"))
    person: Mapped["Person"] = relationship(back_populates="names")


class Person(Base):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column(primary_key=True)

    early_toxicity  = mapped_column(sa.String())
    ray_therapy  = mapped_column(sa.String())
    ray_therapy_comp  = mapped_column(sa.String())
    sex = mapped_column(sa.Enum(Sex))
    event = mapped_column(sa.Enum(Event))
    main_request = mapped_column(sa.Enum(Main_request))
    deauville_score = mapped_column(sa.Enum(Deauville_score))
    anat_request = mapped_column(sa.Enum(Anat_request))
    group = mapped_column(sa.Enum(Group))
    protocol = mapped_column(sa.Enum(Protocol))
    stage = mapped_column(sa.Enum(Stage))
    histologic = mapped_column(sa.Enum(Histologic))
    b_symptoms = mapped_column(sa.Enum(B_symptoms))
    region  = mapped_column(sa.String())
    e_impact  = mapped_column(sa.String())
    bm_damage_myelogram = mapped_column(sa.String())
    bm_damage_kt  = mapped_column(sa.String())
    request_pat  = mapped_column(sa.String()) 	
    start_therapy_date  = mapped_column(sa.Date())
    end_therapy_date  = mapped_column(sa.Date())
    event_date  = mapped_column(sa.Date())
    last_date  = mapped_column(sa.Date())	
    birth_date = mapped_column(sa.Date())
    leykocytes  = mapped_column(sa.Integer())	
    hemoglobin = mapped_column(sa.Integer())
    trombocytes = mapped_column(sa.Integer()) 	
    ldh = mapped_column(sa.Integer())	
    ebv = mapped_column(sa.Integer())	
    esr = mapped_column(sa.Integer()) 	
    init_val = mapped_column(sa.Integer())	
    tumor_val = mapped_column(sa.Integer())	

    names: Mapped[List["Name"]] = relationship(cascade="all, delete-orphan")


name_index = (
    sa.func.row_number()
    .over(partition_by=Name.person_id)
    .label("i")
)

indexed_names = sa.select(Name, name_index).subquery()
primary_names = sa.select(indexed_names).filter(indexed_names.c.i == 1).subquery()
