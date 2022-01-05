from flask import Flask, request, render_template, abort, send_from_directory
from functions import read_json, get_tags, get_posts_tag, add_post, replay_files_name

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)



@app.route("/")
def page_index():
    data = read_json(POST_PATH)
    tags = get_tags(data)
    return render_template('index.html', tags=tags)


@app.route("/tag")
def page_tag():
    tag = request.args.get('tag')
    if not tag:
        abort(400)
    data = read_json(POST_PATH)
    posts = get_posts_tag(data, tag)
    return render_template('post_by_tag.html', tag=tag, posts=posts)


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    if request.method == 'GET':
        return render_template('post_form.html')
    content = request.form.get('content')
    picture = request.files.get('picture')
    if not content or not picture:
        abort(400)
    picture.filename = replay_files_name(picture.filename)
    path = f'{UPLOAD_FOLDER}/{picture.filename}'
    post = {
        'content': content,
        'pic': f'/{path}'
    }
    picture.save(path)
    add_post(POST_PATH, post)


    return render_template("post_uploaded.html", post=post)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

@app.route("/all_posts")
def all_posts_():
    posts = read_json(POST_PATH)
    return render_template('all_posts.html', posts=posts)

app.run(debug=True)

