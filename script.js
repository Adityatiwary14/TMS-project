document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('taskForm');
    const taskList = document.getElementById('taskList');

    const tasks = [];

    taskForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const title = document.getElementById('taskTitle').value;
        const description = document.getElementById('taskDescription').value;
        const dueDate = document.getElementById('taskDueDate').value;

        const task = {
            id: Date.now(),
            title,
            description,
            dueDate
        };

        tasks.push(task);
        displayTasks();
        taskForm.reset();
    });

    const displayTasks = () => {
        taskList.innerHTML = '';

        tasks.forEach(task => {
            const taskItem = document.createElement('li');
            taskItem.className = 'task';

            const taskTitle = document.createElement('h3');
            taskTitle.textContent = task.title;
            taskItem.appendChild(taskTitle);

            const taskDescription = document.createElement('p');
            taskDescription.textContent = task.description;
            taskItem.appendChild(taskDescription);

            const taskDueDate = document.createElement('p');
            taskDueDate.textContent = `Due Date: ${task.dueDate}`;
            taskItem.appendChild(taskDueDate);

            const editButton = document.createElement('button');
            editButton.textContent = 'Edit';
            editButton.addEventListener('click', () => editTask(task.id));
            taskItem.appendChild(editButton);

            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Delete';
            deleteButton.addEventListener('click', () => deleteTask(task.id));
            taskItem.appendChild(deleteButton);

            taskList.appendChild(taskItem);
        });
    };

    const editTask = (taskId) => {
        const task = tasks.find(t => t.id === taskId);
        if (task) {
            document.getElementById('taskTitle').value = task.title;
            document.getElementById('taskDescription').value = task.description;
            document.getElementById('taskDueDate').value = task.dueDate;

            deleteTask(taskId);
        }
    };

    const deleteTask = (taskId) => {
        const taskIndex = tasks.findIndex(t => t.id === taskId);
        if (taskIndex > -1) {
            tasks.splice(taskIndex, 1);
            displayTasks();
        }
    };
});
