from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# routers
from routes.user_routes import router as user_router
from routes.role_routes import router as role_router
from routes.project_status_routes import router as project_status_router
from routes.research_line_routes import router as research_line_router
from routes.document_type_routes import router as document_type_router
from routes.project_role_routes import router as project_role_router
from routes.delivery_status_routes import router as delivery_status_router
from routes.student_routes import router as student_router
from routes.project_routes import router as project_router
from routes.project_user_routes import router as project_user_router
from routes.document_routes import router as document_router
from routes.progress_routes import router as progress_router
from routes.comment_routes import router as comment_router
from routes.project_status_history_routes import router as project_status_history_router
from routes.scheduled_delivery_routes import router as scheduled_delivery_router

app = FastAPI()

origins = [
    "https://ep-square-flower-aiq3n3y4-pooler.c-4.us-east-1.aws.neon.tech",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
app.include_router(user_router, prefix="/api")
app.include_router(role_router, prefix="/api")
app.include_router(project_status_router, prefix="/api")
app.include_router(research_line_router, prefix="/api")
app.include_router(document_type_router, prefix="/api")
app.include_router(project_role_router, prefix="/api")
app.include_router(delivery_status_router, prefix="/api")
app.include_router(student_router, prefix="/api")
app.include_router(project_router, prefix="/api")
app.include_router(project_user_router, prefix="/api")
app.include_router(document_router, prefix="/api")
app.include_router(progress_router, prefix="/api")
app.include_router(comment_router, prefix="/api")
app.include_router(project_status_history_router, prefix="/api")
app.include_router(scheduled_delivery_router, prefix="/api")

@app.get("/")
def home():
    return {"message": "API running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)