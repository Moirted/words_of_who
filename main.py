from flask import *

from wow_back import wow_cheat

app = Flask(__name__, template_folder='./frontend/templates', static_folder='./frontend/static')


@app.route('/', methods=["GET", "POST"])
def hm_pg():
    if request.method == "POST":
        s_in = request.form.get("fins")
        return render_template("page_res.html", content=wow_cheat(s_in))
    return render_template("page_home.html")


if __name__ == '__main__':
    app.run()
