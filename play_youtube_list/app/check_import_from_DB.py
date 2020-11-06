import psycopg2
con = psycopg2.connect(
            host = "localhost",
            database="postgres",
            user = "postgres",
            password = "root")
# for users
cur = con.cursor()
cur.execute("select username, password from users")
userss = cur.fetchall()


print("////////////////////////////////////////////users///////////////////////////////////////////////////////")
for r in userss:
    print (f"username: {r[0]} &&  password: {r[1]}")


# for list of album songs
album_cur = con.cursor()
album_cur.execute("select name,source,category from album")
album_cur_list = album_cur.fetchall()

print("////////////////////////////////////////////videos///////////////////////////////////////////////////////")
for r in album_cur_list:
    print (f"name: {r[0]} &&  source: {r[1]}   && category: {r[2]}")
# for list of {message for admin}
message_cur = con.cursor()
message_cur.execute("select name_of_sender,subject_of_message,source_of_video from message_to_admin")
message_list = message_cur.fetchall()

print("////////////////////////////////////////////messages///////////////////////////////////////////////////////")
for r in message_list:
    print (f"name_of_sender: {r[0]} &&  subject_of_message: {r[1]}    && source_of_video :{r[2]}")

