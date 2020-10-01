CREATE TABLE IF NOT EXISTS users_tbl (
    user_id TEXT,
    photo_addr TEXT,
    username TEXT,
    age int
);
CREATE TABLE IF NOT EXISTS vod_tbl (
    video_id TEXT,
    user_id TEXT,
    video_addr TEXT,
    category_id TEXT,
    channel_id TEXT,
    date int
);

CREATE TABLE IF NOT EXISTS likes_tbl (
    video_id TEXT,
    user_id TEXT,
    like int
);
CREATE TABLE IF NOT EXISTS channels_tbl (
    channel_id TEXT,
    category_id TEXT,
    name TEXT
);
CREATE TABLE IF NOT EXISTS categories_tbl (
    category_id TEXT
);
CREATE TABLE IF NOT EXISTS pin_tbl (
    user_id TEXT,
    channel_id TEXT
);
CREATE TABLE IF NOT EXISTS follower_tbl (
    user_id TEXT,
    follower_id TEXT
);
