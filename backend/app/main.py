from fastapi import FastAPI
from app.api.endpoints import transporters
from app.api.endpoints import truck_elements
from app.api.endpoints import trucks
from app.api.endpoints import offer_elements
from app.api.endpoints import offers
from app.api.endpoints import auth


app = FastAPI (
        title = "GAMI Transport",
        description = "API de gestion de transport GAMI",
        version = "1.0.0"
    )

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Gami Transport"}

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    transporters.router,
    prefix = "/transporters",
    tags = ["Transporteurs"]
    )


app.include_router(
    truck_elements.router,
    prefix = "/truck",
    tags = ["Camion Element"]
)


app.include_router(
    trucks.router,
    prefix = "/truck",
    tags = ["Camions"]
)

app.include_router(
    offer_elements.router,
    prefix = "/offers",
    tags = ["Offres"]
)

app.include_router(
    offers.router,
    prefix = "/offers",
    tags = ["Offres"]
)
