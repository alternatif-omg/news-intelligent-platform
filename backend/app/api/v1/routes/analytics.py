from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def analytics_overview():
    return {
        "message": "Analytics endpoint (coming soon)"
    }
