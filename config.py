import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "19397648"))
    API_HASH = os.environ.get("API_HASH", "19397648")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6332448525:AAHjBfaEDraU3EO0b5PhK7RpqZAChyueNZc")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1092802988")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQEn_BAAh77BS8xt5T31oO_UMosct0hpNI66oxhMziKOEhlGF5xO7cOI6rlScNRbHFGJZEiGA8d5kr-zeFu1DlTXQcvIlfr3ujS-yQem3p1dCAXoyJlk0Bgh8hSbZ3Dnr9R-fe0xmJ3bsYbpVzKO9mESRsi9LTF4wAOO7T1bPHC1agDPuCduVDjwYMQgAdUUiYCQeHeLvW4qQV9bDzgunmo8ZashiY6cwVSHd6kAL_W_EQiJtXEKyBT5Sf98MGlfupsjBne6wxsackU2QEfL0y-81IlpZsq8-6hVEbpoo7Vd1EcPtfru1fGhrVc5pBdB2iJWFeLvoAmkL8j6zvJx6AEpAhkzeAAAAAFPZqCbAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001670824726"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Test0383_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
