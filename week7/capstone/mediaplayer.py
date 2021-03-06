import random

class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        self.count = 0

    def appendSong(self, data):
        if self.head is None:
            new_node = Song(data)            
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Song(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
            
            self.count += 1

    def deleteSong(self, data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data: 
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def showCurrentSong(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


    def printPlaylist(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next
            print("null")

def menu():
  print(20 * "-" , "MENU" , 20 * "-")
  print("1. Add Song to Playlist")
  print("2. Remove song from Playlist")
  print("3. Play")
  print("4. Skip")
  print("5. Go Back")
  print("6. Shuffle")
  print("7. Show Currently Playing Song")
  print("8. Show Current Playlist Order")
  print("0. Exit")
  print(47 * "-")

list = LinkedList()

while True:
    menu()
    choice = int(input())

    if choice == 1:
        data = input("Enter an song title and artist name: ")
        list.appendSong(data)
        print("New Song Added to Playlist")
        list.showCurrentSong()

    elif choice == 2:
        title = input("Enter an song title to delete: ")
        list.deleteSong()

        # Prompt user for Song Title 
        # remove song from playlist
        print("Song Removed to Playlist")

    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....")   


    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")  

    elif choice == 5:

        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")  

    elif choice == 6:
        list.shuffle()
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....")     

    elif choice == 7:
        list.showCurrentSong()
        print("Currently playing: ", end=" ")  

        # Display the song name and artist of the currently playing song

    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")

    elif choice == 0:
        print("Goodbye.")
        break


