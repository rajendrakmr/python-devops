from fastapi import APIRouter, HTTPException
from services.metrics_services import get_system_metrics
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/s3", status_code=200)
def metrics():
    """
    This api will get all s3 storage.
    """
    
    try: 
        return {"message": "In progress for get S3 bucketes."}
    except Exception as e:
        logger.error(f"Error fetching metrics: {e}")
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )


@router.get("/ec2", status_code=200)
def metrics():
    """
    This api will get all ec2 instances.
    """
    
    try: 
        return {"message": "In progress for get ec2 instances."}
    except Exception as e:
        logger.error(f"Error fetching metrics: {e}")
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
