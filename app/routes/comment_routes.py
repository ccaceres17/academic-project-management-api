from fastapi import APIRouter
from controllers.comment_controller import CommentController
from models.comment_model import Comment

router = APIRouter()
controller = CommentController()

@router.post("/comments")
def create_comment(comment: Comment):
    return controller.create_comment(comment)