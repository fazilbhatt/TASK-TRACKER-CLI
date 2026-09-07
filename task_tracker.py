import sys, json, os
from datetime import datetime

def main():
    FILE_NAME = "tasks.json"
    if len(sys.argv) < 2: return print_help()
    
    try:
        tasks = json.load(open(FILE_NAME)) if os.path.exists(FILE_NAME) else []
        cmd, args = sys.argv[1], sys.argv[2:]
        
        if cmd == "add" and args:
            task_id = max([t['id'] for t in tasks], default=0) + 1
            tasks.append({"id": task_id, "description": args[0], "status": "todo", 
                         "createdAt": datetime.now().isoformat(), "updatedAt": datetime.now().isoformat()})
            print(f"Task added successfully (ID: {task_id})")
        
        elif cmd == "update" and len(args) > 1:
            for t in tasks:
                if t['id'] == int(args[0]): 
                    t.update({"description": args[1], "updatedAt": datetime.now().isoformat()})
                    print(f"Task {args[0]} updated."); break
            else: print(f"Task {args[0]} not found.")
        
        elif cmd == "delete" and args:
            prev_len = len(tasks)
            tasks = [t for t in tasks if t['id'] != int(args[0])]
            print(f"Task {args[0]} deleted." if len(tasks) < prev_len else f"Task {args[0]} not found.")
        
        elif cmd.startswith("mark-") and args:
            status = "in-progress" if "progress" in cmd else "done"
            for t in tasks:
                if t['id'] == int(args[0]): 
                    t.update({"status": status, "updatedAt": datetime.now().isoformat()})
                    print(f"Task {args[0]} marked as {status}."); break
            else: print(f"Task {args[0]} not found.")
        
        elif cmd == "list":
            status_filter = args[0] if args and args[0] in ["todo", "in-progress", "done"] else None
            filtered = [t for t in tasks if not status_filter or t['status'] == status_filter]
            print(f"{'ID':<4} {'Status':<12} {'Description'}") if filtered else print("No tasks found.")
            [print(f"{t['id']:<4} {t['status']:<12} {t['description']}") for t in filtered]
        
        else: print_help()
        
        json.dump(tasks, open(FILE_NAME, 'w'), indent=4)
    
    except (ValueError, IndexError): print("Invalid arguments. Check task ID and syntax.")
    except Exception as e: print(f"Error: {e}")

def print_help():
    print("Usage: task-cli <command> [args]\nCommands: add \"desc\", update id \"desc\", delete id, mark-in-progress id, mark-done id, list [status]")

if __name__ == "__main__":
    main()