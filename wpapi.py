import requests
import base64

class WordPressAPI:
    def __init__(self, base_url, admin_username, admin_password):
        self.base_url = base_url
        self.admin_username = admin_username
        self.admin_password = admin_password
        self.session = self.get_session()

    def get_session(self):
        session = requests.Session()
        credentials = f"{self.admin_username}:{self.admin_password}"
        credentials_encoded = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
        session.headers.update({"Authorization": f"Basic {credentials_encoded}"})
        return session

    
    def create_user(self, user_data):
        exists, user_id = self.username_exists(user_data["username"])
        if exists:
            print("The user already exists.")
            return user_id

        user_endpoint = f"{self.base_url}/wp-json/wp/v2/users"
        headers = {
            "Content-Type": "application/json"
        }

        response = self.session.post(user_endpoint, headers=headers, json=user_data)

        if response.status_code == 201:
            print("User created successfully!")
            return response.json()["id"]  # Return the user ID
        else:
            print(f"Failed to create user. Status code: {response.status_code}")
            print("Response content:", response.text)
            return None

    def username_exists(self, username):
        user_endpoint = f"{self.base_url}/wp-json/wp/v2/users"
        params = {"slug": username}
        response = self.session.get(user_endpoint, params=params)

        if response.status_code == 200:
            users = response.json()
            if users:
                return True, users[0]["id"]
            return False, None
        else:
            print(f"Failed to check username existence. Status code: {response.status_code}")
            print("Response content:", response.text)
            return False, None



    def create_post(self, post_title, post_content, media_location, user_data):
        media_data = self.upload_media(media_location)
        if media_data is None:
            return

        author_id = self.create_user(user_data)
        if author_id is None:
            print("Cannot create user.")
            return

        post_endpoint = f"{self.base_url}/wp-json/wp/v2/posts"
        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "title": post_title,
            "content": post_content,
            "status": "publish",
            "featured_media": media_data["id"],
            "author": author_id  # Use the user ID as the author
        }

        response = self.session.post(post_endpoint, headers=headers, json=data)

        if response.status_code == 201:
            print("Post created successfully!")
            return response.json()
        else:
            print(f"Failed to create post. Status code: {response.status_code}")
            print("Response content:", response.text)
            return None


    def upload_media(self, media_location):
        media_endpoint = f"{self.base_url}/wp-json/wp/v2/media"
        with open(media_location, "rb") as file:
            media_data = file.read()

        headers = {
            "Content-Disposition": f"attachment; filename={media_location.split('/')[-1]}",
            "Content-Type": "image/jpeg"
        }

        response = self.session.post(media_endpoint, headers=headers, data=media_data)

        if response.status_code == 201:
            print("Media uploaded successfully!")
            return response.json()
        else:
            print(f"Failed to upload media. Status code: {response.status_code}")
            print("Response content:", response.text)
            return None

    



#STANDALONE USAGE
base_url = "https://wordpress.site"
admin_username = "wp_admin"
admin_password = "wp_password"
post_title = "Title"
post_content = "This is the content of the new post."
media_location = "/path/image.jpg"
new_user_data = {
    "username": "jondoe",
    "email": "jondoe@example.com",  
    "password": "jondoepassword",
    "role": "author" #edit this
}




wp_api = WordPressAPI(base_url, admin_username, admin_password)
wp_api.create_post(post_title, post_content, media_location, new_user_data)
