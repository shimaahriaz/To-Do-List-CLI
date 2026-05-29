from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    id: int
    title: str


blogs = [
    Blog(id=1, title="first blog"),
    Blog(id=2, title="second blog"),
    Blog(id=3, title="third blog"),
    Blog(id=4, title="fourth blog"),
]


@app.get("/blogs")
def get_blogs():
    return {"data": blogs}


@app.get("/blog/{id}")
def get_blog(id: int):
    for blog in blogs:
        if blog.id == id:
            return {"data": blog}

    raise HTTPException(
        status_code=404,
        detail="Blog not found"
    )


@app.post("/blog")
def create_blog(blog: Blog):
    blogs.append(blog)

    return {
        "message": "Blog created successfully",
        "data": blog
    }


@app.put("/blog/{id}")
def update_blog(id: int, updated_blog: Blog):

    for index, blog in enumerate(blogs):

        if blog.id == id:

            blogs[index] = updated_blog

            return {
                "message": "Blog updated successfully",
                "data": updated_blog
            }

    raise HTTPException(
        status_code=404,
        detail="Blog not found"
    )


@app.delete("/blog/{id}")
def delete_blog(id: int):

    for blog in blogs:

        if blog.id == id:

            blogs.remove(blog)

            return {
                "message": "Blog deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Blog not found"
    )