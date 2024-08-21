from bson import ObjectId
from fastapi import APIRouter
from app.database import db
from pydantic import BaseModel

class Benefit(BaseModel):
    name: str
    description: str
    category: str
    disc: float
    provider: str

router = APIRouter()

#Leer
@router.get("/Benefits")
async def get_benefit():
    benefits = db['descuentos'].find()
    return [{"id": str(item["_id"]), "name": item["name"], "description": item["description"]} for item in benefits]

# Crear
@router.post("/Benefits")
async def create_benefit(benefit: Benefit):
    result = db['descuentos'].insert_one(benefit.model_dump())
    return {"id": str(result.inserted_id), "name": benefit.name}

# Actualizar
@router.put("/Benefits/{benefit_id}")
async def update_benefit(benefit_id: str, benefit: Benefit):
    result = db['descuentos'].update_one({"_id": ObjectId(benefit_id)}, {"$set": benefit.model_dump()})
    if result.modified_count == 1:
        return {"message": "Benefit updated"}
    return {"message": "Benefit not found"}

# Eliminar
@router.delete("/Benefits/{benefit_id}")
async def delete_benefit(benefit_id: str):
    result = db['descuentos'].delete_one({"_id": ObjectId(benefit_id)})
    if result.deleted_count == 1:
        return {"message": "Benefit deleted"}
    return {"message": "Benefit not found"}
