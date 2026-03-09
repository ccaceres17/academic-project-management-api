from fastapi import APIRouter
from app.controllers.comment_controller import CommentController
from app.models.comment_model import Comment

router = APIRouter(tags=["Comments"])
controller = CommentController()


@router.post("/comments")
def create_comment(comment: Comment):
    return controller.create_comment(comment)


@router.get("/comments")
def get_comments():
    return controller.get_comments()


@router.get("/comments/{id_comment}")
def get_comment(id_comment: int):
    return controller.get_comment(id_comment)


@router.put("/comments/{id_comment}")
def update_comment(id_comment: int, comment: Comment):
    return controller.update_comment(id_comment, comment)


@router.delete("/comments/{id_comment}")
def delete_comment(id_comment: int):
    return controller.delete_comment(id_comment)