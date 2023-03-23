from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("flames_home.html")


def flames(name1, name2):
    # remove common characters
    for i in name1:
        if i in name2:
            name1 = name1.replace(i, "", 1)
            name2 = name2.replace(i, "", 1)
    # concatenate the remaining characters
    combined_string = name1 + name2
    # calculate the length of the combined string
    length = len(combined_string)
    # FLAMES game logic
    flames_list = ["Friends", "Lovers", "Affection", "Marriage", "Enemy", "Siblings"]
    while len(flames_list) > 1:
        split_index = (length % len(flames_list)) - 1
        if split_index >= 0:
            right = flames_list[split_index + 1:]
            left = flames_list[:split_index]
            flames_list = right + left
        else:
            flames_list = flames_list[:-1]
    return flames_list[0]


@app.route('/result', methods=['POST'])
def result():
    name1 = request.form['name1']
    name2 = request.form['name2']
    result_text = f"{name1} and {name2} are {flames(name1, name2)}!"
    return render_template('flames_result.html', result=result_text) # result variable is used in html


if __name__ == '__main__':
    app.run(debug=True)
