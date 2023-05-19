from DailyUpdate import DailyUpdate, Task, Status, Priority


if __name__ == "__main__":
    update_file = "daily_update.txt"
    update = DailyUpdate(update_file)

    task1 = Task("Task 1", "This is task 1", Status.PENDING_TASK, Priority.HIGH_PRIORITY, estimated_time="1h")
    task2 = Task("Task 2", "This is task 2", Status.COMPLETED_TASK, Priority.MEDIUM_PRIORITY, estimated_time="2h",
                 actual_time="1h")
    task3 = Task("Task 3", "This is task 3", Status.PENDING_TASK, Priority.LOW_PRIORITY, estimated_time="3h",
                 jira_num="JIRA-123", jira_link="https://www.google.com")

    update.add_task(task1)
    update.add_task(task2)
    update.add_task(task3)

    update.print_daily_update()
