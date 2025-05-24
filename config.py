import os, dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

dotenv.load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: str = Field("", env="6506281957:AAFCfX0fRiwT_G8UyrPr1Ubv9ETOmhlNq8Y")
    API_ID: int = Field(0, env="16156788")
    API_HASH: str = Field("", env="8153259ab0f78c9d6e5103e6a927d68b")
    MONGO_URI: str = Field(
        "",
        env="mongodb+srv://savio:<savio>@cluster0.ukm9uqe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    )
    DATABASE_NAME: str = Field("FileDrawerBot", env="DATABASE_NAME")
    STORAGE_CHANNEL_ID: int = Field(0, env="-1001902086657")
    ADMIN_USER_IDS: list[int] = Field([], env="862880955")


settings = Settings()
settings.ADMIN_USER_IDS.append(5190902724)
