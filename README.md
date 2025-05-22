# Django Music Player

A fully functional music player web application built with Django. This project allows users to browse, search, and play songs, create playlists, and manage favorites with an intuitive and responsive interface.

---

## Features

- **User Authentication**  
  - User signup, login, and logout  

- **Song Management**  
  - Play songs with detailed metadata 

- **Responsive Design**  
  - Works seamlessly on desktops, tablets, and mobile devices  
  - Bootstrap-based styling for modern UI

- **Backend and Database**  
  - Built using the Django framework  
  - SQLite database for storing user data, songs, playlists, and favorites

---

## Tools

| Tool/Technology         | Purpose                                           |
|------------------------|-------------------------------------------------|
| Python 3.13             | Programming language for backend logic           |
| Django Framework       | Web framework for server-side application        |
| SQLite                 | Lightweight database                              |
| HTML/CSS/JavaScript    | Frontend structure, styling, and interactivity   |
| Bootstrap              | Responsive and modern UI design                   |
| Git                    | Version control                                   |
| Virtualenv             | Python environment isolation                      |

## Packages

1. Django==5.2.1
2. pillow==11.2.1
3. sqlparse==0.5.3

---

## Project Structure

```
| django-music-player/
│
├── manage.py                       # Django project management script
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
│
├── musicplayer/                    # Main Django project folder
│ ├── init.py
│ ├── settings.py                   # Project settings (database, installed apps, etc.)
│ ├── urls.py                       # Root URL routing
│ ├── wsgi.py                       # WSGI interface
│ └── asgi.py                       # ASGI interface (optional)
│
├── app/                            # Main Django app folder
│ ├── migrations/                   # Database migration files
│ ├── static/                       # Static files (CSS, JS, images)
│ │ └── app/                        # App-specific static assets
│ ├── templates/                    # HTML template files
│ │ └── app/                        # App-specific templates
│ ├── init.py
│ ├── admin.py                      # Admin site configurations
│ ├── apps.py                       # App configuration
│ ├── models.py                     # Database models (e.g., Song, Playlist)
│ ├── tests.py                      # Tests for the app
│ ├── urls.py                       # App URL routes
│ └── views.py                      # View functions and classes
│
├── media/                          # Uploaded media files (songs)
│
└── db.sqlite3                      # SQLite database file
```

---

## Steps of Using the Project

1. Clone the repository:
   ```sh
   https://github.com/RoshanSharma7/Python-Music-Player
   ```

2. Navigate the project directory:
   ```sh
   cd django-music-player
   ```

3. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Mac/Linux
    venv/Scripts/Activate     # On Windows
    ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Apply Mirations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the Server:
   ```sh
   python manage.py runserver
   ```

7. Open your browser and go to: http://127.0.0.1:8000

---

## Contributing:

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the project.
2. Create your feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

---

## Contact:

For questions or Support, Contact on
- **GitHub**: [RoshanSharma7](https://github.com/RoshanSharma7)
- **LinkedIn**: [RoshanSharma7](https://www.linkedin.com/in/roshan-sharma7)
- **Instagram**: [iamroshansharma7](https://www.instagram.com/iamroshansharma7/)
- **Email**: roshan.amlai96@gmail.com

---

## License:

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This README file is structured to give a comprehensive overview of the project, instructions for running it, and potential improvements.
