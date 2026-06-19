import sqlite3
from flask import Flask , render_template ,request ,flash ,redirect ,url_for ,session
from Database import get_db, init_db
app = Flask(__name__)
app.secret_key='linkkiwi2026' #needed for flashing message

QUESTIONS = [
    {
        "q": "Q1. What does HTML stand for?",
        "options": [
            "Hyper Text Markup Language",
            "High Text Machine Language",
            "Hyper Transfer Markup Language",
            "Home Tool Markup Language"
        ],
        "answer": "Hyper Text Markup Language"
    },
    {
        "q": "Q2. Which HTML tag is used to create a hyperlink?",
        "options": ["<a>", "<link>", "<href>", "<url>"],
        "answer": "<a>"
    },
    {
        "q": "Q3. Which CSS property is used to change text color?",
        "options": ["font-color", "color", "text-color", "background-color"],
        "answer": "color"
    },
    {
        "q": "Q4. Which CSS property is used to center text?",
        "options": ["text-align", "align-text", "font-align", "center"],
        "answer": "text-align"
    },
    {
        "q": "Q5. Which language is used to make websites interactive?",
        "options": ["HTML", "CSS", "JavaScript", "SQL"],
        "answer": "JavaScript"
    }
]

QUESTIONS1 = [
    {
        "q": "Q1. What does AI stand for?",
        "options": [
            "Artificial Intelligence",
            "Automatic Intelligence",
            "Advanced Internet",
            "Artificial Internet"
        ],
        "answer": "Artificial Intelligence"
    },
    {
        "q": "Q2. Which of the following is a branch of AI?",
        "options": [
            "Machine Learning",
            "Web Hosting",
            "Networking",
            "Cloud Storage"
        ],
        "answer": "Machine Learning"
    },
    {
        "q": "Q3. Which language is most commonly used in AI development?",
        "options": [
            "Python",
            "HTML",
            "CSS",
            "SQL"
        ],
        "answer": "Python"
    },
    {
        "q": "Q4. What is Machine Learning?",
        "options": [
            "A subset of AI",
            "A programming language",
            "A database",
            "A web browser"
        ],
        "answer": "A subset of AI"
    },
    {
        "q": "Q5. Which company developed ChatGPT?",
        "options": [
            "OpenAI",
            "Google",
            "Microsoft",
            "Amazon"
        ],
        "answer": "OpenAI"
    },
    {
        "q": "Q6. What is Deep Learning?",
        "options": [
            "An advanced form of Machine Learning",
            "A web technology",
            "A database system",
            "An operating system"
        ],
        "answer": "An advanced form of Machine Learning"
    },
    {
        "q": "Q7. Which of the following is an AI application?",
        "options": [
            "Chatbot",
            "Keyboard",
            "Monitor",
            "Printer"
        ],
        "answer": "Chatbot"
    },
    {
        "q": "Q8. Which AI technology is used for speech recognition?",
        "options": [
            "Natural Language Processing",
            "HTML",
            "CSS",
            "Bootstrap"
        ],
        "answer": "Natural Language Processing"
    },
    {
        "q": "Q9. Which of the following is a popular AI assistant?",
        "options": [
            "ChatGPT",
            "MS Paint",
            "Notepad",
            "Calculator"
        ],
        "answer": "ChatGPT"
    },
    {
        "q": "Q10. What is the main goal of Artificial Intelligence?",
        "options": [
            "To simulate human intelligence",
            "To replace electricity",
            "To create hardware only",
            "To increase internet speed"
        ],
        "answer": "To simulate human intelligence"
    }
]

QUESTIONS2 = [
    {
        "q": "Q1. What is Data Science?",
        "options": [
            "Study of data to gain insights",
            "Web Development",
            "Computer Networking",
            "Operating System"
        ],
        "answer": "Study of data to gain insights"
    },
    {
        "q": "Q2. Which language is most popular in Data Science?",
        "options": [
            "Python",
            "HTML",
            "CSS",
            "PHP"
        ],
        "answer": "Python"
    },
    {
        "q": "Q3. Which library is used for data analysis in Python?",
        "options": [
            "Pandas",
            "Bootstrap",
            "Flask",
            "Tkinter"
        ],
        "answer": "Pandas"
    },
    {
        "q": "Q4. Which library is used for numerical computing?",
        "options": [
            "NumPy",
            "Django",
            "OpenCV",
            "Requests"
        ],
        "answer": "NumPy"
    },
    {
        "q": "Q5. What is Data Visualization?",
        "options": [
            "Representing data graphically",
            "Writing code",
            "Creating databases",
            "Building websites"
        ],
        "answer": "Representing data graphically"
    },
    {
        "q": "Q6. Which library is commonly used for plotting graphs?",
        "options": [
            "Matplotlib",
            "BeautifulSoup",
            "Flask",
            "TensorFlow"
        ],
        "answer": "Matplotlib"
    },
    {
        "q": "Q7. What does CSV stand for?",
        "options": [
            "Comma Separated Values",
            "Computer System Values",
            "Code Storage Version",
            "Central Server Value"
        ],
        "answer": "Comma Separated Values"
    },
    {
        "q": "Q8. Which of the following is a Data Science process?",
        "options": [
            "Data Cleaning",
            "Page Styling",
            "Web Hosting",
            "App Installation"
        ],
        "answer": "Data Cleaning"
    },
    {
        "q": "Q9. Which field combines Data Science and AI?",
        "options": [
            "Machine Learning",
            "HTML",
            "CSS",
            "Bootstrap"
        ],
        "answer": "Machine Learning"
    },
    {
        "q": "Q10. What is the main goal of Data Science?",
        "options": [
            "Extract useful insights from data",
            "Create web pages",
            "Manage networks",
            "Design logos"
        ],
        "answer": "Extract useful insights from data"
    }
]

QUESTIONS3 = [
    {
        "q": "Q1. What is Cloud Computing?",
        "options": [
            "Delivering computing services over the Internet",
            "Building websites",
            "Creating databases",
            "Computer repair"
        ],
        "answer": "Delivering computing services over the Internet"
    },
    {
        "q": "Q2. Which of the following is a Cloud Service Provider?",
        "options": [
            "AWS",
            "HTML",
            "CSS",
            "Bootstrap"
        ],
        "answer": "AWS"
    },
    {
        "q": "Q3. What does AWS stand for?",
        "options": [
            "Amazon Web Services",
            "Advanced Web System",
            "Automatic Web Services",
            "Amazon World Server"
        ],
        "answer": "Amazon Web Services"
    },
    {
        "q": "Q4. Which cloud model provides virtual machines?",
        "options": [
            "IaaS",
            "SaaS",
            "PaaS",
            "DaaS"
        ],
        "answer": "IaaS"
    },
    {
        "q": "Q5. What does SaaS stand for?",
        "options": [
            "Software as a Service",
            "Storage as a Service",
            "Server as a Service",
            "System as a Service"
        ],
        "answer": "Software as a Service"
    },
    {
        "q": "Q6. Which of the following is a SaaS application?",
        "options": [
            "Google Docs",
            "Python",
            "Windows",
            "MySQL"
        ],
        "answer": "Google Docs"
    },
    {
        "q": "Q7. Which cloud deployment model is available to everyone?",
        "options": [
            "Public Cloud",
            "Private Cloud",
            "Hybrid Cloud",
            "Community Cloud"
        ],
        "answer": "Public Cloud"
    },
    {
        "q": "Q8. Which company provides Azure Cloud?",
        "options": [
            "Microsoft",
            "Google",
            "Amazon",
            "Oracle"
        ],
        "answer": "Microsoft"
    },
    {
        "q": "Q9. Which company provides Google Cloud Platform?",
        "options": [
            "Google",
            "Microsoft",
            "Amazon",
            "IBM"
        ],
        "answer": "Google"
    },
    {
        "q": "Q10. What is the main benefit of Cloud Computing?",
        "options": [
            "Scalability and flexibility",
            "Slower performance",
            "More hardware maintenance",
            "Limited access"
        ],
        "answer": "Scalability and flexibility"
    }
]

QUESTIONS4 = [
    {
        "q": "Q1. What is Cyber Security?",
        "options": [
            "Protecting systems and data from cyber attacks",
            "Creating websites",
            "Building databases",
            "Computer manufacturing"
        ],
        "answer": "Protecting systems and data from cyber attacks"
    },
    {
        "q": "Q2. What is a Virus?",
        "options": [
            "A malicious software",
            "A programming language",
            "A web browser",
            "A database"
        ],
        "answer": "A malicious software"
    },
    {
        "q": "Q3. Which of the following is used for secure web browsing?",
        "options": [
            "HTTPS",
            "HTTP",
            "FTP",
            "SMTP"
        ],
        "answer": "HTTPS"
    },
    {
        "q": "Q4. What does VPN stand for?",
        "options": [
            "Virtual Private Network",
            "Virtual Public Network",
            "Visual Private Node",
            "Verified Private Network"
        ],
        "answer": "Virtual Private Network"
    },
    {
        "q": "Q5. What is Phishing?",
        "options": [
            "A cyber attack to steal information",
            "A programming technique",
            "A cloud service",
            "A database operation"
        ],
        "answer": "A cyber attack to steal information"
    },
    {
        "q": "Q6. Which tool is commonly used to protect a network?",
        "options": [
            "Firewall",
            "Compiler",
            "Debugger",
            "Editor"
        ],
        "answer": "Firewall"
    },
    {
        "q": "Q7. What is a strong password?",
        "options": [
            "A mix of letters, numbers and symbols",
            "123456",
            "password",
            "abcdef"
        ],
        "answer": "A mix of letters, numbers and symbols"
    },
    {
        "q": "Q8. What does OTP stand for?",
        "options": [
            "One Time Password",
            "Only Text Password",
            "Online Test Password",
            "Open Time Password"
        ],
        "answer": "One Time Password"
    },
    {
        "q": "Q9. Which attack attempts to guess passwords automatically?",
        "options": [
            "Brute Force Attack",
            "SQL",
            "HTML",
            "Routing"
        ],
        "answer": "Brute Force Attack"
    },
    {
        "q": "Q10. What is the main goal of Cyber Security?",
        "options": [
            "Protect confidentiality, integrity and availability of data",
            "Increase internet speed",
            "Create websites",
            "Install software"
        ],
        "answer": "Protect confidentiality, integrity and availability of data"
    }
]

QUESTIONS5 = [
    {
        "q": "Q1. What is Mobile App Development?",
        "options": [
            "Creating applications for mobile devices",
            "Building computer hardware",
            "Managing databases",
            "Creating networks"
        ],
        "answer": "Creating applications for mobile devices"
    },
    {
        "q": "Q2. Which operating system is used by Android devices?",
        "options": [
            "Android",
            "iOS",
            "Windows",
            "Linux"
        ],
        "answer": "Android"
    },
    {
        "q": "Q3. Which company developed Android?",
        "options": [
            "Google",
            "Apple",
            "Microsoft",
            "Amazon"
        ],
        "answer": "Google"
    },
    {
        "q": "Q4. Which language is commonly used for Android development?",
        "options": [
            "Java",
            "HTML",
            "SQL",
            "PHP"
        ],
        "answer": "Java"
    },
    {
        "q": "Q5. Which language is officially recommended for Android development today?",
        "options": [
            "Kotlin",
            "C",
            "Python",
            "Ruby"
        ],
        "answer": "Kotlin"
    },
    {
        "q": "Q6. Which company developed iOS?",
        "options": [
            "Apple",
            "Google",
            "Microsoft",
            "IBM"
        ],
        "answer": "Apple"
    },
    {
        "q": "Q7. Which language is commonly used for iOS development?",
        "options": [
            "Swift",
            "Java",
            "PHP",
            "HTML"
        ],
        "answer": "Swift"
    },
    {
        "q": "Q8. What is Flutter?",
        "options": [
            "A cross-platform app development framework",
            "A database",
            "A web browser",
            "An operating system"
        ],
        "answer": "A cross-platform app development framework"
    },
    {
        "q": "Q9. Which company developed Flutter?",
        "options": [
            "Google",
            "Apple",
            "Microsoft",
            "Oracle"
        ],
        "answer": "Google"
    },
    {
        "q": "Q10. What is the main advantage of Flutter?",
        "options": [
            "One codebase for Android and iOS",
            "Requires two separate codebases",
            "Works only on Android",
            "Works only on iOS"
        ],
        "answer": "One codebase for Android and iOS"
    }
]

QUESTIONS_C = [
    {
        "q": "Q1. Who is known as the father of C language?",
        "options": [
            "Dennis Ritchie",
            "Bjarne Stroustrup",
            "James Gosling",
            "Guido van Rossum"
        ],
        "answer": "Dennis Ritchie"
    },
    {
        "q": "Q2. In which year was C language developed?",
        "options": [
            "1972",
            "1985",
            "1995",
            "2000"
        ],
        "answer": "1972"
    },
    {
        "q": "Q3. C language is mainly used for?",
        "options": [
            "System Programming",
            "Game Design",
            "Web Browsing",
            "Social Media"
        ],
        "answer": "System Programming"
    },
    {
        "q": "Q4. Which symbol is used to end a statement in C?",
        "options": [
            ";",
            ":",
            ".",
            "#"
        ],
        "answer": ";"
    },
    {
        "q": "Q5. Which header file is used for input/output in C?",
        "options": [
            "stdio.h",
            "conio.h",
            "string.h",
            "math.h"
        ],
        "answer": "stdio.h"
    },
    {
        "q": "Q6. Which function is used to print output in C?",
        "options": [
            "printf()",
            "print()",
            "cout",
            "echo"
        ],
        "answer": "printf()"
    },
    {
        "q": "Q7. Which function is used to take input in C?",
        "options": [
            "scanf()",
            "input()",
            "get()",
            "read()"
        ],
        "answer": "scanf()"
    },
    {
        "q": "Q8. C language is a?",
        "options": [
            "Procedural language",
            "Object Oriented language",
            "Machine language",
            "Markup language"
        ],
        "answer": "Procedural language"
    },
    {
        "q": "Q9. Which operator is used for pointer in C?",
        "options": [
            "*",
            "&",
            "#",
            "@"
        ],
        "answer": "*"
    },
    {
        "q": "Q10. C language was developed at?",
        "options": [
            "AT&T Bell Labs",
            "Google",
            "Microsoft",
            "Apple"
        ],
        "answer": "AT&T Bell Labs"
    }
]

QUESTIONS_CPP = [
    {
        "q": "Q1. Who developed C++ language?",
        "options": [
            "Bjarne Stroustrup",
            "Dennis Ritchie",
            "James Gosling",
            "Guido van Rossum"
        ],
        "answer": "Bjarne Stroustrup"
    },
    {
        "q": "Q2. C++ is an extension of which language?",
        "options": [
            "C",
            "Java",
            "Python",
            "Assembly"
        ],
        "answer": "C"
    },
    {
        "q": "Q3. Which concept is NOT supported by C++?",
        "options": [
            "Encapsulation",
            "Inheritance",
            "Polymorphism",
            "HTML Programming"
        ],
        "answer": "HTML Programming"
    },
    {
        "q": "Q4. Which symbol is used for scope resolution in C++?",
        "options": [
            "::",
            "##",
            "**",
            "//"
        ],
        "answer": "::"
    },
    {
        "q": "Q5. C++ supports which programming style?",
        "options": [
            "Both procedural and object-oriented",
            "Only procedural",
            "Only object-oriented",
            "Only functional"
        ],
        "answer": "Both procedural and object-oriented"
    },
    {
        "q": "Q6. Which keyword is used to create a class in C++?",
        "options": [
            "class",
            "struct",
            "object",
            "define"
        ],
        "answer": "class"
    },
    {
        "q": "Q7. What is the extension of C++ file?",
        "options": [
            ".cpp",
            ".c",
            ".java",
            ".py"
        ],
        "answer": ".cpp"
    },
    {
        "q": "Q8. Which operator is used for dynamic memory allocation in C++?",
        "options": [
            "new",
            "malloc",
            "alloc",
            "create"
        ],
        "answer": "new"
    },
    {
        "q": "Q9. Which is a constructor feature in C++?",
        "options": [
            "Same name as class",
            "Has return type",
            "Used for deletion",
            "Always static"
        ],
        "answer": "Same name as class"
    },
    {
        "q": "Q10. Which feature improves code reuse in C++?",
        "options": [
            "Inheritance",
            "Looping",
            "Arrays",
            "Macros"
        ],
        "answer": "Inheritance"
    }
]

QUESTIONS_JAVA = [
    {
        "q": "Q1. Who developed Java programming language?",
        "options": [
            "James Gosling",
            "Dennis Ritchie",
            "Bjarne Stroustrup",
            "Guido van Rossum"
        ],
        "answer": "James Gosling"
    },
    {
        "q": "Q2. Java was developed at which company?",
        "options": [
            "Sun Microsystems",
            "Microsoft",
            "Google",
            "Apple"
        ],
        "answer": "Sun Microsystems"
    },
    {
        "q": "Q3. What is Java primarily known for?",
        "options": [
            "Platform independence",
            "Hardware control",
            "Low-level programming",
            "Markup language"
        ],
        "answer": "Platform independence"
    },
    {
        "q": "Q4. Which keyword is used to create a class in Java?",
        "options": [
            "class",
            "struct",
            "define",
            "object"
        ],
        "answer": "class"
    },
    {
        "q": "Q5. Which method is the entry point of Java program?",
        "options": [
            "main()",
            "start()",
            "run()",
            "init()"
        ],
        "answer": "main()"
    },
    {
        "q": "Q6. Java is which type of language?",
        "options": [
            "Object-Oriented",
            "Procedural",
            "Assembly",
            "Markup"
        ],
        "answer": "Object-Oriented"
    },
    {
        "q": "Q7. Which extension is used for Java files?",
        "options": [
            ".java",
            ".class",
            ".js",
            ".py"
        ],
        "answer": ".java"
    },
    {
        "q": "Q8. Java code is compiled into?",
        "options": [
            "Bytecode",
            "Machine code",
            "Source code",
            "HTML"
        ],
        "answer": "Bytecode"
    },
    {
        "q": "Q9. Which JVM stands for?",
        "options": [
            "Java Virtual Machine",
            "Java Verified Model",
            "Joint Virtual Module",
            "Java Variable Method"
        ],
        "answer": "Java Virtual Machine"
    },
    {
        "q": "Q10. Which feature makes Java secure?",
        "options": [
            "No pointers",
            "Manual memory control",
            "Direct hardware access",
            "Assembly level coding"
        ],
        "answer": "No pointers"
    }
]

QUESTIONS_PYTHON = [
    {
        "q": "Q1. Who developed Python language?",
        "options": [
            "Guido van Rossum",
            "Dennis Ritchie",
            "James Gosling",
            "Bjarne Stroustrup"
        ],
        "answer": "Guido van Rossum"
    },
    {
        "q": "Q2. Python is which type of language?",
        "options": [
            "Interpreted language",
            "Compiled language",
            "Machine language",
            "Assembly language"
        ],
        "answer": "Interpreted language"
    },
    {
        "q": "Q3. Which symbol is used for comments in Python?",
        "options": [
            "#",
            "//",
            "/* */",
            "<!-- -->"
        ],
        "answer": "#"
    },
    {
        "q": "Q4. Which of the following is a Python data type?",
        "options": [
            "List",
            "ArrayList",
            "Vector",
            "TupleList"
        ],
        "answer": "List"
    },
    {
        "q": "Q5. Which keyword is used to define a function in Python?",
        "options": [
            "def",
            "function",
            "define",
            "fun"
        ],
        "answer": "def"
    },
    {
        "q": "Q6. Which extension is used for Python files?",
        "options": [
            ".py",
            ".java",
            ".cpp",
            ".pyt"
        ],
        "answer": ".py"
    },
    {
        "q": "Q7. Which of the following is a Python framework?",
        "options": [
            "Django",
            "Laravel",
            "Spring",
            "React"
        ],
        "answer": "Django"
    },
    {
        "q": "Q8. Python is mainly used for?",
        "options": [
            "Web development, AI, Data Science",
            "Only game development",
            "Only mobile apps",
            "Only database management"
        ],
        "answer": "Web development, AI, Data Science"
    },
    {
        "q": "Q9. Which function is used to print output in Python?",
        "options": [
            "print()",
            "echo()",
            "cout",
            "printf()"
        ],
        "answer": "print()"
    },
    {
        "q": "Q10. Python supports which programming style?",
        "options": [
            "Object-Oriented and Procedural",
            "Only procedural",
            "Only functional",
            "Only machine level"
        ],
        "answer": "Object-Oriented and Procedural"
    }
]

QUESTIONS_OS = [
    {
        "q": "Q1. What is an Operating System?",
        "options": [
            "System software that manages hardware and software",
            "A programming language",
            "A web browser",
            "A database system"
        ],
        "answer": "System software that manages hardware and software"
    },
    {
        "q": "Q2. Which of the following is an Operating System?",
        "options": [
            "Windows",
            "Java",
            "HTML",
            "MySQL"
        ],
        "answer": "Windows"
    },
    {
        "q": "Q3. Which OS is open source?",
        "options": [
            "Linux",
            "Windows",
            "macOS",
            "iOS"
        ],
        "answer": "Linux"
    },
    {
        "q": "Q4. What is the main function of an OS?",
        "options": [
            "Memory and process management",
            "Writing programs",
            "Designing websites",
            "Creating databases"
        ],
        "answer": "Memory and process management"
    },
    {
        "q": "Q5. Which OS is used in Android phones?",
        "options": [
            "Linux-based OS",
            "Windows",
            "macOS",
            "DOS"
        ],
        "answer": "Linux-based OS"
    },
    {
        "q": "Q6. Which component manages CPU scheduling?",
        "options": [
            "Operating System",
            "Compiler",
            "Browser",
            "Assembler"
        ],
        "answer": "Operating System"
    },
    {
        "q": "Q7. What is multitasking in OS?",
        "options": [
            "Running multiple tasks at the same time",
            "Using one program only",
            "Deleting files",
            "Installing software"
        ],
        "answer": "Running multiple tasks at the same time"
    },
    {
        "q": "Q8. Which of these is NOT an OS?",
        "options": [
            "Oracle",
            "Windows",
            "Linux",
            "Unix"
        ],
        "answer": "Oracle"
    },
    {
        "q": "Q9. What does kernel do in OS?",
        "options": [
            "Core part of OS managing system resources",
            "Designing UI",
            "Running browser",
            "Compiling code"
        ],
        "answer": "Core part of OS managing system resources"
    },
    {
        "q": "Q10. Which OS is developed by Microsoft?",
        "options": [
            "Windows",
            "Linux",
            "Ubuntu",
            "Android"
        ],
        "answer": "Windows"
    }
]

QUESTIONS_DBMS = [
    {
        "q": "Q1. What is DBMS?",
        "options": [
            "Software to manage and store data",
            "Programming language",
            "Operating system",
            "Web browser"
        ],
        "answer": "Software to manage and store data"
    },
    {
        "q": "Q2. Which of the following is a DBMS?",
        "options": [
            "MySQL",
            "Java",
            "Linux",
            "HTML"
        ],
        "answer": "MySQL"
    },
    {
        "q": "Q3. What is the full form of SQL?",
        "options": [
            "Structured Query Language",
            "Simple Query Language",
            "Sequential Query Language",
            "Standard Question Language"
        ],
        "answer": "Structured Query Language"
    },
    {
        "q": "Q4. Which command is used to retrieve data in SQL?",
        "options": [
            "SELECT",
            "INSERT",
            "UPDATE",
            "DELETE"
        ],
        "answer": "SELECT"
    },
    {
        "q": "Q5. What is a primary key?",
        "options": [
            "Uniquely identifies a record in a table",
            "Duplicates values allowed",
            "Used for styling tables",
            "A type of query"
        ],
        "answer": "Uniquely identifies a record in a table"
    },
    {
        "q": "Q6. Which of the following is a relational database?",
        "options": [
            "MySQL",
            "MongoDB",
            "Redis",
            "Firebase"
        ],
        "answer": "MySQL"
    },
    {
        "q": "Q7. What is normalization in DBMS?",
        "options": [
            "Process of organizing data to reduce redundancy",
            "Deleting database",
            "Encrypting data",
            "Creating backup"
        ],
        "answer": "Process of organizing data to reduce redundancy"
    },
    {
        "q": "Q8. Which language is used to manipulate data in DBMS?",
        "options": [
            "DML",
            "DDL",
            "HTML",
            "XML"
        ],
        "answer": "DML"
    },
    {
        "q": "Q9. Which of the following is NOT a DBMS?",
        "options": [
            "Python",
            "Oracle",
            "MySQL",
            "MongoDB"
        ],
        "answer": "Python"
    },
    {
        "q": "Q10. What does DBMS stand for?",
        "options": [
            "Database Management System",
            "Data Backup Management System",
            "Digital Base Management Software",
            "Database Memory System"
        ],
        "answer": "Database Management System"
    }
]

QUESTIONS_CN = [
    {
        "q": "Q1. What is a computer network?",
        "options": [
            "A system of connected computers to share data",
            "A type of software",
            "A programming language",
            "A database system"
        ],
        "answer": "A system of connected computers to share data"
    },
    {
        "q": "Q2. What does LAN stand for?",
        "options": [
            "Local Area Network",
            "Large Area Network",
            "Light Access Network",
            "Logical Area Network"
        ],
        "answer": "Local Area Network"
    },
    {
        "q": "Q3. Which device is used to connect different networks?",
        "options": [
            "Router",
            "Keyboard",
            "Monitor",
            "Printer"
        ],
        "answer": "Router"
    },
    {
        "q": "Q4. What does IP stand for?",
        "options": [
            "Internet Protocol",
            "Internal Process",
            "Interface Program",
            "Internet Provider"
        ],
        "answer": "Internet Protocol"
    },
    {
        "q": "Q5. Which topology has a central hub?",
        "options": [
            "Star topology",
            "Bus topology",
            "Ring topology",
            "Mesh topology"
        ],
        "answer": "Star topology"
    },
    {
        "q": "Q6. Which device filters network traffic?",
        "options": [
            "Firewall",
            "Monitor",
            "Keyboard",
            "Scanner"
        ],
        "answer": "Firewall"
    },
    {
        "q": "Q7. What is the full form of WAN?",
        "options": [
            "Wide Area Network",
            "Wireless Access Network",
            "World Area Node",
            "Web Area Network"
        ],
        "answer": "Wide Area Network"
    },
    {
        "q": "Q8. Which protocol is used for web browsing?",
        "options": [
            "HTTP",
            "FTP",
            "SMTP",
            "TCP"
        ],
        "answer": "HTTP"
    },
    {
        "q": "Q9. What is the main function of a router?",
        "options": [
            "To forward data packets between networks",
            "To store files",
            "To display output",
            "To write programs"
        ],
        "answer": "To forward data packets between networks"
    },
    {
        "q": "Q10. Which layer of OSI model handles routing?",
        "options": [
            "Network layer",
            "Physical layer",
            "Application layer",
            "Data link layer"
        ],
        "answer": "Network layer"
    }
]

QUESTIONS_DS = [
    {
        "q": "Q1. What is a data structure?",
        "options": [
            "A way to organize and store data",
            "A programming language",
            "An operating system",
            "A database software"
        ],
        "answer": "A way to organize and store data"
    },
    {
        "q": "Q2. Which data structure follows LIFO principle?",
        "options": [
            "Stack",
            "Queue",
            "Array",
            "Tree"
        ],
        "answer": "Stack"
    },
    {
        "q": "Q3. Which data structure follows FIFO principle?",
        "options": [
            "Queue",
            "Stack",
            "Graph",
            "Heap"
        ],
        "answer": "Queue"
    },
    {
        "q": "Q4. What is an array?",
        "options": [
            "A collection of similar data elements",
            "A type of database",
            "A network device",
            "An operating system"
        ],
        "answer": "A collection of similar data elements"
    },
    {
        "q": "Q5. Which data structure uses nodes and pointers?",
        "options": [
            "Linked List",
            "Array",
            "Stack",
            "Queue"
        ],
        "answer": "Linked List"
    }
]

stud = [
    {
        'Sr_no':1,
        'Name':'John Doe',
        'username':'John',
        'email':'John@gmail.com',
        'password':'John@1234'
    },
    {
        'Sr_no':2,
        'Name':'Jane smith',
        'username':'Jone',
        'email':'Jane@gmail.com',
        'password':'Jone@1234'
    }
]

@app.route('/')
def Home():
        return render_template('Home.html',students=stud)
    
'''@app.route('/start')
def start():
        session["score"] = 0
        return redirect(url_for("web_development", qno=0))'''
    
    

@app.route('/login', methods=['GET', 'POST'])
def login():

     if request.method == 'POST':

         username = request.form.get('username')
         password = request.form.get('password')
         if username == '' or password == '':
             flash("Please provide all information!")
             return render_template('login.html')

         flash("Login Successfully!")
         return redirect(url_for('technology'))

     return render_template('login.html')




@app.route('/explore_technology')
def explore_technology():

    if 'sr_no' in session:
        return redirect(url_for('technology'))

    flash('Please Login or Register First!')
    return redirect(url_for('login'))


@app.route('/technology')
def technology():
    return render_template('technology.html')

@app.route('/web_development/<int:qno>', methods=['GET', 'POST'])
def web_development(qno):

    if "score" not in session:
        session["score"] = 0

    # POST (answer submit)
    if request.method == "POST":

        selected = request.form.get("answer")

        # save answer in session per question
        session[f"q{qno}"] = selected

        # NEXT button
        if "next" in request.form and qno < len(QUESTIONS) - 1:
            return redirect(url_for("web_development", qno=qno+1))

        # PREVIOUS button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("web_development", qno=qno-1))

        # SUBMIT button
        if "submit" in request.form:
            score = 0

            for i in range(len(QUESTIONS)):
                if session.get(f"q{i}") == QUESTIONS[i]["answer"]:
                    score += 1

            session["score"] = score
            return redirect(url_for("Result"))

    return render_template(
        "web_development.html",
        question=QUESTIONS[qno],
        qno=qno,
        total=len(QUESTIONS)
    )


@app.route('/Artificial_Intelligence/<int:qno>', methods=['GET', 'POST'])
def Artificial_Intelligence(qno):

    if "score" not in session:
        session["score"] = 0

    # POST (answer submit)
    if request.method == "POST":

        selected = request.form.get("answer")

        # save answer in session per question
        session[f"q{qno}"] = selected

        # NEXT button
        if "next" in request.form and qno < len(QUESTIONS1) - 1:
            return redirect(url_for("Artificial_Intelligence", qno=qno+1))

        # PREVIOUS button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("Artificial_Intelligence", qno=qno-1))

        # SUBMIT button
        if "submit" in request.form:
            score = 0

            for i in range(len(QUESTIONS1)):
                if session.get(f"q{i}") == QUESTIONS1[i]["answer"]:
                    score += 1

            session["score"] = score
            return redirect(url_for("Result"))

    return render_template(
        "Artificial_Intelligence.html",
        question=QUESTIONS1[qno],
        qno=qno,
        total=len(QUESTIONS1)
    )

@app.route('/Data_Science/<int:qno>', methods=['GET', 'POST'])
def Data_Science(qno):

    if "score" not in session:
        session["score"] = 0

    # POST (answer submit)
    if request.method == "POST":

        selected = request.form.get("answer")

        # save answer in session per question
        session[f"q{qno}"] = selected

        # NEXT button
        if "next" in request.form and qno < len(QUESTIONS2) - 1:
            return redirect(url_for("Data_Science", qno=qno+1))

        # PREVIOUS button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("Data_Science", qno=qno-1))

        # SUBMIT button
        if "submit" in request.form:
            score = 0

            for i in range(len(QUESTIONS2)):
                if session.get(f"q{i}") == QUESTIONS2[i]["answer"]:
                    score += 1

            session["score"] = score
            return redirect(url_for("Result"))

    return render_template(
        "Data_Science.html",
        question=QUESTIONS2[qno],
        qno=qno,
        total=len(QUESTIONS2)
    )

@app.route('/Cloud_Computing/<int:qno>', methods=['GET', 'POST'])
def Cloud_Computing(qno):

    if "score" not in session:
        session["score"] = 0

    # POST (answer submit)
    if request.method == "POST":

        selected = request.form.get("answer")

        # save answer in session per question
        session[f"q{qno}"] = selected

        # NEXT button
        if "next" in request.form and qno < len(QUESTIONS3) - 1:
            return redirect(url_for("Cloud_Computing", qno=qno+1))

        # PREVIOUS button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("Cloud_Computing", qno=qno-1))

        # SUBMIT button
        if "submit" in request.form:
            score = 0

            for i in range(len(QUESTIONS3)):
                if session.get(f"q{i}") == QUESTIONS3[i]["answer"]:
                    score += 1

            session["score"] = score
            return redirect(url_for("Result"))

    return render_template(
        "Cloud_Computing.html",
        question=QUESTIONS3[qno],
        qno=qno,
        total=len(QUESTIONS3)
    )

@app.route('/Cyber_Security/<int:qno>', methods=['GET', 'POST'])
def Cyber_Security(qno):

    if "score" not in session:
        session["score"] = 0

    # POST (answer submit)
    if request.method == "POST":

        selected = request.form.get("answer")

        # save answer in session per question
        session[f"q{qno}"] = selected

        # NEXT button
        if "next" in request.form and qno < len(QUESTIONS4) - 1:
            return redirect(url_for("Cyber_Security", qno=qno+1))

        # PREVIOUS button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("Cyber_Security", qno=qno-1))

        # SUBMIT button
        if "submit" in request.form:
            score = 0

            for i in range(len(QUESTIONS4)):
                if session.get(f"q{i}") == QUESTIONS4[i]["answer"]:
                    score += 1

            session["score"] = score
            return redirect(url_for("Result"))

    return render_template(
        "Cyber_Security.html",
        question=QUESTIONS4[qno],
        qno=qno,
        total=len(QUESTIONS4)
    )

@app.route('/Mobile_App_Development/<int:qno>', methods=['GET', 'POST'])
def Mobile_App_Development(qno):

    if "score" not in session:
        session["score"] = 0

    # POST (answer submit)
    if request.method == "POST":

        selected = request.form.get("answer")

        # save answer in session per question
        session[f"q{qno}"] = selected

        # NEXT button
        if "next" in request.form and qno < len(QUESTIONS5) - 1:
            return redirect(url_for("Mobile_App_Development", qno=qno+1))

        # PREVIOUS button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("Mobile_App_Development", qno=qno-1))

        # SUBMIT button
        if "submit" in request.form:
            score = 0

            for i in range(len(QUESTIONS5)):
                if session.get(f"q{i}") == QUESTIONS5[i]["answer"]:
                    score += 1

            session["score"] = score
            return redirect(url_for("Result"))

    return render_template(
        "Mobile_App_Development.html",
        question=QUESTIONS5[qno],
        qno=qno,
        total=len(QUESTIONS5)
    )


@app.route('/explore_programing_lang')
def explore_programing_lang():

    if 'sr_no' in session:
        return redirect(url_for('programing_lang'))

    flash('Please Login or Register First!')
    return redirect(url_for('login'))

@app.route('/programing_lang')
def programing_lang():
    return render_template('programing_lang.html')

@app.route('/c_lang/<int:qno>', methods=['GET', 'POST'])
def c_lang(qno):

    if "score" not in session:
        session["score"] = 0

    # POST (answer submit)
    if request.method == "POST":

        selected = request.form.get("answer")

        # save answer in session per question
        session[f"q{qno}"] = selected

        # NEXT button
        if "next" in request.form and qno < len(QUESTIONS_C) - 1:
            return redirect(url_for("c_lang", qno=qno+1))

        # PREVIOUS button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("c_lang", qno=qno-1))

        # SUBMIT button
        if "submit" in request.form:
            score = 0

            for i in range(len(QUESTIONS_C)):
                if session.get(f"q{i}") == QUESTIONS_C[i]["answer"]:
                    score += 1

            session["score"] = score
            return redirect(url_for("Result"))

    return render_template(
        "c_lang.html",
        question=QUESTIONS_C[qno],
        qno=qno,
        total=len(QUESTIONS_C)
    )

@app.route('/cpp_lang/<int:qno>', methods=['GET', 'POST'])
def cpp_lang(qno):

    if "score" not in session:
        session["score"] = 0

    # POST (answer submit)
    if request.method == "POST":

        selected = request.form.get("answer")

        # save answer in session per question
        session[f"q{qno}"] = selected

        # NEXT button
        if "next" in request.form and qno < len(QUESTIONS_CPP) - 1:
            return redirect(url_for("cpp_lang", qno=qno+1))

        # PREVIOUS button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("cpp_lang", qno=qno-1))

        # SUBMIT button
        if "submit" in request.form:
            score = 0

            for i in range(len(QUESTIONS_CPP)):
                if session.get(f"q{i}") == QUESTIONS_CPP[i]["answer"]:
                    score += 1

            session["score"] = score
            return redirect(url_for("Result"))

    return render_template(
        "cpp_lang.html",
        question=QUESTIONS_CPP[qno],
        qno=qno,
        total=len(QUESTIONS_CPP)
    )

@app.route('/java_lang/<int:qno>', methods=['GET', 'POST'])
def java_lang(qno):

    if "score" not in session:
        session["score"] = 0

    # POST (answer submit)
    if request.method == "POST":

        selected = request.form.get("answer")

        # save answer in session per question
        session[f"q{qno}"] = selected

        # NEXT button
        if "next" in request.form and qno < len(QUESTIONS_JAVA) - 1:
            return redirect(url_for("java_lang", qno=qno+1))

        # PREVIOUS button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("java_lang", qno=qno-1))

        # SUBMIT button
        if "submit" in request.form:
            score = 0

            for i in range(len(QUESTIONS_JAVA)):
                if session.get(f"q{i}") == QUESTIONS_JAVA[i]["answer"]:
                    score += 1

            session["score"] = score
            return redirect(url_for("Result"))

    return render_template(
        "java_lang.html",
        question=QUESTIONS_JAVA[qno],
        qno=qno,
        total=len(QUESTIONS_JAVA)
    )

@app.route('/python_lang/<int:qno>', methods=['GET', 'POST'])
def python_lang(qno):

    if "score" not in session:
        session["score"] = 0

    # POST (answer submit)
    if request.method == "POST":

        selected = request.form.get("answer")

        # save answer in session per question
        session[f"q{qno}"] = selected

        # NEXT button
        if "next" in request.form and qno < len(QUESTIONS_PYTHON) - 1:
            return redirect(url_for("python_lang", qno=qno+1))

        # PREVIOUS button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("python_lang", qno=qno-1))

        # SUBMIT button
        if "submit" in request.form:
            score = 0

            for i in range(len(QUESTIONS_PYTHON)):
                if session.get(f"q{i}") == QUESTIONS_PYTHON[i]["answer"]:
                    score += 1

            session["score"] = score
            return redirect(url_for("Result"))

    return render_template(
        "python_lang.html",
        question=QUESTIONS_PYTHON[qno],
        qno=qno,
        total=len(QUESTIONS_PYTHON)
    )



@app.route('/explore_computer_science')
def explore_computer_science():

    if 'sr_no' in session:
        return redirect(url_for('computer_science'))

    flash('Please Login or Register First!')
    return redirect(url_for('login'))

@app.route('/computer_science')
def computer_science():
    return render_template('computer_science.html')


@app.route('/operating_system/<int:qno>', methods=['GET', 'POST'])
def operating_system(qno):

    if "score" not in session:
        session["score"] = 0

    # POST (answer submit)
    if request.method == "POST":

        selected = request.form.get("answer")

        # save answer in session per question
        session[f"q{qno}"] = selected

        # NEXT button
        if "next" in request.form and qno < len(QUESTIONS_OS) - 1:
            return redirect(url_for("operating_system", qno=qno+1))

        # PREVIOUS button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("operating_system", qno=qno-1))

        # SUBMIT button
        if "submit" in request.form:
            score = 0

            for i in range(len(QUESTIONS_OS)):
                if session.get(f"q{i}") == QUESTIONS_OS[i]["answer"]:
                    score += 1

            session["score"] = score
            return redirect(url_for("Result"))

    return render_template(
        "operating_system.html",
        question=QUESTIONS_OS[qno],
        qno=qno,
        total=len(QUESTIONS_OS)
    )

@app.route('/dbms/<int:qno>', methods=['GET', 'POST'])
def dbms(qno):

    if "score" not in session:
        session["score"] = 0

    # POST (answer submit)
    if request.method == "POST":

        selected = request.form.get("answer")

        # save answer in session per question
        session[f"q{qno}"] = selected

        # NEXT button
        if "next" in request.form and qno < len(QUESTIONS_DBMS) - 1:
            return redirect(url_for("dbms", qno=qno+1))

        # PREVIOUS button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("dbms", qno=qno-1))

        # SUBMIT button
        if "submit" in request.form:
            score = 0

            for i in range(len(QUESTIONS_DBMS)):
                if session.get(f"q{i}") == QUESTIONS_DBMS[i]["answer"]:
                    score += 1

            session["score"] = score
            return redirect(url_for("Result"))

    return render_template(
        "dbms.html",
        question=QUESTIONS_DBMS[qno],
        qno=qno,
        total=len(QUESTIONS_DBMS)
    )

@app.route('/computer_networks/<int:qno>', methods=['GET', 'POST'])
def computer_networks(qno):

    if "score" not in session:
        session["score"] = 0

    # POST (answer submit)
    if request.method == "POST":

        selected = request.form.get("answer")

        # save answer in session per question
        session[f"q{qno}"] = selected

        # NEXT button
        if "next" in request.form and qno < len(QUESTIONS_CN) - 1:
            return redirect(url_for("computer_networks", qno=qno+1))

        # PREVIOUS button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("computer_networks", qno=qno-1))

        # SUBMIT button
        if "submit" in request.form:
            score = 0

            for i in range(len(QUESTIONS_CN)):
                if session.get(f"q{i}") == QUESTIONS_CN[i]["answer"]:
                    score += 1

            session["score"] = score
            return redirect(url_for("Result"))

    return render_template(
        "computer_networks.html",
        question=QUESTIONS_CN[qno],
        qno=qno,
        total=len(QUESTIONS_CN)
    )

@app.route('/data_structures/<int:qno>', methods=['GET', 'POST'])
def data_structures(qno):

    if "score" not in session:
        session["score"] = 0

    # POST (answer submit)
    if request.method == "POST":

        selected = request.form.get("answer")

        # save answer in session per question
        session[f"q{qno}"] = selected

        # NEXT button
        if "next" in request.form and qno < len(QUESTIONS_DS) - 1:
            return redirect(url_for("data_structures", qno=qno+1))

        # PREVIOUS button
        if "prev" in request.form and qno > 0:
            return redirect(url_for("data_structures", qno=qno-1))

        # SUBMIT button
        if "submit" in request.form:
            score = 0

            for i in range(len(QUESTIONS_DS)):
                if session.get(f"q{i}") == QUESTIONS_DS[i]["answer"]:
                    score += 1

            session["score"] = score
            return redirect(url_for("Result"))

    return render_template(
        "data_structures.html",
        question=QUESTIONS_DS[qno],
        qno=qno,
        total=len(QUESTIONS_DS)
    )



@app.route('/logout')
def logout():

    session.pop('sr_no', None)
    flash('you have been logout.','info')
    return redirect(url_for('Home'))

@app.route('/Register', methods=['GET', 'POST'])
def Register():
    if request.method == 'POST':

        sr_no = request.form.get('sr_no')
        student_name = request.form.get('student_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        subject = request.form.get('subject')

        if not sr_no or not student_name or not username or not email or not password or not subject:
            flash('Please provide all details!', 'danger')
            return redirect(url_for('Register'))

        conn = get_db()

        

        conn.execute(
            '''
            INSERT INTO SCORE
            (Student_name, Username, Email, Password, subject)
            VALUES (?, ?, ?, ?, ?)
            ''',
            (student_name, username, email, password, subject)
        )

        conn.commit()
        conn.close()

        new_students = {
            'Sr_no':sr_no,
            'Name':student_name,
            'username':username,
            'email':email,
            'password':password

        }
        stud.append(new_students)

        flash('🎉 Registration Successful!', 'success')

        return redirect(url_for('Register'))

    return render_template('Register.html')

@app.route('/search')
def search():
    q = request.args.get('q', '')
    conn = get_db()

    if q:
        students = conn.execute(
            '''SELECT * FROM SCORE
               WHERE Student_name LIKE ?
               OR Username LIKE ?''',
            (f'%{q}%', f'%{q}%')
        ).fetchall()
    else:
        students = conn.execute(
            'SELECT * FROM SCORE ORDER BY Sr_no ASC'
        ).fetchall()

    conn.close()

    return render_template(
        'search.html',
        students=students,
        query=q
    )



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Add_Students', methods=['GET', 'POST'])
def Add_Students():

    if request.method == "POST":

        roll = request.form.get('roll_name')
        name = request.form.get('student_name')
        marks = request.form.get('marks')


        if not name or not marks:
            flash('Please provide both name and marks', 'danger')
            return render_template("Add_students.html")
        
        conn = get_db()
        conn.execute('''INSERT INTO SCORE
                     (Student_name,total_marks) VALUES(?,?)''',
                     (name, int(marks))
                     )
        conn.commit()
        conn.close()

        new_student = {
            'name':name,
            'roll_no':roll,
            'marks':int(marks),
        }

        stud.append(new_student)
        #flash massage display        
        flash(f"Student name : {name} Added successfully!","success")
        print(f"Received Student: {name}")
        print(f"Updated Student List: {stud}")
        return redirect(url_for('Add_Students'))

    return render_template('Add_students.html')


@app.route("/students")
def students():

    conn = get_db()
    db_students = conn.execute(
        'SELECT * FROM SCORE ORDER BY Sr_no ASC'
    ).fetchall()
    conn.close()

    combined_students = []

    # Dictionary Data
    for s in stud:
        combined_students.append({
        'Sr_no': s.get('Sr_no', s.get('roll_no', '')),
        'Name': s.get('Name', s.get('name', '')),
        'username': s.get('username', ''),
        'email': s.get('email', ''),
        'password': s.get('password', '')
    })

    # Database Data
    for s in db_students:
        combined_students.append({
        'Sr_no': s['Sr_no'],
        'Name': s['Student_name'],
        'username': s['Username'],
        'email': s['Email'],
        'password': s['Password']
    })

    return render_template(
        "students.html",
        students=combined_students
    )

    
@app.route('/view_student/<int:Sr_no>')
def view_student(Sr_no):

    conn = get_db()

    student = conn.execute(
        "SELECT * FROM SCORE WHERE Sr_no=?",
        (Sr_no,)
    ).fetchone()

    conn.close()

    return render_template('view_student.html', students=student)


@app.route('/delete_candidate/<int:Sr_no>')
def delete_candidate(Sr_no):

    conn = get_db()

    student = conn.execute(
    'SELECT * FROM SCORE WHERE Sr_no=?',
    (Sr_no,)
).fetchone()
    if student is None:
        flash("student not found","danger")
        conn.close()
    
    conn.execute(
    'DELETE FROM SCORE WHERE Sr_no=?',
    (Sr_no,)
)
    conn.commit()
    conn.close()
    flash("candidate deleted successfully","success")
    return redirect(url_for('students'))

@app.route('/edit_student/<int:Sr_no>', methods=['GET', 'POST'])
def edit_student(Sr_no):

    conn = get_db()

    if request.method == 'POST':

        Candidate_name = request.form['Candidate_name']

        conn.execute(
            "UPDATE SCORE SET student_name=? WHERE Sr_no=?",
            (Candidate_name, Sr_no)
        )

        conn.commit()
        conn.close()

        return redirect(url_for('students'))

    student = conn.execute(
        "SELECT * FROM SCORE WHERE Sr_no=?",
        (Sr_no,)
    ).fetchone()

    conn.close()

    return render_template('edit_student.html', student=student)


@app.route('/filter')
def filter():

    subject = request.args.get('subject')

    conn = get_db()

    if subject:
        students = conn.execute(
            "SELECT * FROM SCORE WHERE subject=?",
            (subject,)
        ).fetchall()
    else:
        students = conn.execute(
            "SELECT * FROM SCORE"
        ).fetchall()

    conn.close()

    return render_template(
        'filter_result.html',
        students=students
    )

@app.route('/Subject')
def Subject():
    return render_template('Subject.html')


@app.route('/Result')
def Result():
    score = session.get("score", 0)
    total = len(QUESTIONS)

    return render_template("result.html", score=score, total=total)
    


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
















































































