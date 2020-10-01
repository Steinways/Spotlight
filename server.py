from flask import Flask, request, jsonify

app = Flask(__name__)
import sqlite3
import time


@app.route('/')
def hello_world():
    return 'Hello, World!'


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/get_user/<user_id>', methods=['GET'])
def get_user(user_id):
    '''
    URL: /get_user/<user_id>
    Gets all information for a given USER_ID.
    '''

    # creates a connection
    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute("SELECT * FROM users_tbl WHERE user_id = ?", [user_id])
    result = c.fetchall()
    # close the connection

    conn.commit()
    conn.close()

    return jsonify(result)


@app.route('/create_user', methods=['POST'])
def create_user():
    '''
    URL: /create_user
    Posts an entry into users_tbl of user_id, photo_addr, username, and age.
    '''
    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    user_input = request.form['user_id']
    photo_input = request.form['photo_addr']
    username_input = request.form['username']
    age_input = request.form['age']
    c.execute('insert into users_tbl (user_id, photo_addr, username, age) values (?, ?, ?, ?)',
              (user_input, photo_input, username_input, age_input))
    conn.commit()
    conn.close()
    return ''


@app.route('/get_allvids/<channel_id>', methods=['GET'])
def get_allvids(channel_id):
    '''
    URL: /get_allVids/<channel_id>
    Gets all the video_ids for a given CHANNEL_ID.
    '''

    # creates a connection
    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute("SELECT video_id FROM vod_tbl WHERE channel_id = ?", [channel_id])
    result = c.fetchall()
    # close the connection

    conn.commit()
    conn.close()

    return jsonify(result)


@app.route('/post_video', methods=['POST'])
def post_video():
    '''
    URL: /post_video
    Posts a vod with current time (unix), category_id, channel_id, user_id, video_id, video_addr.
    '''

    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    user_input = request.form['user_id']
    video_input = request.form['video_id']
    video_addr = request.form['video_addr']
    category_id = request.form['category_id']
    channel_id = request.form['channel_id']
    c.execute('insert into vod_tbl (user_id, video_id, video_addr, date, category_id, channel_id) values (?, ?, ?, '
              '?, ?, ?)',
              (user_input, video_input, video_addr, time.time(), category_id, channel_id))
    conn.commit()
    conn.close()
    return ''


@app.route('/get_trendingtoday/', methods=['GET'])
def get_trendingtoday():
    '''
    URL: /get_trending
    Gets all the vods that are trending within the past 24 hours, descending order of likes.
    '''

    # creates a connection
    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    range = (time.time() - 86400)
    c.execute("SELECT * FROM vod_tbl WHERE date > ?", [range])
    result = c.fetchall()
    # close the connection

    conn.commit()
    conn.close()

    return jsonify(result)


@app.route('/get_trendingweek/', methods=['GET'])
def get_trendingweek():
    '''
    URL: /get_trendingweek
    Gets all the VIDEO_IDS that are trending within the past week, descending order of likes.
    '''

    # creates a connection
    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    range = (time.time() - (86400*7))
    c.execute("SELECT * FROM vod_tbl WHERE date > ?", [range])
    result = c.fetchall()
    # close the connection

    conn.commit()
    conn.close()

    return jsonify(result)


@app.route('/get_trendingmonth/', methods=['GET'])
def get_trendingmonth():
    '''
    URL: /get_trendingmonth
    Gets all the VIDEO_IDS that are trending within the past month, descending order of likes.
    '''

    # creates a connection
    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    range = (time.time() - (86400*7*30))
    c.execute("SELECT * FROM vod_tbl WHERE date > ?", [range])
    result = c.fetchall()
    # close the connection

    conn.commit()
    conn.close()

    return jsonify(result)


@app.route('/get_trendingyear/', methods=['GET'])
def get_trendingyear():
    '''
    URL: /get_trendingyear
    Gets all the VIDEO_IDS that are trending within the past year, descending order of likes.
    '''

    # creates a connection
    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    range = (time.time() - (86400*7*30*12))
    c.execute("SELECT * FROM vod_tbl WHERE date > ?", [range])
    result = c.fetchall()
    # close the connection

    conn.commit()
    conn.close()

    return jsonify(result)


@app.route('/get_trendingall/', methods=['GET'])
def get_trendingall():
    '''
    URL: /get_trendingall
    Gets all the VIDEO_IDS that are trending within all time, descending order of likes.
    '''

    # creates a connection
    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    range = 0
    c.execute("SELECT *, COUNT(*) FROM vod_tbl WHERE date > ?", [range])
    result = c.fetchall()
    # close the connection

    conn.commit()
    conn.close()

    return jsonify(result)


@app.route('/get_uservids/<user_id>', methods=['GET'])
def get_uservids(user_id):
    '''
    URL: /get_uservids/<user_id>
    Gets all the video_ids for a given USER_ID.
    '''

    # creates a connection
    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute("SELECT video_id FROM vod_tbl WHERE user_id = ?", [user_id])
    result = c.fetchall()
    # close the connection

    conn.commit()
    conn.close()

    return jsonify(result)


@app.route('/get_allcategories', methods=['GET'])
def get_allcategories():
    '''
    URL: /get_allcategories
    Gets all the category ids.
    '''

    # creates a connection
    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute("SELECT * FROM categories_tbl")
    result = c.fetchall()
    # close the connection

    conn.commit()
    conn.close()

    return jsonify(result)


@app.route('/get_pin/<user_id>', methods=['GET'])
def get_pin(user_id):
    '''
    URL: /get_pin/<user_id>/
    Gets all the pinned channels for a given USER_ID.
    '''

    # creates a connection
    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute("SELECT * FROM categories_tbl WHERE user_id = ?", [user_id])
    result = c.fetchall()
    # close the connection

    conn.commit()
    conn.close()

    return jsonify(result)


@app.route('/create_pin', methods=['POST'])
def create_pin():
    '''
    URL: /create_pin
    Posts an entry of a user's pinned channel into pin_tbl with user_id, channel_id.
    '''
    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    user_input = request.form['user_id']
    channel_input = request.form['channel_id']
    c.execute('insert into pin_tbl (user_id, channel_id) values (?, ?)',
              (user_input, channel_input))
    conn.commit()
    conn.close()
    return ''


@app.route('/get_allcategories', methods=['GET'])
def get_allchannels(category_id):
    '''
    URL: /get_allcategories/<category_id>
    Gets all the channel_ids for a given CATEGORY_ID.
    '''

    # creates a connection
    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute("SELECT * FROM channels_tbl WHERE category_id = ?", [category_id])
    result = c.fetchall()
    # close the connection

    conn.commit()
    conn.close()

    return jsonify(result)


@app.route('/like_video', methods=['POST'])
def like_video():
    '''
    URL: /like_video
    Given a user_id and like int, likes the video_id. '1' indicates like and '0' indicates no like.
    '''

    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    user_input = request.form['user_id']
    video_input = request.form['video_id']
    like_input = request.form['like']
    c.execute('insert into users_tbl (user_id, video_id, like) values (?, ?, ?)',
              (user_input, video_input, like_input))
    conn.commit()
    conn.close()
    return ''


@app.route('/like_count/<video_id>', methods=['GET'])
def like_count(video_id):
    '''
    URL: /like_count/<video_id>
    Returns the amount of likes on a given VIDEO_ID.
    '''

    conn = sqlite3.connect('spotlight.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    count = c.execute("COUNT(*) FROM likes_tbl WHERE like = 1 AND video_id = ?", [video_id])

    conn.commit()
    conn.close()
    return count
