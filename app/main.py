from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

# IMPORT ROUTERS
from app.routes.user_routes import router as user_router
from app.routes.role_routes import router as role_router
from app.routes.student_routes import router as student_router
from app.routes.project_routes import router as project_router
from app.routes.project_user_routes import router as project_user_router
from app.routes.project_status_routes import router as status_router
from app.routes.project_status_history_routes import router as status_history_router
from app.routes.research_line_routes import router as research_line_router
from app.routes.research_group_routes import router as research_group_router
from app.routes.document_routes import router as document_router
from app.routes.document_type_routes import router as document_type_router
from app.routes.progress_routes import router as progress_router
from app.routes.comment_routes import router as comment_router
from app.routes.delivery_status_routes import router as delivery_status_router
from app.routes.scheduled_delivery_routes import router as delivery_router


from app.routes.faculty_router import router as faculty_router
from app.routes.program_router import router as program_router 
from app.routes.auth_router import router as auth_router 


# REGISTER ROUTERS
app.include_router(user_router, prefix="/api")
app.include_router(role_router, prefix="/api")
app.include_router(student_router, prefix="/api")
app.include_router(project_router, prefix="/api")
app.include_router(project_user_router, prefix="/api")
app.include_router(status_router, prefix="/api")
app.include_router(status_history_router, prefix="/api")
app.include_router(research_line_router, prefix="/api")
app.include_router(research_group_router, prefix="/api")
app.include_router(document_router, prefix="/api")
app.include_router(document_type_router, prefix="/api")
app.include_router(progress_router, prefix="/api")
app.include_router(comment_router, prefix="/api")
app.include_router(delivery_status_router, prefix="/api")
app.include_router(delivery_router, prefix="/api")


app.include_router(faculty_router, prefix="/api")
app.include_router(program_router, prefix="/api")  
app.include_router(auth_router, prefix="/api")

@app.get("/")
def home():
    return {"message": "API running"}