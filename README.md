# Portfolio Website

A personal portfolio website built with Flask.

## Features

- Responsive design
- Home, About, Projects, and Contact sections
- Mobile navigation with hamburger menu
- Smooth scrolling and sticky navbar
- Social media links

## Project Structure

```
Portfolio Website Project/
├── app.py
├── .env
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes.py
│   ├── templates/
│   │   ├── index.html
│   │   └── includes/
│   │       ├── _header.html
│   │       └── _footer.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── script.js
```

## Setup Instructions

1. **Clone the repository**

   ```sh
   git clone <your-repo-url>
   cd "Portfolio Website Project"
   ```

2. **Create a virtual environment**

   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set environment variables**

   Create a `.env` file in the root directory:

   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ```

5. **Run the app**

   ```sh
   python app.py
   ```

6. **Visit**

   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Customization

- Edit `app/templates/index.html` and includes for your content.
- Update `app/static/css/style.css` for your styles.
- Add your projects and contact info in the appropriate sections.

## License

This project is licensed under the MIT License.