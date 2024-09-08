from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List


class Person(BaseModel):
    nome: str = Field(description="O nome da pessoa.")
    rg: str = Field(description="O RG da pessoa.")
    cpf: str = Field(description="O CPF da pessoa.")
    endereco: str = Field(description="O endereço da pessoa.")
    
    
class Company(BaseModel):
    razao_social: str = Field(description="A razão social da empresa.")
    cnpj: str = Field(description="O CNPJ da empresa.")
    endereco: str = Field(description="O endereço da empresa.")
    representante: Person = Field(description="O representante (pessoa) da empresa.")
    

class InvoiceJson(BaseModel):
    numero_contrato: str = Field(description="O número do contrato do contrato (ID).")
    objeto_contrato: str = Field(description="O objeto do contrato.")
    data_contrato: str = Field(description="A data em que o contrato foi escrito.")
    valor_contrato: str = Field(description="O valor do contrato.")
    vigencia_contrato: str = Field(description="A vigência do contrato.")
    contratante: Company = Field(description="A empresa contratante.")
    contratada: Company = Field(description="A empresa contratada.")
    pessoas_citadas: List[Person] = Field(default_factory=list, description="A lista de pessoas citadas.")
