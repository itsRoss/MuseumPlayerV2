from gipiozero import Button
from vlc import EventType
import time
import vlc

#function on press
#when button is pressed play the second video
def pressed():
    #add second video to medialist
    media_list_player.set_media_list(media_list2)

    #play second video
    media_list_player.play_item(media2)

    #set playlist to loop used when returning to the loop video
    media_list_player.set_media_list(media_list)

#function return to loop mode o to loop the first video
#argument is event video end reached
def returnVideoLoop(event):

    #set playlist playback mode to loop
    media_list_player.set_playback_mode(1)

    #play video loop
    media_list_player.play_item(media1)

#main
if __name__ == '__main__':

    #set up Button
    button17 = Button(17)
    button17.when_pressed = when_pressed

    #create mediaListPlayer object
    media_list_player = vlc.MediaListPlayer()

    #create vlc instance
    player = vlc.Instance()

    #create media list for loop video
    media_list = player.set_media_list_new()
    #create media list for one shot video
    media_list2 = player.set_media_list_new()

    #create media elements
    #loop video
    media1 = player.media_new("video.mp4")
    media_list.add_media(media1)
    #add media to media_list
    media_list_player.set_media_list(media_list)

    #one shot video
    media2 = player.media_new("video2.mp4")
    media_list2.add_media(media2)

    #new media player instance
    new_player = player.media_player_new()
    new_player.set_fullscreen(True)

    #setting media player to it
    media_list_player.set_media_player(new_player)
    media_list_player.set_playback_mode(1)
    media_list_player.play_item(media1)

    #event end video reached
    event_manager = media_list_player.event_manager()
    event = vlc.EventType()
    event_manager.event_attach(event.MediaPLayerEndReached, returnVideoLoop)

    while True:
        continue
