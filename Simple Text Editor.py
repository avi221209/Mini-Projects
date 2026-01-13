while True:
   choice = input("Enter The filename to open or create:").lower()

   if choice == "open":
       new_choice1 = input("Enter a file name to open (file.txt) or (file1.txt): ")
       
       if new_choice1 not in ["file.txt","file1.txt"]:
            print("Invalid")
            continue
       
       with open(new_choice1, "r") as f:
            print(f.read())
            break
   
   elif choice == "create":
       text = input("Enter You text: ")
       
       with open("file2.txt","w") as f:
           f.write(text)

       with open("file2.txt","r") as f:
           print(f.read())    
       break
 