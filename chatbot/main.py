from fastapi import FastAPI
import uvicorn

from chatbot.routers.chat_response_routers import router as try_router

app = FastAPI()

app.include_router(try_router,prefix='/api')


if __name__ == "__main__":
    uvicorn.run(app="main:app",host='0.0.0.0',port=8000,reload=True)
