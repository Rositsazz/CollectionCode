from playlist import Playlist
from song import Song
import time
from MusicCrawler import MusicCrawler


def main():
    # s = Song(album="The Sons of Odin",
    #          title="Odin",
    #          artist="Manowar",
    #          length="3:44")
    # s1 = Song(album="The Sonds of Odin",
    #           title="Sons of Odin",
    #           artist="Manowar",
    #           length="6:08")
    # p = Playlist("Manowar songs", repeat="SONG")
    # p.add_song(s)
    # p.add_song(s1)
    # p.add_song(Song(album="Fallen",
    #                 title="Bring Me To Life (radio edit)",
    #                 artist="Evanesence",
    #                 length="3:30"))

    # p.pprint_playlist()
    crawler = MusicCrawler("/home/rositsazz/music")
    zrock = crawler.generate_playlist(playname="Test")
    zrock.pprint_playlist()
    zrock.save()
    # p.save()
    # p = Playlist.load("Manowar-songs.json")
    # try:
    #     while True:
    #         song = p.next_song()
    #         print(str(song))
    #         time.sleep(1)
    # except Exception as e:
    #     print(e)

if __name__ == '__main__':
    main()
