from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import config, tasks

from app.api.routes import router as api_router


def get_application():
    app = FastAPI(title="Phresh", version="1.0.0")
    app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

    app.add_middleware(
        CORSMiddleware,
@@ -15,6 +17,9 @@ def get_application():
        allow_headers=["*"],
    )

    app.add_event_handler("startup", tasks.create_start_app_handler(app))
    app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))

    app.include_router(api_router, prefix="/api")

    return app
