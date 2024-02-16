# Function creation for insertin the task
def insert_task():
     task=input("Please Eneter Your Task to Schedule:")
     task_list.append(task)
     print("Your task is Inserted Sucessfully!")
     print(".........................................................")
# Creating the function for viewing the task
def view_task():
     if len(task_list)==0:
          print("Task Schedule is Empty!")
          print("Please Insert any Schedule!")
     else:
          for i, task in enumerate(task_list):
               print(f'{1+i}.{task}')
          print(".........................................................")
# Creating the function for deleting the task
def delete_task():  
     if len(task_list)==0:
          print("Task Schedule is Empty!")
          print("Please Insert any Schedule!")
     else:
          for i, task in enumerate(task_list):
               print(f'{1+i}.{task}')
          choice=int(input("Enter the task Number you want to delete...."))
          task_list.remove(task_list[choice-1])
          print("Your task ",(task_list[choice-1])," is Deleted Sucessfully!")
     print(".........................................................")
# Main Program
task_list=[]
print("================== WELCOME TO TASKS SCHEDULE ==================")
while True:
     print("Select Your option to do any one task from Below:")
     print("1.Insert Task\n2.View Task\n3.Delete Task\n4.Quit")
     
# Using the match case for user input actions
     choice=int(input())
     match choice:
          case 1:
               insert_task()
          case 2:
               view_task()
          case 3:
               delete_task()
          case 4:
               print("*******************THANK YOU FOR ACTIVITES******************")
               break
          case _:
               print("Your Option is Wrong\nPlease Enter a Valid Option")
               
               
