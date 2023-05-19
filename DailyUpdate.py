"""Daily Update Generator

This script generates a daily update for the team. The daily update
is a summary of the work done for the day. It includes the following
sections:
    - Current Tasks
    - Completed Tasks
    - Pending Tasks
"""

from datetime import date

update_file = "daily_update.txt"


class DailyUpdate:

    def __init__(self, update_file):
        self.update_file = update_file
        self.date = date.today()  # date of the daily update
        self.all_tasks = []  # list of all tasks for the day
        self.current_tasks = []  # list of tasks for the day
        self.completed_tasks = []  # list of completed tasks for the day
        self.pending_tasks = []  # list of pending tasks for the day
        self.blocked_tasks = []  # list of blocked tasks for the day
        self.miscellaneous_tasks = []  # list of miscellaneous tasks for the day

    def add_task(self, task):
        """Add Task
        Description: Adds a task to the daily update
        """
        if task not in self.all_tasks:
            self.all_tasks.append(task)
        else:
            raise Exception("Task already in daily update")

        if task.status == Status.CURRENT_TASK:
            self.current_tasks.append(task)
        elif task.status == Status.COMPLETED_TASK:
            self.completed_tasks.append(task)
        elif task.status == Status.PENDING_TASK:
            self.pending_tasks.append(task)
        elif task.status == Status.BLOCKED_TASK:
            self.blocked_tasks.append(task)
        elif task.status == Status.MISCELLANEOUS_TASK:
            self.miscellaneous_tasks.append(task)
        else:
            raise Exception("Invalid task status")

    def remove_task(self, task):
        """Remove Task
        Description: Removes a task from the daily update
        """
        if task not in self.all_tasks:
            raise Exception("Task not in daily update")
        else:
            self.all_tasks.remove(task)

        if task.status == Status.CURRENT_TASK:
            self.current_tasks.remove(task)
        elif task.status == Status.COMPLETED_TASK:
            self.completed_tasks.remove(task)
        elif task.status == Status.PENDING_TASK:
            self.pending_tasks.remove(task)
        elif task.status == Status.BLOCKED_TASK:
            self.blocked_tasks.remove(task)
        elif task.status == Status.MISCELLANEOUS_TASK:
            self.miscellaneous_tasks.remove(task)
        else:
            raise Exception("Invalid task status")

    def print_daily_update(self):
        """Print Daily update
        Description: Prints the daily update to the console
        The update should follow this format:
        Date
        Current Tasks
        -------------
            - [Priority] Task Name - Jira Number [Estimated time]
                Task Description
                Jira Link (if applicable)
            ...
        Completed Tasks
        ---------------
            - Task Name - Jira Number
                Notes if applicable
            ...
        Pending Tasks
        -------------
            - Task Name - Jira Number
                Notes if applicable
            ...
        """
        print("--------------------------------------------------------------")
        # date in format: Month Day, Year
        date = self.date.strftime("%B %d, %Y")
        print(date)

        print("Current Tasks")
        print("-------------")

        # print all tasks
        for task in self.all_tasks:
            jira_str = ""
            if task.jira_num:
                jira_str = f" - {task.jira_num}"
            print(f"\t- [{task.priority}] {task.name}{jira_str} [{task.estimated_time}]")

            print(f"\t{task.description}")
            if task.jira_link:
                print(f"\t{task.jira_link}")

        print("Completed Tasks")
        print("---------------")

        print("Pending Tasks")
        print("-------------")


class Task:
    """ Task
    Description: A task is a unit of work that needs to be completed
    All tasks have the following attributes:
        - name: name of the task
        - description: description of the task
        - status: status of the task (current, completed, pending)
        - priority: priority of the task (highest, high, medium, low, lowest)
        - estimated_time: estimated time to complete the task
        - actual_time: actual time to complete the task
        - jira_num: jira number for the task
        - jira_link: jira link for the task

    """

    def __init__(self, name, description, status, priority, estimated_time=None, actual_time=None, jira_num=None,
                 jira_link=None):
        self.name = name
        self.description = description
        self.status = status
        self.priority = priority
        self.estimated_time = estimated_time
        self.actual_time = actual_time
        self.jira_num = jira_num
        self.jira_link = jira_link


class Status:
    """ Status
    Description: Status of a task
    Note: A task can only have one status at a time
    Note: All tasks are current tasks so there is no need to have a current
    task status.

    Description of statuses:
        - completed: task is completed
        - pending: task is pending so it is still in progress
        - blocked: task is blocked
        - miscellaneous: task is in the miscellaneous category
            (i.e. meetings, support sessions, etc.)
    """
    COMPLETED_TASK = "completed"
    PENDING_TASK = "pending"
    BLOCKED_TASK = "blocked"
    MISCELLANEOUS_TASK = "miscellaneous"


class Priority:
    HiGHEST_PRIORITY = "highest"
    HIGH_PRIORITY = "high"
    MEDIUM_PRIORITY = "medium"
    LOW_PRIORITY = "low"
    LOWEST_PRIORITY = "lowest"


def get_last_update() -> str:
    last_update = ""
    # open update file
    with open(update_file, "r") as f:
        last_update_line = f.read()
        last_update += last_update_line
    # read last update
    # return last update
    return last_update



