class Queue: 
    def __init__(self):
        self.songs = list()

    def addSong(self, song):
        if song not in self.songs:
            self.songs.insert(0,song)
            return True
        return False


    def enqueue(self, item):
        self.songs.insert(0, item)
    
    def dequeue(self):
        return self.songs.pop()

    def size(self):
        return len(self.songs)
    
    def isEmpty(self):
        return self.songs == []
    
    def peek(self):
        return self.songs[0]

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
    

list = Queue()

list.enqueue("Song 1")

