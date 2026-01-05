from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def list_news():
    return {
        "message": "List of news (coming soon)"
    }
