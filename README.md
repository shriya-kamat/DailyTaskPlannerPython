# 📅 Daily Task Planner  

A simple **daily task planner** built with **Python, PyQt5, and SQLite**. This application helps users organize tasks for specific dates using a calendar interface, allowing them to add, view, and mark tasks as completed.  

## 🚀 Features  

✅ **Calendar Integration** – Select a date to view or add tasks.  
✅ **Task Management** – Add, update, and track daily tasks.  
✅ **Task Completion Tracking** – Mark tasks as completed or pending.  
✅ **Persistent Storage** – Uses SQLite to save tasks for future reference.  
✅ **User-friendly UI** – Built with PyQt5 for a clean and intuitive interface.  

## 🛠️ Installation  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/shriya-kamat/DailyTaskPlannerPython.git  
   cd DailyTaskPlannerPython  
   ```  

2. **Install Dependencies**  
   Ensure you have Python installed, then run:  
   ```bash
   pip install PyQt5  
   ```  

3. **Run the Application**  
   ```bash
   python main.py  
   ```  

## 🖥️ Usage  

1. **Select a date** on the calendar.  
2. **View tasks** for that date.  
3. **Add a new task** using the input box and click "Add New".  
4. **Mark tasks as completed** by checking them off.  
5. **Click "Save Changes"** to update task status.  

## 📂 Project Structure  

```
📂 DailyTaskPlannerPython  
 ├── 📜 main.py        # Main application logic  
 ├── 📜 main.ui        # PyQt5 UI design  
 ├── 📜 data.db        # SQLite database file (auto-generated)  
 ├── 📜 README.md      # Project documentation  
```  

## 📝 Database Schema  

The application uses a simple SQLite database with a `tasks` table:  

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completed TEXT CHECK(completed IN ('YES', 'NO')),
    date TEXT NOT NULL
);
```  

## 📌 Future Improvements  

🔹 Add support for task priorities.  
🔹 Implement notifications/reminders.  
🔹 Export task lists to a file (CSV, PDF).  

## 📜 License  

This project is **open-source** under the [MIT License](LICENSE).  
