import shlex

database = {}

def add(task):
  if task in database:
    print(f'Task "{task}" already exists')
    return
  database[task] = False
  print(f'Added "{task}"')

def remove(task):
  if task not in database:
    print(f'Task "{task}" does not exist')
    return
  del database[task]
  print(f'Deleted "{task}"')

def rename(task, new_name):
  if task not in database:
    print(f'Task "{task}" does not exist')
    return
  if new_name in database:
    print(f'Task "{new_name}" already exists')
    return
  database[new_name] = database[task]
  del database[task]
  print(f'Renamed "{task}" to "{new_name}"')

def list_tasks(filter='todo'):
  match filter:
    case 'done':
      filter = lambda task: database[task]
    case 'all':
      filter = lambda _: True
    case 'todo':
      filter = lambda task: not database[task]
    case _:
      print(f'Unknown filter "{filter}"')
  for task in database:
    if filter(task):
      print('[x]' if database[task] else '[ ]', task)

def check(task):
  if task not in database:
    print(f'Task "{task}" does not exist')
    return
  database[task] = True
  print(f'Checked "{task}"')

def uncheck(task):
  if task not in database:
    print(f'Task "{task}" does not exist')
    return
  database[task] = False
  print(f'Unchecked "{task}"')

def toggle(task):
  if task not in database:
    print(f'Task "{task}" does not exist')
    return
  database[task] = not database[task]
  print(f'Toggled "{task}"')

if __name__ == '__main__':
  print('To Do List CLI')
  while True:
    args = shlex.split(input('> '))
    match args[0]:
      case 'add':
        if len(args) < 2:
          print('Usage: add <task>')
          continue
        add(args[1])
      case 'list':
        if len(args) > 1:
          list_tasks(filter=args[1])
        else:
          list_tasks()
      case 'remove':
        if len(args) < 2:
          print('Usage: remove <task>')
          continue
        remove(args[1])
      case 'rename':
        if len(args) < 3:
          print('Usage: rename <old> <new>')
          continue
        check(args[1], args[2])
      case 'check':
        if len(args) < 2:
          print('Usage: check <task>')
        check(args[1])
      case 'uncheck':
        if len(args) < 2:
          print('Usage: uncheck <task>')
          continue
        uncheck(args[1])
      case 'toggle':
        if len(args) < 2:
          print('Usage: toggle <task>')
          continue
        toggle(args[1])
      case 'exit':
        exit(0)
      case _:
        print('Unknown command')