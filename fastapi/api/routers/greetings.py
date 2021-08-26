from fastapi import APIRouter, Depends, Response, status
from starlette.requests import Request

from services.greetingService import GreetingService
from models.greetingDto import GreetingDto

from utils.utils import Utils

#import logging

router = APIRouter()

logger = Utils.manageGlobalLogger(__name__)

@router.get("/", response_model=GreetingDto, name="greetings", status_code=200)
async def get_predict(
    request: Request,
    response: Response = None
) -> GreetingDto:

    logger.info('Greetings endponit called!')

    gs = GreetingService()
    greeting = gs.greetings()

    response.status_code = status.HTTP_200_OK

    return greeting
