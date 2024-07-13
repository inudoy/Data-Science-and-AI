#Youtube manager application

import json
def load_data():
    try:
        with open('youtubes.txt','r') as file:
            test=  json.load(file)
            print(type(test))
            return test

    except FileNotFoundError:
        return []
    finally:
        print("complete loading...")
        
def date_helper(video):
    with open('youtubes.txt','w') as file:
        json.dump(video, file)
def listall(video):
    print("\n")
    print("*"*60)
    for index , vid in enumerate(video,start=1):
        print(f"{index}.{vid['name']},duration:{vid['time']} ")
    print("\n")
    print("-"*60)
def addvideo(video):
    name = input("enter vidoe name ")
    
    time=input("enter vidoe length ")
    
    video.append({'name': name, 'time': time})
    date_helper(video)
    
    

def updatevideo(video):
    listall(video)
    index=int(input("enter vidoe number \n"))
    if 1<=index<=len(video):
        name=input("enter vidoe name")
        time=input("enter vidoe length")
        video[index-1]['name']=name
        video[index-1]['time']=time
        date_helper(video)
        
    

def deletevideo(video):
    listall(video)
    index=int(input("enter vidoe number \n"))
    if 1<=index<=len(video):
        video.pop(index-1)
        date_helper(video)

def main():
    
    video=load_data()
    while True:
        print("\nYoutube Manager Application")
        print("chose a option ")
        print("1.List all video")
        print("2. Add a yotube video ")
        print("3. update youtube video  details")
        print("4. delete youtube Video")
        print("5. Exit")
        
        print(".....................................................................")
        # print(video,"\n")
        
        choice = input("enter your choice")
        
        match choice:
            case '1':
                #list all video
                print("list all video")
                listall(video)
                
            case '2':
                #add a yotube video
                print("add a yotube video")
                addvideo(video)
            
            case '3':
                updatevideo(video)
            
            case '4':
                #delete youtube Video
                print("delete youtube Video")
                deletevideo(video)
            case '5':  
                #exit
                print("Exiting the program")
                
                break
            case _:
                print("Invalid choice. Please try again")
                


if __name__ ==  "__main__":
    main()
    