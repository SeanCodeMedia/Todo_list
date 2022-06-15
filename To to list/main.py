import sqlite3 as db
import os

connection  = db.connect("todolist.db");
cursorObject  = connection.cursor(); 

RunProgram = True; 

os.system("color 2")

def Error():

	os.system("cls")
	os.system("color 4")

def createTable(listName):

	
	sql = "CREATE TABLE IF NOT EXISTS "+listName+" (task_id INTEGER PRIMARY KEY AUTOINCREMENT, dateCreated DATETIME,description TEXT,taskDone BOOLEAN)"
	try:
		cursorObject.execute(sql)

	except Exception as e:

		Error(); 
		print("Opps it seem like you did not input a valid to-do list name please enter a name without space, number or characters >>>")
		input("Please hit the enter key to continue...")
		os.system("cls")

		main();

         

def printTable (Tablename, command=None):
	try:

		listTable = cursorObject.execute("SELECT*FROM " + Tablename) 

		dataList = cursorObject.fetchall()

		if(len(dataList) > 0):

			for nameOfList in dataList:
				print("================")
				print ("Task Number: " + str(nameOfList[0]) + "| Date task created: " + str(nameOfList[1]) + " | Task: "+ str((nameOfList[2]) + " | Task Complete: " + str(nameOfList[3])))
				
			print("================")
		elif(command == "a"):

			 print("This to-do list is empty !!")

		else:
			command15 = input("This to-do list is empty do you want to add a task to this list?(Yes/No)>>>")

			if(command15.lower() == "yes"):


				insertData(Tablename)

			elif(command15.lower() == "no"):

				os.system("cls")
				main()




	except:

		Error()
		input("Please enter a vaild name (list does not exist) press the enter key to continue...")
		os.system("cls")
		main()


def showTable():

	listTable = cursorObject.execute("select name from sqlite_master where type = 'table'")

	tableCount = cursorObject.fetchall()

	if(len(tableCount) > 1):

		for nameOfList in tableCount:
			
			if(nameOfList[0] != "sqlite_sequence"):
				print("================")
				print (nameOfList[0])
				print("================")
	else:

		print("Notice:You haven't created a to-do list yet!!")

def deleteTable():

	table = cursorObject.execute("select name from sqlite_master where type = 'table'")

	count = cursorObject.fetchall()

	if(len(count) > 1):

		print("Here's the list of to do list you have created in the past please pick one to delete >>>") 

		showTable()

		command3 = input("Please enter the name of the list that you would like to remove >>>")
		deleteTB = "DROP TABLE " +command3
		
		if(len(command3) > 0 ):

			try:
				cursorObject.execute(deleteTB)
				input("you have deleted this to-do list successfully...hit enter to continue >>>")
			except:
				Error()
				input("oops this to-do list name you entered does not exist!! hit enter to continue>>>")
		else:
			Error()
			input("oops you did not enter a list name hit enter to continue>>>")

	else:
		input("you haven't created a list yet...please hit enter to continue>>>")
	
	
	os.system("cls")
	main()


def insertData(Tablename):
	try:

		command5 = input("Please enter an description of the task >>>")

		if(len(command5) == 0):

			print("Please enter a discription of the task!")

			insertData(Tablename)

		else: 

			command6 = input("Did you complete this task ?(Yes or No) >>>")

			if(command6.lower() == "yes"):

				cursorObject.execute("INSERT INTO "+Tablename+" (task_id,dateCreated,description,taskDone)VALUES(NULL,DATETIME('now','localtime'),?,?)",(command5,command6))
				connection.commit()

			elif(command6.lower() == "no"):

				cursorObject.execute("INSERT INTO "+Tablename+" (task_id,dateCreated,description,taskDone)VALUES(NULL,DATETIME('now','localtime'),?,?)",(command5,command6))
				connection.commit()


			else:

				print("Please enter (yes or no)")
				insertData(Tablename)

		commnad7 = input("Do you want to add another task to your to-do list? (Yes/No) >>>")

		if(commnad7.lower() == "yes" ):

			os.system("cls")

			print("This is your updated to-do list")

			printTable(Tablename)

			insertData(Tablename)


		elif(commnad7.lower() == "no"):

			os.system("cls")

			print("This is your updated to-do list")

			printTable(Tablename)

			input("Please hit enter to continue...>>>")

			os.system("cls")
			main()
		else:
			print("Please enter yes or no!")
			insertData(Tablename)
	
	except Exception as e:

	 	print(e)
	



def deleteRow (Tablename):

	command11 = input("Please select a task number to delete a task from the list >>>")

	sql = "DELETE FROM "+Tablename+" WHERE task_id=?"

	#sql2 = "DELETE FROM sqlite_sequence WHERE name=?"

	cursorObject.execute(sql, (command11,))
	
	connection.commit()

	printTable(Tablename)

def updateTask(Tablename):

	command_11 = input("Please select a task number to update a task from the list >>>")
	command12 = input("Please enter the description of the task >>>")
	command13 = input("Did you finish this task? (Yes or No) >>>")

	sql = "UPDATE " + Tablename + " SET description = ?, taskDone = ? WHERE task_id = ?"

	cursorObject.execute(sql, (command12,command13,command_11,))
	connection.commit()
	
	printTable(Tablename)

input("Welcome to the To Do List Program written by Sean Peart. Please press enter to start>>>");


def main():
	os.system("color 2")

	while RunProgram: 

		command1 = input(" Press the N key to create a new to do list \n Press the V key  to view a to do list \n Press the S key to show all the list \n Press the D key  to delete a list \n Press the A key to add a task to a list \n Press the R key to delete a task from a list \n Press the U key to update a task \n Press the E key to exit program >>>")

		if(command1.lower() == "n"):

			showTable()
			

			command2 = input("Please enter the name of the list that you would like to create >>>")
		
			createTable(command2)

			showTable()

			command4 = input(" Do you want to add a task to your list ? (Yes/No) >>>")

			if(command4.lower() == "yes"):

				insertData(command2)

			elif(command4.lower() == "no"):

				os.system("cls")
				main()
			else:
				os.system("color 4")
				input("you have entered a invalid input... please hit enter to continue")
				os.system("cls")
				main()

		elif (command1.lower() == "s"):
			
			print("Here's a List of to-do list you have created in the past")

			showTable()

		elif (command1.lower() == "d"):
		         
		     deleteTable()

		elif(command1.lower() == "a"):

			print("Here's the list of to do list you have created in the past please pick one to add a task to >>>") 

			showTable()

			command8 = input("Please select a list you want to add a task to  >>>") 

			printTable(command8,command1.lower())

			insertData(command8) 

			printTable(command8)

		elif(command1.lower() == "v"):

				print("Here's the list of to do list you have created in the past please pick one to view >>>") 

				showTable()

				command9 = input("Please select a list you want to view >>>") 
		
				printTable(command9)
				

		elif(command1.lower() == "r" ):

			tableCount = cursorObject.fetchall() 

			if(len(tableCount) > 1 ):

				print("Here's the list of to do list you have created in the past please pick one to Delete a task from >>>") 

				showTable()

				command10 = input("Please enter the to do list name you would like to delete a task from >>>")

				printTable(command10)

				deleteRow(command10)
			else:

				input("You didn't create a to-do list yet.. please hit enter to continue >>>")
				os.system("cls")
				main()

		elif(command1.lower() == "u" ):

			tableCount = cursorObject.fetchall()

			if(len(tableCount)):

				print("Here's the list of to do list you have created in the past please pick one to update a task >>>") 

				showTable()

				command11 = input("Please enter the to do list name you would like to update a task >>>")

				printTable(command11)

				updateTask(command11)
			else:

				input("There is no to-do list update hit enter to continue... >>>")

		elif(command1.lower() == "e" ): 

			connection.close()
			exit()
			

		else:

			Error()

			print("Please enter a valid key !")

		input("Please hit the enter key to continue...")

		os.system("cls")
		os.system("color 2")




if __name__ == '__main__':
	main()
