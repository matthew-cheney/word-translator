from fastapi import FastAPI

app = FastAPI(
    title="Word Translator",
    description="Translate words into English",
    version="1.0.0"
)

import routes  # This is not optional
