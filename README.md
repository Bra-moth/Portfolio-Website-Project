#3498db;
            --dark: #2c3e50;
            --light: #f5f5f5;
            --accent: #e74c3c;
            --text: #333;
            --white: #ffffff;
            --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            --transition: all 0.3s ease;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--light);
            color: var(--text);
            line-height: 1.7;
            scroll-behavior: smooth;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        section {
            padding: 80px 0;
        }

        h1, h2, h3, h4 {
            margin-bottom: 20px;
            font-weight: 700;
            line-height: 1.3;
        }

        h1 { font-size: 2.8rem; }
        h2 { font-size: 2.2rem; }
        h3 { font-size: 1.8rem; }
        h4 { font-size: 1.4rem; }

        p {
            margin-bottom: 15px;
            font-size: 1.1rem;
        }

        a {
            text-decoration: none;
            color: inherit;
            transition: var(--transition);
        }

        .btn {
            display: inline-block;
            padding: 12px 30px;
            background-color: var(--primary);
            color: var(--white);
            border-radius: 50px;
            font-weight: 600;
            transition: var(--transition);
            border: none;
            cursor: pointer;
            box-shadow: var(--shadow);
        }

        .btn:hover {
            background-color: var(--dark);
            transform: translateY(-3px);
        }

        .btn-accent {
            background-color: var(--accent);
        }

        .section-title {
            text-align: center;
            margin-bottom: 50px;
            position: relative;
        }

        .section-title::after {
            content: '';
            display: block;
            width: 80px;
            height: 4px;
            background: var(--primary);
            margin: 20px auto;
            border-radius: 2px;
        }

        header {
            background-color: var(--dark);
            color: var(--white);
            padding: 20px 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            box-shadow: var(--shadow);
            transition: var(--transition);
        }

        header.scrolled {
            padding: 15px 0;
            background-color: rgba(44, 62, 80, 0.95);
        }

        .logo {
            display: flex;
            align-items: center;
            font-size: 1.5rem;
            font-weight: 700;
        }

        .logo-img {
            width: 40px;
            height: 40px;
            margin-right: 10px;
            border-radius: 50%;
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-links {
            display: flex;
            list-style: none;
        }

        .nav-links li {
            margin-left: 30px;
            position: relative;
        }

        .nav-links a {
            color: var(--white);
            font-weight: 500;
            padding: 5px 0;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0;
            height: 2px;
            background-color: var(--primary);
            transition: var(--transition);
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        .hamburger {
            display: none;
            cursor: pointer;
        }

        .hero {
            padding: 180px 0 100px;
            text-align: center;
            background: linear-gradient(135deg, var(--primary), #2c3e50);
            color: var(--white);
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1472&q=80') center/cover;
            opacity: 0.1;
        }

        .hero-content {
            position: relative;
            max-width: 800px;
            margin: 0 auto;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 20px;
            animation: fadeInDown 1s ease;
        }

        .hero p {
            font-size: 1.3rem;
            margin-bottom: 30px;
            animation: fadeInUp 1s ease;
        }

        .hero-btns {
            display: flex;
            justify-content: center;
            gap: 20px;
            animation: fadeIn 1.5s ease;
        }

        footer {
            background-color: var(--dark);
            color: var(--white);
            padding: 50px 0 20px;
            text-align: center;
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
        }

        .social-link {
            width: 50px;
            height: 50px;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.3rem;
            transition: var(--transition);
        }

        .social-link:hover {
            background-color: var(--primary);
            transform: translateY(-5px);
        }

        .copyright {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.7);
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @media (max-width: 768px) {
            .hamburger {
                display: block;
                z-index: 1001;
            }

            .nav-links {
                position: fixed;
                top: 0;
                right: -100%;
                width: 70%;
                height: 100vh;
                background-color: var(--dark);
                flex-direction: column;
                align-items: center;
                justify-content: center;
                transition: var(--transition);
                z-index: 1000;
            }

            .nav-links.active {
                right: 0;
            }

            .nav-links li {
                margin: 15px 0;
            }

            h1 { font-size: 2.2rem; }
            h2 { font-size: 1.8rem; }
            h3 { font-size: 1.5rem; }

            .hero {
                padding: 150px 0 80px;
            }

            .hero h1 {
                font-size: 2.5rem;
            }

            .hero p {
                font-size: 1.1rem;
            }

            .hero-btns {
                flex-direction: column;
                align-items: center;
            }

            section {
                padding: 60px 0;
            }
        }
    </style>
</head>
<body>
    <header id="header">
        <div class="container">
            <nav>
                <div class="logo">
                    <img src="https://via.placeholder.com/40" alt="Your Logo" class="logo-img">
                    <span>Your Name</span>
                </div>
                <ul class="nav-links">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#projects">Projects</a></li>
                    <li><a href="#resume">Resume</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
                <div class="hamburger">
                    <i class="fas fa-bars"></i>
                </div>
            </nav>
        </div>
    </header>

    <section class="hero" id="home">
        <div class="container">
            <div class="hero-content">
                <h1>Your Name</h1>
                <p>Your Tagline or Description</p>
                <div class="hero-btns">
                    <a href="#contact" class="btn">Get In Touch</a>
                    <a href="#projects" class="btn btn-accent">View My Work</a>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="social-links">
                <a href="#" target="_blank" class="social-link">
                    <i class="fab fa-facebook-f"></i>
                </a>
                <a href="#" target="_blank" class="social-link">
                    <i class="fab fa-twitter"></i>
                </a>
                <a href="#" target="_blank" class="social-link">
                    <i class="fab fa-linkedin-in"></i>
                </a>
                <a href="#" target="_blank" class="social-link">
                    <i class="fab fa-github"></i>
                </a>
            </div>
            <p class="copyright">&copy; 2025 Your Name. All rights reserved.</p>
        </div>
    </footer>

    <script>
        const hamburger = document.querySelector('.hamburger');
        const navLinks = document.querySelector('.nav-links');

        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.innerHTML = navLinks.classList.contains('active') 
                ? '<i class="fas fa-times"></i>' 
                : '<i class="fas fa-bars"></i>';
        });

        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                hamburger.innerHTML = '<i class="fas fa-bars"></i>';
            });
        });

        window.addEventListener('scroll', () => {
            const header = document.getElementById('header');
            if (window.scrollY > 100) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });

        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
    </script>
</body>
</html>