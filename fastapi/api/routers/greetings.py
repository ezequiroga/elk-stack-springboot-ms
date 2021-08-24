from fastapi import APIRouter, Depends, Response, status
from starlette.requests import Request

from services.greetingService import GreetingService
from models.greetingDto import GreetingDto

from utils.utils import Utils

#import logging

router = APIRouter()

logger = Utils.manageGlobalLogger(__name__)

#logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)

#fh = logging.FileHandler('greetingdto.log')
#fh.setLevel(logging.INFO)

#ch = logging.StreamHandler()
#ch.setLevel(logging.INFO)

#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#fh.setFormatter(formatter)
#ch.setFormatter(formatter)

#logger.addHandler(fh)
#logger.addHandler(ch)

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
