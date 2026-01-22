from fastapi import APIRouter, HTTPException
from services.metrics_services import get_system_metrics
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/metrics", status_code=200)
def metrics():
    """
    This api will get system metrics of current running usagge
    """
    
    try:
        metrics = get_system_metrics()
        return metrics
    except Exception as e:
        logger.error(f"Error fetching metrics: {e}")
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
