from abc import ABC, abstractmethod


# Wrong

class MediaPlayer(ABC):
    @abstractmethod
    def play_video(self, video_file):
        pass

    @abstractmethod
    def play_audio(self, audio_file):
        pass

    @abstractmethod
    def stop_video(self, video_file):
        pass

    @abstractmethod
    def stop_audio(self, audio_file):
        pass


# In this case, any class that implements the MediaPlayer interface would be forced to implement all the methods, even
# if it doesn't need them.


# Correct

class AudioPlayer(ABC):
    @abstractmethod
    def play_audio(self, audio_file):
        pass

    @abstractmethod
    def stop_audio(self, audio_file):
        pass


class VideoPlayer(ABC):
    @abstractmethod
    def play_video(self, video_file):
        pass

    @abstractmethod
    def stop_video(self, video_file):
        pass
