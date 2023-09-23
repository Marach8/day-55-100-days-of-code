import os, time

list1 = []
head = ['Description', 'Due Date', 'Priority']

  
def menu():
  w = '\033[4mWELCOME TO OUR TO-DO LIST MANAGER\033[0m'
  print(f'\033[0m{w:^65}')
  print()
  print('\033[1;33m1: Add\n2: View\n3: Edit\n4: Remove')
  ask = input('\033[0m>> ')
  return ask


def add():
  auto_load()
  os.system('clear')
  time.sleep(1.5)
  print('\033[4mFill the following information for your TODO\033[0m')
  print()
  time.sleep(1)
  ask1 = input('Enter the To-do: ')
  ask2 = input('Enter the due date or time of the To-do: ')
  list2 = [ask1, ask2]

  while True:
    print()
    print('\033[1;36mBased on how important the event is to you, you can select a priority of High, Medium or Low.')
    time.sleep(1)
    print()
    ask3 = input('\033[0mEnter the priority\n1: High\n2: Medium\n3: Low\n>> ')
    if ask3 == '1':
      list2.append('High')
      break
    elif ask3 == '2':
      list2.append('Medium')
      break
    elif ask3 == '3':
      list2.append('Low')
      break
    else:
      print()
      print('\033[31mPlease select 1, 2 or 3 to proceed')
      time.sleep(2)
      continue 
  time.sleep(1)
  list1.append(list2)
  auto_save(list1)
  print('\033[32mYour Todo has been added Succesfully😎')
  time.sleep(2)
  querry = input('\033[0mWant to add again? y/n: ')
  if querry == 'y':
    time.sleep(1.5)
    os.system('clear')
    add()
  else:
    os.system('clear')
    time.sleep(2)
    body()
    

def view():
  auto_load()
  if len(list1) != 0:
    time.sleep(2)
    print()
    q = '\033[4mEnter any of the numbers to perform the following operations\033[0m'
    print(f'\033[0m{q}')
    print()
    ask = input('\033[0;37m1: View all todo\n2: View by priority\n>> ')
    if ask == '1':
      printer(list1)
      print()
      todo_load()
    elif ask == '2':
      while True:
        print()
        list2 = []
        list2.insert(0, head)
        ask2 = input('1: view High priority\n2: view Medium priority\n3: view Low priority\n>> ')
        if ask2 == '1':
          for i, j in enumerate(list1):
            if 'High' in j:
              list2.append(j)
          printer(list2)
          break
        elif ask2 == '2':
          for i, j in enumerate(list1):
            if 'Medium' in j:
              list2.append(j)
          printer(list2)
          break
        elif ask2 == '3':
          for i, j in enumerate(list1):
            if 'Low' in j:
              list2.append(j)
          printer(list2)
          break
        else:
          print ()
          print('\033[31mplease input 1, 2 or 3 to proceed!')
          print()
          continue
    else:
      print()
      print('\033[31mPlease input 1, or 2 to proceed!')
      print()
      view()
    todo_load()
  else:
    print ('\033[31mYou currently have no entries in your To-do list. Add entries first before you can view!')
    time.sleep(2)
    os.system('clear')
    body()
    
def edit():
  auto_load()
  if len(list1) != 0:
    print ()
    printer(list1)
    print ()
    
    a = input('Type in any of the information above that you wish to change?: ').strip()
    b = input('Enter the replacement: ').strip()
    m = 0
    for i, j in enumerate(list1):
      if a in j:
        d = j.index(a)
        list1[i][d] = b
        auto_save(list1)
        print()
        print('\033[32mItem edited Successfully😊')
        time.sleep(2)
        break
      else:
        m += 1
        if m == len(list1):
          print()
          time.sleep(1.5)
          print('\033[31mThe item you chose is not in there')
          time.sleep(2.5)
        else:
          continue
              
    print()
    time.sleep(3)
    os.system('clear')
    body()

                    
  else:
    print ('\033[31mYou currently have no entries in your To-do list. Add entries first before you can edit!')
    time.sleep(8)
    os.system('clear')
    body()


def remove():
  auto_load()
  if len(list1) != 0:
    print ()
    printer(list1)
    print ()
    
    m = 0
    while True:
      print()
      a = input('''\033[0mType in any of the information above that you wish to remove?: ''')
      for i, j in enumerate(list1):
        if a in j:
          list1.remove(j)
          auto_save(list1)
          print()
          time.sleep(1.5)
          print('\033[32mItem removed succesfully')
          time.sleep(2)
          break
        else:
          m += 1
          if m == len(list1):
            print()
            time.sleep(1.5)
            print('\033[31mThe item you chose is not in there')
            time.sleep(2.5)
          else:
            continue
            
      print()                     
      printer(list1)
      response = input('\033[0mWant to remove again? y/n: ')
      if response == 'y':
        os.system('clear')
        printer(list1)
        continue
      else:
        break
    time.sleep(1.5)
    os.system('clear')
    body()
                    
  else:
    print ('\033[31mYou currently have no entries in your To-do list. Add entries first before you can remove!')
    time.sleep(8)
    os.system('clear')
    body()


def printer(w):
  global p
  os.system('clear')
  m = 0
  for i in w:
    if m == 0:
      for j in i:
        print(f'\033[1;33m{j:^20}', end='|')
        m += 1
      print()
      print('    ___________________________________________________________')
    else:
      for j in i:
        print(f'\033[34m{j:^20}', end='|')
    print()
  print()


def todo_load():
  time.sleep(2)
  ask4 = input('''\033[0mWhen you are done viewing, press 'Enter' to go back to main menu: 
''')
  if len(ask4) == 0:
    time.sleep(1.5)
    print()
    print('\033[35mTODO menu Loading... Please wait...')
    time.sleep(1.5)
    os.system('clear')
    body()


def body():
  b = menu()
  while True:
    
    if b == '1':
      add()
    elif b == '2':
      view()
    elif b == '3':
      edit()
    elif b == '4':
      remove()
    else:
      print()
      print('\033[31mInvalid selection! Please select either 1, 2, 3 or 4')
      time.sleep(3)
      os.system('clear')
      b = menu()
      continue 

p = 0
def auto_load():
  global list1, p
  try:
    m = open('todo.txt', 'r')
    list1 = eval(m.read())
    if head in list1:
      p += 1
    m.close()
  except FileNotFoundError:
    pass

#h = os.listdir()
def auto_save(anylist):
  global list1, p, h
  if p == 0:
    list1.insert(0, head)
  else:
    pass

  if os.path.exists('backup'):
    pass
  else:
    os.mkdir('backup')
    
  backup_file = os.path.join('backup/', 'b_file')
  file = open(backup_file, 'a+')
  file.write(f'{str(anylist)}\n')
  file.close()
  
  n = open('todo.txt', 'w')
  n.write(str(anylist))
  n.close()
  p += 1

body()