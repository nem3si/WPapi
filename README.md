<h1>WPapi - WordPress API Automation</h1>

<p>WPapi is a Python class that provides automation for interacting with the WordPress REST API using Basic Authentication. It allows you to create new users, upload media files, and create posts programmatically.</p>

<h2>Prerequisites</h2>

<p>To use WPapi, you need the following:</p>

<ul>
  <li>Python 3.x installed on your system</li>
  <li>Requests library (<code>requests</code>) for making HTTP requests</li>
  <li>Base64 library (<code>base64</code>) for encoding credentials</li>
</ul>


<h2>Getting Started</h2>

<ol>
  <li>Download or clone the <code>wpapi.py</code> file into your project directory.</li>
  <li>Import the <code>WordPressAPI</code> class into your Python script.</li>
</ol>

<pre><code>from wpapi import WordPressAPI</code></pre>

<ol start="3">
  <li>Create an instance of the <code>WordPressAPI</code> class by providing the base URL of your WordPress site and the admin username and password.</li>
</ol>

<pre><code>base_url = "https://your-wordpress-site.com"
admin_username = "your_admin_username"
admin_password = "your_admin_password"

wp_api = WordPressAPI(base_url, admin_username, admin_password)
</code></pre>

<h2>Usage</h2>

<h3>Creating a New User</h3>

<p>To create a new user in the WordPress system, use the <code>create_user</code> method and provide the user data as a dictionary with the following keys:</p>

<ul>
  <li><code>"username"</code>: The desired username for the new user.</li>
  <li><code>"email"</code>: The email address of the new user.</li>
  <li><code>"password"</code>: The password for the new user.</li>
  <li><code>"role"</code>: The role of the new user (e.g., "author", "editor", "administrator").</li>
</ul>

<pre><code>new_user_data = {
    "username": "new_user",
    "email": "new_user@example.com",
    "password": "password123",
    "role": "author"
}

user_id = wp_api.create_user(new_user_data);
</code></pre>

<h3>Uploading Media</h3>

<p>To upload a media file to the WordPress media library, use the <code>upload_media</code> method and provide the local file path of the media.</p>

<pre><code>media_location = "/path/to/your/media/file.jpg"

media_data = wp_api.upload_media(media_location);
</code></pre>

<h3>Creating a New Post</h3>

<p>To create a new post in the WordPress system, use the <code>create_post</code> method and provide the post title, content, media data (obtained from <code>upload_media</code>), and user data (obtained from <code>create_user</code>).</p>

<pre><code>post_title = "New Post Title"
post_content = "This is the content of the new post."

new_user_data = {
    "username": "author_user",
    "email": "author_user@example.com",
    "password": "author_password",
    "role": "author"
}

media_location = "/path/to/your/media/file.jpg"

media_data = wp_api.upload_media(media_location);

if media_data:
    wp_api.create_post(post_title, post_content, media_data, new_user_data);
</code></pre>

<h2>Error Handling</h2>

<p>WPapi provides basic error handling for cases such as invalid credentials, failed API requests, and existing users. It will print error messages with relevant information to help you troubleshoot any issues that may arise during automation.</p>

<h2>Standalone Usage</h2>

<p>You can also run WPapi as a standalone script to test its functionality. Simply update the <code>base_url</code>, <code>admin_username</code>, <code>admin_password</code>, <code>post_title</code>, <code>post_content</code>, <code>media_location</code>, and <code>new_user_data</code> variables with your desired values, and then run the script.</p>

<pre><code>base_url = "https://your-wordpress-site.com"
admin_username = "your_admin_username"
admin_password = "your_admin_password"
post_title = "New Post Title"
post_content = "This is the content of the new post."
media_location = "/path/to/your/media/file.jpg"

new_user_data = {
    "username": "new_user",
    "email": "new_user@example.com",
    "password": "password123",
    "role": "author"
}

wp_api = WordPressAPI(base_url, admin_username, admin_password)
wp_api.create_post(post_title, post_content, media_location, new_user_data)
</code></pre>
