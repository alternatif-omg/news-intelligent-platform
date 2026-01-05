from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def search_news():
    return {
        "message": "Search endpoint (coming soon)"
    }
